# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个基于 langbot-app/LangBot 框架的崩坏3往世乐土攻略助手插件。该插件通过解析用户指令，提供乐土攻略图片和推荐内容。

## 技术架构

### 主要组件

- **main.py**: 核心插件逻辑，包含 `ElysianRealmAssistant` 类
- **ElysianRealmConfig.yaml**: 配置文件，存储角色名称映射到攻略文件名的关系
- **pyproject.toml**: Python 项目配置文件，包含依赖管理
- **requirements.txt**: 传统的依赖文件

### 核心功能模块

1. **消息处理系统**: 使用正则表达式匹配用户指令
2. **配置管理**: 动态加载和更新 YAML 配置文件
3. **图片缓存系统**: 本地缓存攻略图片，支持缓存清理
4. **API 集成**: 从米游社 API 获取最新推荐攻略
5. **错误处理**: 完善的异常处理和重试机制

### 指令模式

插件通过正则表达式匹配以下指令格式：
- `乐土list` / `[关键词]乐土list` - 查询配置信息
- `乐土推荐[数字]` / `全部乐土推荐` - 获取推荐攻略
- `[角色名]乐土[数字]` - 查询角色攻略
- `[角色名][流派]流` - 查询流派攻略
- `RealmCommand add [key] [values]` - 添加配置（管理员功能）

## 依赖管理

### Python 版本
- 需要 Python 3.13+

### 核心依赖
- `pyyaml` - YAML 配置文件处理
- `regex` - 增强的正则表达式支持
- `requests` - HTTP 请求处理

### 包管理
项目使用 `uv` 作为包管理器，也支持传统的 `pip` 安装方式。

## 常用命令

### 安装依赖
```bash
# 使用 uv（推荐）
uv sync

# 或使用 pip
pip install -r requirements.txt
```

### 开发环境
```bash
# 激活虚拟环境（如果使用 uv）
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 或者直接使用 uv 运行
uv run python main.py
```

## 配置文件结构

`ElysianRealmConfig.yaml` 使用以下结构：
```yaml
角色标识符:
  - 角色别名1
  - 角色别名2
  - ...
```

例如：
```yaml
Human:
  - 人律乐土
  - 爱律乐土
```

## 开发注意事项

### 文件编码
- 所有文件使用 UTF-8 编码
- Windows 脚本需要使用 CRLF 换行符

### 缓存系统
- 图片缓存存储在 `cache/` 目录
- 缓存文件使用 URL 的 MD5 值命名
- 插件启动时会自动清理过期缓存（默认保留365天，最大1GB）

### 日志系统
- 使用 LangBot 框架的日志系统 (`self.ap.logger`)
- 支持 `info`、`debug` 等日志级别

### 错误处理
- 网络请求包含重试机制
- 图片下载失败时有降级处理
- 配置文件加载错误时有默认处理

## 框架集成

该插件基于 langbot-app/LangBot 框架开发：
- 使用 `@register` 装饰器注册插件
- 使用 `@handler` 装饰器处理消息事件
- 支持群聊和私聊消息处理
- 使用 `platform_types` 进行消息格式化

### 消息处理流程
1. 接收消息事件 (`PersonNormalMessageReceived`/`GroupNormalMessageReceived`)
2. 正则表达式匹配指令格式
3. 根据指令类型路由到对应处理函数
4. 返回格式化的消息链（文本+图片）

### 图片处理
- 支持本地缓存和网络下载
- 使用 base64 编码传输图片
- 支持米游社和 GitHub 图片源