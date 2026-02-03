---
name: c-cpp-testing
description: C/C++ 测试模式 - Google Test/Mock、Catch2、单元测试、集成测试、测试驱动开发、内存泄漏检测
---

# C/C++ 测试模式

C/C++ 测试的最佳实践和模式。

## 测试框架

### Google Test (gtest)

```cpp
#include <gtest/gtest.h>

// 基本测试
TEST(FactorialTest, HandlesZeroInput) {
    EXPECT_EQ(factorial(0), 1);
}

TEST(FactorialTest, HandlesPositiveInput) {
    EXPECT_EQ(factorial(1), 1);
    EXPECT_EQ(factorial(2), 2);
    EXPECT_EQ(factorial(3), 6);
    EXPECT_EQ(factorial(8), 40320);
}

// 测试夹具
class QueueTest : public ::testing::Test {
protected:
    void SetUp() override {
        q1_.Enqueue(1);
        q2_.Enqueue(2);
        q2_.Enqueue(3);
    }

    Queue<int> q0_;
    Queue<int> q1_;
    Queue<int> q2_;
};

TEST_F(QueueTest, DefaultValueIsZero) {
    EXPECT_EQ(q0_.Size(), 0);
}
```

### Catch2

```cpp
#include <catch2/catch_test_macros.hpp>

TEST_CASE("factorial of 0 is 1", "[factorial]") {
    REQUIRE(factorial(0) == 1);
}

TEST_CASE("factorial of positive numbers", "[factorial]") {
    REQUIRE(factorial(1) == 1);
    REQUIRE(factorial(2) == 2);
    REQUIRE(factorial(3) == 6);
}

// BDD 风格
SCENARIO("vectors can be sized and resized") {
    GIVEN("A vector with some items") {
        std::vector<int> v(5);

        REQUIRE(v.size() == 5);
        REQUIRE(v.capacity() >= 5);

        WHEN("the size is increased") {
            v.resize(10);

            THEN("the size and capacity change") {
                REQUIRE(v.size() == 10);
                REQUIRE(v.capacity() >= 10);
            }
        }
    }
}
```

## 测试模式

### AAA 模式 (Arrange-Act-Assert)

```cpp
TEST(AccountTest, DepositIncreasesBalance) {
    // Arrange (准备)
    Account account(100);

    // Act (执行)
    account.deposit(50);

    // Assert (断言)
    EXPECT_EQ(account.balance(), 150);
}
```

### 参数化测试

```cpp
// Google Test
class PrimeTest : public ::testing::TestWithParam<int> {};

TEST_P(PrimeTest, ReturnsTrue) {
    int n = GetParam();
    EXPECT_TRUE(isPrime(n));
}

INSTANTIATE_TEST_SUITE_P(
    PrimeTests,
    PrimeTest,
    ::testing::Values(2, 3, 5, 7, 11, 13)
);
```

### Mock 对象 (Google Mock)

```cpp
class MockTurtle : public Turtle {
public:
    MOCK_METHOD(void, PenUp, (), (override));
    MOCK_METHOD(void, PenDown, (), (override));
    MOCK_METHOD(void, Forward, (int units), (override));
};

TEST(PainterTest, CanDrawSomething) {
    MockTurtle turtle;
    EXPECT_CALL(turtle, PenDown())
        .Times(1);

    Painter painter(&turtle);
    painter.DrawCircle(0, 0, 10);
}
```

## 内存泄漏检测

### Valgrind

```bash
# 使用 Valgrind 检测内存泄漏
valgrind --leak-check=full --show-leak-kinds=all ./test_program

# 输出示例:
# ==12345== LEAK SUMMARY:
# ==12345==    definitely lost: 40 bytes in 1 blocks
# ==12345==    indirectly lost: 0 bytes in 0 blocks
# ==12345==    possibly lost: 0 bytes in 0 blocks
```

### AddressSanitizer

```cpp
// 编译时启用 ASan
// g++ -fsanitize=address -g test.cpp

#include <iostream>

int main() {
    int* arr = new int[5];
    arr[5] = 42;  // 越界访问，ASan 会报告
    delete[] arr;
    return 0;
}
```

## TDD 实践

### Red-Green-Refactor

```cpp
// Step 1: RED - 写失败的测试
TEST(CalculatorTest, AddTwoNumbers) {
    Calculator calc;
    EXPECT_EQ(calc.add(2, 3), 5);  // 还未实现
}

// Step 2: GREEN - 最小实现
int Calculator::add(int a, int b) {
    return a + b;
}

// Step 3: REFACTOR - 改进代码质量
```

## 集成测试

```cpp
// 文件系统集成测试
class FileSystemTest : public ::testing::Test {
protected:
    std::string test_dir_ = "/tmp/test_fs_XXXXXX";
    char* dir_template_;

    void SetUp() override {
        dir_template_ = strdup(test_dir_.c_str());
        mkdtemp(dir_template_);
    }

    void TearDown() override {
        // 清理测试目录
        std::string command = "rm -rf " + std::string(dir_template_);
        system(command.c_str());
        free(dir_template_);
    }
};

TEST_F(FileSystemTest, CanWriteAndReadFile) {
    std::string filepath = std::string(dir_template_) + "/test.txt";

    // 写入文件
    std::ofstream out(filepath);
    out << "Hello, World!";
    out.close();

    // 读取文件
    std::ifstream in(filepath);
    std::string content;
    std::getline(in, content);

    EXPECT_EQ(content, "Hello, World!");
}
```

## 最佳实践

1. **测试命名**: 使用描述性名称，说明测试内容
2. **一个测试一个断言**: 保持测试简单明了
3. **使用测试夹具**: 共享设置代码
4. **避免测试间依赖**: 每个测试独立运行
5. **测试边界条件**: 包括空值、最大值等
6. **测试错误路径**: 确保错误处理正确
7. **保持测试快速**: 慢速测试标记为 SLOW
8. **使用 Mock**: 隔离外部依赖

## 编译和运行

```bash
# 使用 CMake
cmake -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build
ctest --test-dir build --verbose

# 使用 Google Test
./test_suite --gtest_filter=TestCase.TestName

# 使用 Valgrind
valgrind ./test_suite
```
