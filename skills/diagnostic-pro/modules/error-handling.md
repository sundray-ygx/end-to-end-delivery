# Error Handling 模块

错误处理模式库，提供健壮的错误处理策略。

## 核心概念

### 错误处理哲学

**异常 vs Result 类型**:
- **异常**: 传统 try-catch，打乱控制流
- **Result 类型**: 显式成功/失败，函数式方法
- **错误代码**: C 风格，需要纪律
- **Option/Maybe 类型**: 用于可空值

**使用场景**:
- 异常: 意外错误，异常条件
- Result 类型: 预期错误，验证失败
- Panic/崩溃: 不可恢复错误，编程 bug

### 错误分类

**可恢复错误**:
- 网络超时
- 缺失文件
- 无效用户输入
- API 速率限制

**不可恢复错误**:
- 内存不足
- 栈溢出
- 编程 bug (空指针等)

## Python 错误处理

### 自定义异常层次

```python
class ApplicationError(Exception):
    """应用错误基类"""
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
        self.timestamp = datetime.utcnow()

class ValidationError(ApplicationError):
    """验证失败时抛出"""
    pass

class NotFoundError(ApplicationError):
    """资源未找到时抛出"""
    pass

# 使用
def get_user(user_id: str) -> User:
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise NotFoundError(
            f"User not found",
            code="USER_NOT_FOUND",
            details={"user_id": user_id}
        )
    return user
```

### 上下文管理器清理

```python
from contextlib import contextmanager

@contextmanager
def database_transaction(session):
    """确保事务提交或回滚"""
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

# 使用
with database_transaction(db.session) as session:
    user = User(name="Alice")
    session.add(user)
    # 自动提交或回滚
```

### 指数退避重试

```python
import time
from functools import wraps

def retry(max_attempts: int = 3, backoff_factor: float = 2.0):
    """带指数退避的重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        sleep_time = backoff_factor ** attempt
                        time.sleep(sleep_time)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3)
def fetch_data(url: str) -> dict:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
```

## TypeScript/JavaScript 错误处理

### 自定义错误类

```typescript
class ApplicationError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500,
    public details?: Record<string, any>,
  ) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}

class ValidationError extends ApplicationError {
  constructor(message: string, details?: Record<string, any>) {
    super(message, "VALIDATION_ERROR", 400, details);
  }
}

class NotFoundError extends ApplicationError {
  constructor(resource: string, id: string) {
    super(`${resource} not found`, "NOT_FOUND", 404, { resource, id });
  }
}
```

### Result 类型模式

```typescript
type Result<T, E = Error> =
  | { success: true; value: T }
  | { success: false; error: E };

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await db.findUser(id);
    if (!user) {
      return { success: false, error: new NotFoundError("User", id) };
    }
    return { success: true, value: user };
  } catch (e) {
    return { success: false, error: e as Error };
  }
}

// 使用
const result = await fetchUser("123");
if (result.success) {
  console.log(result.value.name);
} else {
  console.error(result.error.message);
}
```

### 异步错误处理

```typescript
// Promise 链错误处理
async function fetchData() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    if (error instanceof TypeError) {
      // 网络错误
      console.error("Network error:", error);
    } else if (error instanceof SyntaxError) {
      // JSON 解析错误
      console.error("Invalid JSON:", error);
    } else {
      // 其他错误
      console.error("Unknown error:", error);
    }
    throw error;
  }
}
```

## Go 错误处理

### 错误包装

```go
package service

import (
    "errors"
    "fmt"
)

var (
    ErrUserNotFound = errors.New("user not found")
    ErrInvalidInput = errors.New("invalid input")
)

func GetUser(id string) (*User, error) {
    user, err := db.FindUser(id)
    if err != nil {
        return nil, fmt.Errorf("failed to find user: %w", err)
    }
    if user == nil {
        return nil, ErrUserNotFound
    }
    return user, nil
}
```

### 自定义错误类型

```go
type AppError struct {
    Code    string
    Message string
    Cause   error
}

func (e *AppError) Error() string {
    if e.Cause != nil {
        return fmt.Sprintf("%s: %s (caused by: %v)", e.Code, e.Message, e.Cause)
    }
    return fmt.Sprintf("%s: %s", e.Code, e.Message)
}

func (e *AppError) Unwrap() error {
    return e.Cause
}

// 使用
func ProcessOrder(order *Order) error {
    if order.Total <= 0 {
        return &AppError{
            Code:    "INVALID_AMOUNT",
            Message: "order total must be positive",
        }
    }
    // ...
}
```

## 高级模式

### 熔断器模式

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half-open

    def call(self, func):
        def wrapper(*args, **kwargs):
            if self.state == "open":
                if time.time() - self.last_failure_time > self.timeout:
                    self.state = "half-open"
                else:
                    raise Exception("Circuit breaker is open")

            try:
                result = func(*args, **kwargs)
                if self.state == "half-open":
                    self.state = "closed"
                    self.failures = 0
                return result
            except Exception as e:
                self.failures += 1
                self.last_failure_time = time.time()
                if self.failures >= self.failure_threshold:
                    self.state = "open"
                raise
        return wrapper
```

### 优雅降级

```typescript
async function fetchDataWithFallback(
  primary: () => Promise<Data>,
  fallback: () => Promise<Data>
): Promise<Data> {
  try {
    return await primary();
  } catch (error) {
    console.warn("Primary failed, using fallback:", error);
    return await fallback();
  }
}

// 使用
const data = await fetchDataWithFallback(
  () => fetchFromPrimaryAPI(),
  () => fetchFromCache()
);
```

## 最佳实践

1. **尽早失败**: 在输入验证阶段捕获错误
2. **提供上下文**: 错误消息应包含足够的上下文信息
3. **不要捕获所有异常**: 只捕获能处理的异常
4. **记录错误**: 记录错误以便调试
5. **优雅降级**: 提供备用方案而不是直接失败
6. **重试策略**: 对临时性错误使用重试
7. **错误传播**: 让错误向上传播到能处理它的地方
