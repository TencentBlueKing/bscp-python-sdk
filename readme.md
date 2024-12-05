## BSCP-PYTHON-SDK

[![license](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)]()

[EnglishDocs](./readme_en.md)

## Overview

bscp-python-sdk 是蓝鲸 BSCP 项目的 Python SDK，它能帮助你轻松访问项目保存在 BSCP 上的配置内容。

## Features

- kv 配置拉取
- kv 配置 watch

## 使用示例

### 安装

```bash
python -m pip install bk-bscp
```

注: 只支持 `Python 3.8+` 版本

### 客户端对象 `BscpClient`

使用 `BscpClient` 来完成主要操作，其支持两种不同的调用风格。

普通风格：

```python
from bk_bscp.client import BscpClient

client = BscpClient(server_addrs, token, biz_id)
try:
    pair = client.get("app1", "key1")
finally:
    client.close()
```

- 普通风格要求你手动管理连接，适合复用长连接，在需要完成大量操作时使用

上下文管理器风格：

```python
from bk_bscp.client import BscpClient

with BscpClient(server_addrs, token, biz_id) as client:
    pair = client.get("app1", "key1")
```

- 在这种风格下，client 的连接会自动关闭，适合短连接，操作次数不多时的场景

### 示例文件

更多示例代码请参考 examples/ 目录。

### 开发指南

安装环境

```bash
# 安装版本, 修改{version}为版本好， 如3.18， 如果已经有版本，步骤忽略
uv python install {version}

# 创建环境, 修改{path}为python真实路径
uv venv -p {path}/python

# 安装依赖
uv sync --frozen
```

执行单元测试：

```bash
uv run pytest -s tests/
```

一些相关的环境变量配置项：

```bash
# 设置日志打印级别，默认为 INFO
BSCP_LOG_LEVEL=DEBUG
```

#### 启用集成测试

为了更好地测试 SDK 的功能，本项目编写了一些会连接真实 BSCP 服务器的集成测试用例。这些测试默认处于未启用状态，你可以配置以下环境变量来启用：

```bash
BSCP_SERVER_ADDRS="your-bscp.example.com:9090"
BSCP_TOKEN="your_token"
BSCP_BIZ_ID="1"

# 启用 Get 功能测试
BSCP_EXISTENT_APP_KEY="your_app,your_key"
```

#### 同步自动生成的 gRPC 源码文件

在项目的 `bk_bscp/grpc_lib` 目录里，存放着由 grpc 相关工具链自动生成的 Python 源码文件。需注意的是，这些源码所依赖的原始 proto 定义文件，并未保存在本 SDK 项目中，而是存放于 bscp 主项目里。当你需要更新这批文件时，请先将 bscp 项目克隆到本地，切换到项目根目录中，执行以下命令：

```bash
find ./pkg/protocol/core ./pkg/protocol/feed-server -name "*.proto" | \
    xargs python -m grpc_tools.protoc -I. -I ./pkg/thirdparty/protobuf/ --python_out=. --pyi_out=. --grpc_python_out=.
```

然后，回到本 SDK 项目的 scripts/ 子目录，执行以下脚本完成同步：

```bash
# 将 {bscp_project_path} 替换为真实的 bscp 项目目录
bash sync_grpc_generated.sh {bscp_project_path}
```

## Support

- [蓝鲸论坛](https://bk.tencent.com/s-mart/community)
- [蓝鲸 DevOps 在线视频教程](https://bk.tencent.com/s-mart/video/)
- 联系我们，技术交流QQ群：

<img src="https://github.com/Tencent/bk-PaaS/raw/master/docs/resource/img/bk_qq_group.png" width="250" hegiht="250" align=center />

## BlueKing Community

- [BK-CI](https://github.com/Tencent/bk-ci)：蓝鲸持续集成平台是一个开源的持续集成和持续交付系统，可以轻松将你的研发流程呈现到你面前。
- [BK-BCS](https://github.com/Tencent/bk-bcs)：蓝鲸容器管理平台是以容器技术为基础，为微服务业务提供编排管理的基础服务平台。
- [BK-PaaS](https://github.com/Tencent/bk-PaaS)：蓝鲸PaaS平台是一个开放式的开发平台，让开发者可以方便快捷地创建、开发、部署和管理SaaS应用。
- [BK-SOPS](https://github.com/Tencent/bk-sops)：标准运维（SOPS）是通过可视化的图形界面进行任务流程编排和执行的系统，是蓝鲸体系中一款轻量级的调度编排类SaaS产品。
- [BK-CMDB](https://github.com/Tencent/bk-cmdb)：蓝鲸配置平台是一个面向资产及应用的企业级配置管理平台。

## Contributing

如果你有好的意见或建议，欢迎给我们提 Issues 或 Pull Requests，为蓝鲸开源社区贡献力量。

## License

bscp-python-sdk 是基于MIT协议， 详细请参考[LICENSE](./LICENSE.txt)。
