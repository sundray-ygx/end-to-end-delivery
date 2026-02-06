---
name: python-patterns
description: Python 开发模式 - Pythonic 惯用法、PEP 8 标准、类型提示和构建健壮高效可维护 Python 应用程序的最佳实践。
---

# Python 开发模式

构建健壮、高效、可维护应用程序的 Pythonic 惯用法和最佳实践。

## 何时激活

- 编写新的 Python 代码
- 审查 Python 代码
- 重构现有 Python 代码
- 设计 Python 包/模块

## 核心原则

### 1. 可读性优先

Python 优先考虑可读性。代码应该显而易见且易于理解。

```python
# 好的实践：清晰可读
def get_active_users(users: list[User]) -> list[User]:
    """从提供的列表中仅返回活跃用户。"""
    return [user for user in users if user.is_active]


# 不好的实践：聪明但令人困惑
def get_active_users(u):
    return [x for x in u if x.a]
```

### 2. 显式优于隐式

避免魔法；明确代码的功能。

```python
# 好的实践：显式配置
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 不好的实践：隐藏的副作用
import some_module
some_module.setup()  # 这做了什么？
```

### 3. EAFP - 请求原谅比许可更容易

Python 优先使用异常处理而非条件检查。

```python
# 好的实践：EAFP 风格
def get_value(dictionary: dict, key: str) -> Any:
    try:
        return dictionary[key]
    except KeyError:
        return default_value

# 不好的实践：LBYL (Look Before You Leap) 风格
def get_value(dictionary: dict, key: str) -> Any:
    if key in dictionary:
        return dictionary[key]
    else:
        return default_value
```

## 类型提示

### 基本类型注解

```python
from typing import Optional, List, Dict, Any

def process_user(
    user_id: str,
    data: Dict[str, Any],
    active: bool = True
) -> Optional[User]:
    """处理用户并返回更新后的 User 或 None。"""
    if not active:
        return None
    return User(user_id, data)
```

### 现代类型提示 (Python 3.9+)

```python
# Python 3.9+ - 使用内置类型
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Python 3.8 及更早版本 - 使用 typing 模块
from typing import List, Dict

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
```

### 泛型

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# 使用
stack: Stack[int] = Stack()
stack.push(1)
```

### Protocol（结构子类型）

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())  # 类型检查通过
render(Square())  # 类型检查通过
```

## Pythonic 惯用法

### 列表推导

```python
# 好的实践：列表推导
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# 不好：使用循环
squares = []
for x in range(10):
    squares.append(x**2)
```

### 字典和集合推导

```python
# 字典推导
word_lengths = {word: len(word) for word in ["hello", "world"]}

# 集合推导
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}
```

### 上下文管理器

```python
# 好的实践：使用 with 语句
with open("file.txt", "r") as f:
    content = f.read()
# 文件自动关闭

# 不好：手动管理
f = open("file.txt", "r")
content = f.read()
f.close()  # 如果抛出异常可能不会执行
```

### 枚举

```python
# 好的实践：使用 enumerate
for i, item in enumerate(items):
    print(f"Index {i}: {item}")

# 不好：手动索引
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")
```

### Zip

```python
# 好的实践：使用 zip
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 不好：手动索引
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")
```

### 生成器表达式

```python
# 好的实践：生成器表达式（内存高效）
sum_of_squares = sum(x**2 for x in range(1000000))

# 不好：列表推导（创建临时列表）
sum_of_squares = sum([x**2 for x in range(1000000)])
```

## 装饰器

### 基本装饰器

```python
import functools
import time

def timer(func):
    """测量函数执行时间的装饰器。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"
```

### 带参数的装饰器

```python
def repeat(times: int):
    """重复执行函数指定次数的装饰器。"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# greet("Alice") 返回 ["Hello, Alice!", "Hello, Alice!", "Hello, Alice!"]
```

### 类装饰器

```python
class CountCalls:
    """统计函数调用次数的类装饰器。"""
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")
```

## 错误处理

### 异常层次结构

```python
class ApplicationError(Exception):
    """应用程序错误基类。"""
    pass

class ValidationError(ApplicationError):
    """验证失败时引发。"""
    pass

class NotFoundError(ApplicationError):
    """资源未找到时引发。"""
    pass

# 使用
def get_user(user_id: str) -> User:
    if not user_id:
        raise ValidationError("user_id cannot be empty")

    user = database.find(user_id)
    if not user:
        raise NotFoundError(f"User {user_id} not found")

    return user
```

### 上下文中的异常处理

```python
# 使用 finally 确保清理
def process_file(filename: str):
    f = None
    try:
        f = open(filename, "r")
        # 处理文件
    except IOError as e:
        print(f"Error reading file: {e}")
        raise
    finally:
        if f:
            f.close()

# 更好的实践：使用 with
def process_file(filename: str):
    try:
        with open(filename, "r") as f:
            # 处理文件
            pass
    except IOError as e:
        print(f"Error reading file: {e}")
        raise
```

### 链式异常

```python
def load_config(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigError(f"Config file not found: {path}") from e
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in config: {path}") from e
```

## 并发

### asyncio (Python 3.7+)

