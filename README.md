# 小米Watch S4 主题项目

这是一个为小米Watch S4智能手表设计的主题项目。

## 实现目的

- 为小米Watch S4用户提供个性化的表盘主题
- 简化主题开发流程，降低开发门槛
- 提供完整的主题开发框架和工具
- 支持多种表盘元素和动画效果

## 实现路径

1. 搭建项目基础结构，包括目录组织和配置文件
2. 实现核心功能模块，如画布渲染、元素管理等
3. 提供主题构建和测试工具
4. 编写开发文档和使用指南
5. 优化主题性能和兼容性

## 项目结构

```
mi-watch-s4-theme/
├── README.md          # 项目说明文件
├── CHANGELOG.md       # 修订日志
├── package.json       # 项目配置文件
└── src/
    ├── main.py        # 主程序入口
    ├── widgets/       # 界面组件库
    ├── utils/         # 实用工具集
    └── data/          # 资源数据文件
```

## 功能特性

- 支持小米Watch S4智能手表
- 可自定义表盘样式
- 支持动画效果
- 支持多种字体样式
- 提供完整的主题开发框架

## 使用方法

1. 安装依赖：`npm install`
2. 开发主题：修改src目录下的文件
3. 构建主题：`npm run build`
4. 导入手表：通过小米穿戴App导入生成的RPK文件

## 开发指导

### 主题配置

修改 `src/data/config.json` 文件来自定义主题：

- `theme_name`：主题名称
- `version`：主题版本
- `author`：作者名称
- `screen_size`：屏幕尺寸（小米Watch S4为1.43）
- `resolution`：屏幕分辨率（小米Watch S4为466x466）
- `elements`：表盘元素配置，包括时间、日期、电池、步数、心率等
- `background`：背景配置
- `animations`：动画配置

### 组件开发

在 `src/widgets/` 目录下添加自定义组件：

- `canvas.py`：画布和基础元素类
- 可添加其他组件文件，如 `clock.py`、`weather.py` 等

### 工具函数

在 `src/utils/` 目录下添加工具函数：

- `helper.py`：主题辅助工具，包括配置管理、验证和构建

### 构建和测试

- 构建主题：`python3 src/main.py build`
- 测试主题：`python3 src/main.py test`
- 开发模式：`python3 src/main.py dev`

## 开发规范

- 遵循小米手表主题开发规范
- 确保主题在小米Watch S4上正常显示
- 优化主题性能，避免卡顿
- 确保主题兼容小米Watch S4的屏幕尺寸和分辨率
- 遵循代码风格和命名规范

## 变更记录

详见 [CHANGELOG.md](CHANGELOG.md) 文件。
