---
name: python-testing
description: Python 测试策略，使用 pytest、TDD 方法论、fixtures、mocking、参数化和覆盖率要求。
---

# Python 测试模式

使用 pytest、TDD 方法论和最佳实践的 Python 应用程序综合测试策略。

## 何时激活

- 编写新的 Python 代码（遵循 TDD：红、绿、重构）
- 为 Python 项目设计测试套件
- 审查 Python 测试覆盖率
- 设置测试基础设施

## 核心测试理念

### 测试驱动开发 (TDD)

始终遵循 TDD 循环：

1. **RED（红）**：为期望的行为编写失败的测试
2. **GREEN（绿）**：编写最小代码使测试通过
3. **REFACTOR（重构）**：在保持测试绿色的同时改进代码

```python
# 步骤 1: 编写失败的测试 (RED)
def test_add_numbers():
    result = add(2, 3)
    assert result == 5

# 步骤 2: 编写最小实现 (GREEN)
def add(a, b):
    return a + b

# 步骤 3: 如需重构 (REFACTOR)
```

### 覆盖率要求

- **目标**：80%+ 代码覆盖率
- **关键路径**：要求 100% 覆盖率
- 使用 `pytest --cov` 测量覆盖率

```bash
pytest --cov=mypackage --cov-report=term-missing --cov-report=html
```

## pytest 基础

### 基本测试结构

```python
import pytest

def test_addition():
    """测试基本加法。"""
    assert 2 + 2 == 4

def test_string_uppercase():
    """测试字符串大写转换。"""
    text = "hello"
    assert text.upper() == "HELLO"

def test_list_append():
    """测试列表追加。"""
    items = [1, 2, 3]
    items.append(4)
    assert 4 in items
    assert len(items) == 4
```

### 断言

```python
# 相等
assert result == expected

# 不相等
assert result != unexpected

# 真值
assert result  # 真值
assert not result  # 假值
assert result is True  # 确切为 True
assert result is False  # 确切为 False
assert result is None  # 确切为 None

# 成员关系
assert item in collection
assert item not in collection

# 比较
assert result > 0
assert 0 <= result <= 100

# 类型检查
assert isinstance(result, str)

# 异常测试（推荐方式）
with pytest.raises(ValueError):
    raise ValueError("error message")

# 检查异常消息
with pytest.raises(ValueError, match="invalid input"):
    raise ValueError("invalid input provided")

# 检查异常属性
with pytest.raises(ValueError) as exc_info:
    raise ValueError("error message")
assert str(exc_info.value) == "error message"
```

## Fixtures

### 基本 Fixture 使用

```python
import pytest

@pytest.fixture
def sample_data():
    """提供示例数据的 fixture。"""
    return {"name": "Alice", "age": 30}

def test_sample_data(sample_data):
    """使用 fixture 的测试。"""
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
```

### 带设置/清理的 Fixture

```python
@pytest.fixture
def database():
    """带设置和清理的 fixture。"""
    # 设置
    db = Database(":memory:")
    db.create_tables()
    db.insert_test_data()

    yield db  # 提供给测试

    # 清理
    db.close()

def test_database_query(database):
    """测试数据库操作。"""
    result = database.query("SELECT * FROM users")
    assert len(result) > 0
```

### Fixture 作用域

```python
# 函数作用域（默认）- 每个测试运行
@pytest.fixture
def temp_file():
    with open("temp.txt", "w") as f:
        yield f
    os.remove("temp.txt")

# 模块作用域 - 每个模块运行一次
@pytest.fixture(scope="module")
def module_db():
    db = Database(":memory:")
    db.create_tables()
    yield db
    db.close()

# 会话作用域 - 每个测试会话运行一次
@pytest.fixture(scope="session")
def shared_resource():
    resource = ExpensiveResource()
    yield resource
    resource.cleanup()
```

### 带参数的 Fixture

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    """参数化 fixture。"""
    return request.param

def test_numbers(number):
    """测试运行 3 次，每个参数一次。"""
    assert number > 0
```

### 使用多个 Fixtures

```python
@pytest.fixture
def user():
    return User(id=1, name="Alice")

@pytest.fixture
def admin():
    return User(id=2, name="Admin", role="admin")

def test_user_admin_interaction(user, admin):
    """使用多个 fixtures 的测试。"""
    assert admin.can_manage(user)