```python
import asyncio

async def fetch_data(url: str) -> dict:
    """异步获取数据。"""
    await asyncio.sleep(1)  # 模拟 I/O
    return {"url": url, "data": "sample"}

async def main():
    # 并发运行多个协程
    results = await asyncio.gather(
        fetch_data("https://api.example.com/1"),
        fetch_data("https://api.example.com/2"),
        fetch_data("https://api.example.com/3")
    )
    for result in results:
        print(result)

asyncio.run(main())
```

### 线程池

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_item(item: int) -> int:
    time.sleep(0.1)  # 模拟 I/O
    return item * 2

def main():
    items = range(10)

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_item, items))

    print(results)

if __name__ == "__main__":
    main()
```

### 多进程 (CPU 密集型)

```python
from concurrent.futures import ProcessPoolExecutor
import math

def compute_factorial(n: int) -> int:
    return math.factorial(n)

def main():
    numbers = [10000, 20000, 30000, 40000, 50000]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_factorial, numbers))

    for n, result in zip(numbers, results):
        print(f"{n}! has {len(str(result))} digits")

if __name__ == "__main__":
    main()
```

## 包和模块组织

### 标准项目结构

```
myproject/
├── pyproject.toml           # 现代 Python 项目配置
├── README.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── main.py
│       ├── utils.py
│       └── subpackage/
│           └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
└── docs/
```

### __init__.py 最佳实践

```python
# src/mypackage/__init__.py
"""我的包的简短描述。"""

__version__ = "1.0.0"

# 导出公共 API
from mypackage.main import PublicClass, public_function

__all__ = ["PublicClass", "public_function", "__version__"]
```

### 相对导入

```python
# 在包内使用相对导入
from . import utils
from .subpackage import module
from .. import parent_module
```

## 数据类

### dataclass (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    """表示用户的简单数据类。"""
    name: str
    email: str
    age: int = 0
    friends: List['User'] = field(default_factory=list)

    def send_message(self, message: str) -> None:
        """发送消息给用户。"""
        print(f"Sending to {self.name}: {message}")

# 使用
alice = User(name="Alice", email="alice@example.com", age=30)
bob = User(name="Bob", email="bob@example.com")

alice.friends.append(bob)
```

### 不可变 dataclass

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    """不可变的二维点。"""
    x: float
    y: float

# Point 继承自 tuple，不可修改
p = Point(1.0, 2.0)
# p.x = 3.0  # 引发 FrozenInstanceError
```

## 最佳实践

### 1. 遵循 PEP 8

```python
# 使用 pycodestyle 或 black 检查代码风格
# pip install black
# black myproject/

# 函数和变量使用 snake_case
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

# 类使用 PascalCase
class ShoppingCart:
    pass

# 常量使用 UPPER_SNAKE_CASE
MAX_RETRIES = 3
```

### 2. 使用虚拟环境

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 导出依赖
pip freeze > requirements.txt
```

### 3. 文档字符串

```python
def calculate_compound_interest(
    principal: float,
    rate: float,
    periods: int
) -> float:
    """计算复利。

    Args:
        principal: 本金金额
        rate: 每期利率（例如，0.05 表示 5%）
        periods: 计息期数

    Returns:
        最终金额，包括利息

    Example:
        >>> calculate_compound_interest(1000, 0.05, 10)
        1628.89...
    """
    return principal * (1 + rate) ** periods
```

### 4. 日志记录

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_data(data: dict) -> None:
    logger.debug(f"Processing data: {data}")

    try:
        result = complex_calculation(data)
        logger.info("Calculation completed successfully")
    except Exception as e:
        logger.error(f"Calculation failed: {e}", exc_info=True)
        raise

# 使用
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    process_data({"key": "value"})
```

## 工具集成

### 类型检查 (mypy)

```bash
# 安装 mypy
pip install mypy

# 运行类型检查
mypy src/

# pyproject.toml 配置
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### 代码格式化 (black)

```bash
# 安装 black
pip install black

# 格式化代码
black src/

# 检查格式（不修改文件）
black --check src/
```

### 导入排序 (isort)

```bash
# 安装 isort
pip install isort

# 排序导入
isort src/

# 与 black 配合使用
isort --profile black src/
```

### 代码检查 (flake8/pylint)

```bash
# 安装 flake8
pip install flake8

# 运行检查
flake8 src/

# 安装 pylint
pip install pylint

# 运行 pylint
pylint src/
```

## 快速参考

| 惯用法 | 描述 |
|--------|------|
| 列表推导 | `[x for x in items if condition]` |
| 上下文管理器 | `with open(file) as f:` |
| enumerate | `for i, item in enumerate(items):` |
| zip | `for a, b in zip(list_a, list_b):` |
| 生成器表达式 | `(x for x in items)` - 内存高效 |
| f-strings | `f"{variable}"` - Python 3.6+ |
| dataclass | `@dataclass` - 简化类定义 |
| 类型提示 | `def func(x: int) -> str:` |
| asyncio | `async/await` - 异步编程 |

**记住**：Python 代码应该是可读的。"胜于聪明，清晰更好。"代码被阅读的次数远多于被编写的次数。
