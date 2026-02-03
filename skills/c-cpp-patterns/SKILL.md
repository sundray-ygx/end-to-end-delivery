---
name: c-cpp-patterns
description: C/C++ 开发模式 - 现代 C++ (C++11/14/17/20) 最佳实践、内存管理、STL 使用、RAII 模式、智能指针、并发编程
---

# C/C++ 开发模式

现代 C++ 开发最佳实践，涵盖 C++11/14/17/20 特性。

## 核心原则

### 1. RAII (Resource Acquisition Is Initialization)

```cpp
// ❌ 错误: 手动资源管理
void processFile(const char* filename) {
    FILE* f = fopen(filename, "r");
    // ... 使用文件
    fclose(f);  // 可能因为异常而跳过
}

// ✅ 正确: 使用 RAII
void processFile(const std::string& filename) {
    std::ifstream file(filename);
    // ... 使用文件
    // 自动关闭，即使发生异常
}
```

### 2. 智能指针优先

```cpp
// ❌ 错误: 原始指针所有权
class MyClass {
    User* user_;
public:
    MyClass() : user_(new User()) {}
    ~MyClass() { delete user_; }  // 可能复制后双重删除
};

// ✅ 正确: 使用 unique_ptr
class MyClass {
    std::unique_ptr<User> user_;
public:
    MyClass() : user_(std::make_unique<User>()) {}
    // 自动删除，不可复制但可移动
};
```

### 3. 值语义优先

```cpp
// ❌ 不必要的指针
void printUser(const User* user);

// ✅ 值传递或引用传递
void printUser(const User& user);  // 大对象用引用
void printId(int id);              // 小对象用值
```

## 内存管理

### 智能指针使用

```cpp
// unique_ptr - 独占所有权
auto ptr = std::make_unique<MyClass>();

// shared_ptr - 共享所有权
auto shared = std::make_shared<MyClass>();

// weak_ptr - 避免循环引用
std::weak_ptr<MyClass> weak = shared;

// 不要混用原始指针和智能指针
```

### 避免内存泄漏

```cpp
// 使用 STL 容器自动管理内存
std::vector<std::unique_ptr<User>> users;
users.push_back(std::make_unique<User>());

// 使用标准算法代替手动循环
std::vector<int> numbers = {1, 2, 3, 4, 5};
auto result = std::accumulate(numbers.begin(), numbers.end(), 0);
```

## STL 使用

### 容器选择

```cpp
// std::vector - 默认选择，连续内存
std::vector<int> vec = {1, 2, 3};

// std::map - 有序键值对
std::map<std::string, int> ages;

// std::unordered_map - 哈希表，O(1) 查找
std::unordered_map<std::string, int> cache;

// std::string - 字符串处理
std::string str = "Hello";
```

### 算法使用

```cpp
// 使用算法代替循环
std::vector<int> vec = {1, 2, 3, 4, 5};

// 查找
auto it = std::find(vec.begin(), vec.end(), 3);

// 排序
std::sort(vec.begin(), vec.end());

// 变换
std::transform(vec.begin(), vec.end(), vec.begin(),
               [](int x) { return x * 2; });
```

## 现代C++特性

### auto 类型推导

```cpp
// 自动推导类型
auto x = 42;                    // int
auto y = std::make_unique<T>(); // unique_ptr<T>
auto& z = something();          // 引用

// 范围 for 循环
for (const auto& item : container) {
    process(item);
}
```

### Lambda 表达式

```cpp
// 基本语法
auto lambda = [](int x) { return x * 2; };

// 捕获上下文
int factor = 2;
auto multiply = [factor](int x) { return x * factor; };

// 可变捕获
auto accumulator = [sum = 0](int x) mutable {
    sum += x;
    return sum;
};
```

### 移动语义

```cpp
// 避免不必要的拷贝
std::string createString() {
    return "Hello";  // RVO (Return Value Optimization)
}

// 使用 std::move 转移所有权
std::string str = "Hello";
std::string other = std::move(str);  // str 现在为空

// 容器使用移动语义
std::vector<std::string> vec;
vec.push_back(std::string("Hello"));  // 移动构造
```

## 并发编程

### std::thread

```cpp
#include <thread>

void worker(int id) {
    // 工作线程逻辑
}

// 创建线程
std::thread t(worker, 1);

// 等待完成
t.join();

// 分离线程
t.detach();
```

### std::mutex 和锁

```cpp
#include <mutex>

class ThreadSafeCounter {
    mutable std::mutex mutex_;
    int count_ = 0;
public:
    void increment() {
        std::lock_guard<std::mutex> lock(mutex_);
        ++count_;
    }

    int get() const {
        std::lock_guard<std::mutex> lock(mutex_);
        return count_;
    }
};
```

### 条件变量

```cpp
#include <condition_variable>

std::mutex mutex_;
std::condition_variable cv_;
bool ready = false;

void worker() {
    std::unique_lock<std::mutex> lock(mutex_);
    cv_.wait(lock, [] { return ready; });
    // 处理数据
}

void signal() {
    {
        std::lock_guard<std::mutex> lock(mutex_);
        ready = true;
    }
    cv_.notify_one();
}
```

## 错误处理

### 异常安全

```cpp
// RAII 确保异常安全
class FileManager {
    std::ofstream file_;
public:
    FileManager(const std::string& filename)
        : file_(filename) {}

    // 析构函数自动关闭文件
    ~FileManager() {
        // 即使发生异常也会执行
    }

    // 禁止拷贝，允许移动
    FileManager(const FileManager&) = delete;
    FileManager& operator=(const FileManager&) = delete;
    FileManager(FileManager&&) = default;
    FileManager& operator=(FileManager&&) = default;
};
```

### noexcept

```cpp
// 标记不抛异常的函数
int safeFunction() noexcept {
    return 42;
}

// 条件 noexcept
template<typename T>
void process(T t) noexcept(std::is_nothrow_copy_constructible<T>::value) {
    // ...
}
```

## 最佳实践

1. **使用现代C++特性**: auto、range-for、lambda、智能指针
2. **避免原始指针**: 使用智能指针管理所有权
3. **RAII优先**: 让对象生命周期管理资源
4. **值语义优先**: 减少指针使用，提高代码清晰度
5. **const 正确性**: 尽可能使用 const
6. **使用 STL**: 不要重新发明轮子
7. **异常安全**: 确保资源正确释放
8. **移动语义**: 避免不必要的拷贝