```

### 自动使用的 Fixtures

```python
@pytest.fixture(autouse=True)
def reset_config():
    """在每个测试之前自动运行。"""
    Config.reset()
    yield
    Config.cleanup()

def test_without_fixture_call():
    # reset_config 自动运行
    assert Config.get_setting("debug") is False
```

### Conftest.py 用于共享 Fixtures

```python
# tests/conftest.py
import pytest

@pytest.fixture
def client():
    """所有测试的共享 fixture。"""
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_headers(client):
    """为 API 测试生成认证头。"""
    response = client.post("/api/login", json={
        "username": "test",
        "password": "test"
    })
    token = response.json["token"]
    return {"Authorization": f"Bearer {token}"}
```

## 参数化

### 基本参数化

```python
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("PyThOn", "PYTHON"),
])
def test_uppercase(input, expected):
    """测试运行 3 次，使用不同的输入。"""
    assert input.upper() == expected
```

### 多个参数

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    """使用多个输入测试加法。"""
    assert add(a, b) == expected
```

### 带 IDs 的参数化

```python
@pytest.mark.parametrize("input,expected", [
    ("valid@email.com", True),
    ("invalid", False),
    ("@no-domain.com", False),
], ids=["valid-email", "missing-at", "missing-domain"])
def test_email_validation(input, expected):
    """使用可读测试 ID 测试邮箱验证。"""
    assert is_valid_email(input) is expected
```

### 参数化 Fixtures

```python
@pytest.fixture(params=["sqlite", "postgresql", "mysql"])
def db(request):
    """针对多个数据库后端测试。"""
    if request.param == "sqlite":
        return Database(":memory:")
    elif request.param == "postgresql":
        return Database("postgresql://localhost/test")
    elif request.param == "mysql":
        return Database("mysql://localhost/test")

def test_database_operations(db):
    """测试运行 3 次，每个数据库一次。"""
    result = db.query("SELECT 1")
    assert result is not None
```

## 标记和测试选择

### 自定义标记

```python
# 标记慢速测试
@pytest.mark.slow
def test_slow_operation():
    time.sleep(5)

# 标记集成测试
@pytest.mark.integration
def test_api_integration():
    response = requests.get("https://api.example.com")
    assert response.status_code == 200

# 标记单元测试
@pytest.mark.unit
def test_unit_logic():
    assert calculate(2, 3) == 5
```

### 运行特定测试

```bash
# 仅运行快速测试
pytest -m "not slow"

# 仅运行集成测试
pytest -m integration

# 运行集成或慢速测试
pytest -m "integration or slow"

# 运行标记为 unit 但非 slow 的测试
pytest -m "unit and not slow"
```

### 在 pytest.ini 中配置标记

```ini
[pytest]
markers =
    slow: 标记慢速测试
    integration: 标记集成测试
    unit: 标记单元测试
    django: 标记需要 Django 的测试
```

## 模拟和补丁

### 模拟函数

```python
from unittest.mock import patch, Mock

@patch("mypackage.external_api_call")
def test_with_mock(api_call_mock):
    """使用模拟的外部 API 进行测试。"""
    api_call_mock.return_value = {"status": "success"}

    result = my_function()

    api_call_mock.assert_called_once()
    assert result["status"] == "success"
```

### 模拟返回值

```python
@patch("mypackage.Database.connect")
def test_database_connection(connect_mock):
    """使用模拟的数据库连接进行测试。"""
    connect_mock.return_value = MockConnection()

    db = Database()
    db.connect()

    connect_mock.assert_called_once_with("localhost")
```

### 模拟异常

```python
@patch("mypackage.api_call")
def test_api_error_handling(api_call_mock):
    """使用模拟异常测试错误处理。"""
    api_call_mock.side_effect = ConnectionError("Network error")

    with pytest.raises(ConnectionError):
        api_call()

    api_call_mock.assert_called_once()
```

### 模拟上下文管理器

```python
@patch("builtins.open", new_callable=mock_open)
def test_file_reading(mock_file):
    """使用模拟的 open 测试文件读取。"""
    mock_file.return_value.read.return_value = "file content"

    result = read_file("test.txt")

    mock_file.assert_called_once_with("test.txt", "r")
    assert result == "file content"
```

