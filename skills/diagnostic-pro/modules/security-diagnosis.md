# Security Diagnosis 模块

安全诊断模块，识别和修复安全漏洞。

## 触发条件

- 添加身份验证或授权
- 处理用户输入或文件上传
- 创建新的 API 端点
- 使用密钥或凭证
- 实现支付功能
- 存储或传输敏感数据
- 集成第三方 API

## 安全检查清单

### 1. 密钥管理

#### ❌ 绝不要这样做
```typescript
const apiKey = "sk-proj-xxxxx"  // 硬编码密钥
const dbPassword = "password123" // 源代码中的密码
```

#### ✅ 始终这样做
```typescript
const apiKey = process.env.OPENAI_API_KEY
const dbUrl = process.env.DATABASE_URL

// 验证密钥存在
if (!apiKey) {
  throw new Error('OPENAI_API_KEY not configured')
}
```

### 2. 输入验证

#### 始终验证用户输入
```typescript
import { z } from 'zod'

const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150)
})

export async function createUser(input: unknown) {
  try {
    const validated = CreateUserSchema.parse(input)
    return await db.users.create(validated)
  } catch (error) {
    if (error instanceof z.ZodError) {
      return { success: false, errors: error.errors }
    }
    throw error
  }
}
```

### 3. SQL 注入预防

#### ❌ 永远不要拼接 SQL
```typescript
// 危险 - SQL 注入漏洞
const query = `SELECT * FROM users WHERE email = '${userEmail}'`
await db.query(query)
```

#### ✅ 始终使用参数化查询
```typescript
// 安全 - 参数化查询
const { data } = await supabase
  .from('users')
  .select('*')
  .eq('email', userEmail)
```

### 4. 认证与授权

#### JWT Token 处理
```typescript
// ❌ 错误: localStorage (易受 XSS 攻击)
localStorage.setItem('token', token)

// ✅ 正确: httpOnly cookies
res.setHeader('Set-Cookie',
  `token=${token}; HttpOnly; Secure; SameSite=Strict; Max-Age=3600`)
```

### 5. XSS 预防

```typescript
import DOMPurify from 'isomorphic-dompurify'

// 始终清理用户提供的 HTML
function renderUserContent(html: string) {
  const clean = DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p'],
    ALLOWED_ATTR: []
  })
  return <div dangerouslySetInnerHTML={{ __html: clean }} />
}
```

### 6. CSRF 保护

```typescript
import { csrf } from '@/lib/csrf'

export async function POST(request: Request) {
  const token = request.headers.get('X-CSRF-Token')

  if (!csrf.verify(token)) {
    return NextResponse.json(
      { error: 'Invalid CSRF token' },
      { status: 403 }
    )
  }

  // 处理请求
}
```

### 7. 速率限制

```typescript
import rateLimit from 'express-rate-limit'

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 分钟
  max: 100, // 每个窗口 100 个请求
  message: 'Too many requests'
})

app.use('/api/', limiter)
```

### 8. 敏感数据暴露

```typescript
// ❌ 错误: 记录敏感数据
console.log('User login:', { email, password })

// ✅ 正确: 编辑敏感数据
console.log('User login:', { email, userId })
```

## 安全扫描命令

```bash
# 检查硬编码密钥
grep -rn "sk-" --include="*.ts" --include="*.js" . 2>/dev/null | head -10
grep -rn "api_key" --include="*.ts" --include="*.js" . 2>/dev/null | head -10
grep -rn "password" --include="*.ts" --include="*.js" . 2>/dev/null | head -10
grep -rn "secret" --include="*.ts" --include="*.js" . 2>/dev/null | head -10

# 检查 console.log
grep -rn "console.log" --include="*.ts" --include="*.tsx" src/ 2>/dev/null | head -10

# 检查 TODO/FIXME
grep -rn "TODO\|FIXME" --include="*.ts" --include="*.js" src/ 2>/dev/null | head -10
```

## 部署前安全检查清单

- [ ] **密钥**: 无硬编码密钥，全部在环境变量中
- [ ] **输入验证**: 所有用户输入已验证
- [ ] **SQL 注入**: 所有查询使用参数化
- [ ] **XSS**: 用户内容已清理
- [ ] **CSRF**: 保护已启用
- [ ] **认证**: 正确的 token 处理
- [ ] **授权**: 角色检查就位
- [ ] **速率限制**: 所有端点已启用
- [ ] **HTTPS**: 生产环境强制执行
- [ ] **安全头**: CSP, X-Frame-Options 已配置
- [ ] **错误处理**: 错误中无敏感数据
- [ ] **日志**: 日志中无敏感数据
- [ ] **依赖**: 最新，无已知漏洞