### 使用 Autospec

```python
@patch("mypackage.DBConnection", autospec=True)
def test_autospec(db_mock):
    """使用 autospec 测试以捕获 API 误用。"""
    db = db_mock.return_value
    db.query("SELECT * FROM users")

    # 如果 DBConnection 没有 query 方法，这将失败
    db_mock.assert_called_once()
```

### 模拟类实例

```python
class TestUserService:
    @patch("mypackage.UserRepository")
    def test_create_user(self, repo_mock):
        """使用模拟的仓库测试用户创建。"""
        repo_mock.return_value.save.return_value = User(id=1, name="Alice")

        service = UserService(repo_mock.return_value)
        user = service.create_user(name="Alice")

        assert user.name == "Alice"
        repo_mock.return_value.save.assert_called_once()
```

### 模拟属性

```python
@pytest.fixture
def mock_config():
    """创建带属性的模拟对象。"""
    config = Mock()
    type(config).debug = PropertyMock(return_value=True)
    type(config).api_key = PropertyMock(return_value="test-key")
    return config

def test_with_mock_config(mock_config):
    """使用模拟的配置属性进行测试。"""
    assert mock_config.debug is True
    assert mock_config.api_key == "test-key"
```

## 测试异步代码

### 使用 pytest-asyncio 的异步测试

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    """测试异步函数。"""
    result = await async_add(2, 3)
    assert result == 5

@pytest.mark.asyncio
async def test_async_with_fixture(async_client):
    """使用异步 fixture 测试异步。"""
    response = await async_client.get("/api/users")
    assert response.status_code == 200
```

### 异步 Fixture

```python
@pytest.fixture
async def async_client():
    """提供异步测试客户端的异步 fixture。"""
    app = create_app()
    async with app.test_client() as client:
        yield client

@pytest.mark.asyncio
async def test_api_endpoint(async_client):
    """使用异步 fixture 进行测试。"""
    response = await async_client.get("/api/data")
    assert response.status_code == 200
```

### 模拟异步函数

```python
@pytest.mark.asyncio
@patch("mypackage.async_api_call")
async def test_async_mock(api_call_mock):
    """使用模拟测试异步函数。"""
    api_call_mock.return_value = {"status": "ok"}

    result = await my_async_function()

    api_call_mock.assert_awaited_once()
    assert result["status"] == "ok"
```

## 测试异常

### 测试预期的异常

```python
def test_divide_by_zero():
    """测试除以零引发 ZeroDivisionError。"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_custom_exception():
    """测试带消息的自定义异常。"""
    with pytest.raises(ValueError, match="invalid input"):
        validate_input("invalid")
```

### 测试异常属性

```python
def test_exception_with_details():
    """测试带自定义属性的异常。"""
    with pytest.raises(CustomError) as exc_info:
        raise CustomError("error", code=400)

    assert exc_info.value.code == 400
    assert "error" in str(exc_info.value)
```

## 测试副作用

### 测试文件操作

```python
import tempfile
import os

def test_file_processing():
    """使用临时文件测试文件处理。"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("test content")
        temp_path = f.name

    try:
        result = process_file(temp_path)
        assert result == "processed: test content"
    finally:
        os.unlink(temp_path)
```

### 使用 pytest 的 tmp_path Fixture 测试

```python
def test_with_tmp_path(tmp_path):
    """使用 pytest 内置的临时路径 fixture 进行测试。"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello world")

    result = process_file(str(test_file))
    assert result == "hello world"
    # tmp_path 自动清理
```

### 使用 tmpdir Fixture 测试

```python
def test_with_tmpdir(tmpdir):
    """使用 pytest 的 tmpdir fixture 进行测试。"""
    test_file = tmpdir.join("test.txt")
    test_file.write("data")

    result = process_file(str(test_file))
    assert result == "data"
```

## 测试组织

### 目录结构

```
tests/
├── conftest.py                 # 共享 fixtures
├── __init__.py
├── unit/                       # 单元测试
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_utils.py
│   └── test_services.py
├── integration/                # 集成测试
│   ├── __init__.py
│   ├── test_api.py
│   └── test_database.py
└── e2e/                        # 端到端测试
    ├── __init__.py
    └── test_user_flow.py
```

### 测试类

```python
class TestUserService:
    """在类中分组相关测试。"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """设置在这个类中的每个测试之前运行。"""
        self.service = UserService()

    def test_create_user(self):
        """测试用户创建。"""
        user = self.service.create_user("Alice")
        assert user.name == "Alice"

    def test_delete_user(self):
        """测试用户删除。"""
        user = User(id=1, name="Bob")
        self.service.delete_user(user)
        assert not self.service.user_exists(1)
```

## 最佳实践

### 应该做的

- **遵循 TDD**：在编写代码之前编写测试（红-绿-重构）
- **测试一件事**：每个测试应该验证单个行为
- **使用描述性名称**：`test_user_login_with_invalid_credentials_fails`
- **使用 fixtures**：使用 fixtures 消除重复
- **模拟外部依赖**：不依赖外部服务
- **测试边缘情况**：空输入、None 值、边界条件
- **目标 80%+ 覆盖率**：专注于关键路径
- **保持测试快速**：使用标记分离慢速测试

### 不应该做的

- **不要测试实现**：测试行为，而非内部
- **不要在测试中使用复杂的条件**：保持测试简单
- **不要忽略测试失败**：所有测试必须通过
- **不要测试第三方代码**：信任库能正常工作
- **不要在测试之间共享状态**：测试应该独立
- **不要在测试中捕获异常**：使用 `pytest.raises`
- **不要使用 print 语句**：使用断言和 pytest 输出
- **不要编写太脆弱的测试**：避免过于具体的模拟

## 常见模式

### 测试 API 端点 (FastAPI/Flask)

```python
@pytest.fixture
def client():
    app = create_app(testing=True)
    return app.test_client()

def test_get_user(client):
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json["id"] == 1

def test_create_user(client):
    response = client.post("/api/users", json={
        "name": "Alice",
        "email": "alice@example.com"
    })
    assert response.status_code == 201
    assert response.json["name"] == "Alice"
```

### 测试数据库操作

```python
@pytest.fixture
def db_session():
    """创建测试数据库会话。"""
    session = Session(bind=engine)
    session.begin_nested()
    yield session
    session.rollback()
    session.close()

def test_create_user(db_session):
    user = User(name="Alice", email="alice@example.com")
    db_session.add(user)
    db_session.commit()

    retrieved = db_session.query(User).filter_by(name="Alice").first()
    assert retrieved.email == "alice@example.com"
```

### 测试类方法

```python
class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add(self, calculator):
        assert calculator.add(2, 3) == 5

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)
```

## pytest 配置

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --strict-markers
    --disable-warnings
    --cov=mypackage
    --cov-report=term-missing
    --cov-report=html
markers =
    slow: 标记慢速测试
    integration: 标记集成测试
    unit: 标记单元测试
```

### pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--cov=mypackage",
    "--cov-report=term-missing",
    "--cov-report=html",
]
markers = [
    "slow: 标记慢速测试",
    "integration: 标记集成测试",
    "unit: 标记单元测试",
]
```

## 运行测试

```bash
# 运行所有测试
pytest

# 运行特定文件
pytest tests/test_utils.py

# 运行特定测试
pytest tests/test_utils.py::test_function

# 使用详细输出运行
pytest -v

# 使用覆盖率运行
pytest --cov=mypackage --cov-report=html

# 仅运行快速测试
pytest -m "not slow"

# 运行直到第一次失败
pytest -x

# 运行并在 N 次失败后停止
pytest --maxfail=3

# 运行上次失败的测试
pytest --lf

# 使用模式运行测试
pytest -k "test_user"

# 失败时使用调试器运行
pytest --pdb
```

## 快速参考

| 模式 | 用法 |
|---------|-------|
| `pytest.raises()` | 测试预期的异常 |
| `@pytest.fixture()` | 创建可复用的测试 fixtures |
| `@pytest.mark.parametrize()` | 使用多个输入运行测试 |
| `@pytest.mark.slow` | 标记慢速测试 |
| `pytest -m "not slow"` | 跳过慢速测试 |
| `@patch()` | 模拟函数和类 |
| `tmp_path` fixture | 自动临时目录 |
| `pytest --cov` | 生成覆盖率报告 |
| `assert` | 简单可读的断言 |

**记住**：测试也是代码。保持它们干净、可读和可维护。好的测试捕获错误；伟大的测试预防错误。
