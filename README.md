# CM Security Tools 🛡️

![logo](/resource/logo.png)

v(bata 0.3.8)    By 万能小魏 & ChicoMalo & MnznEux

## 📖 项目简介

CM Security Tools 是一款集成了多种网络安全扫描功能的综合工具包，由万能小魏、ChicoMalo和MnznEux联合开发。工具采用模块化设计，支持多线程扫描，旨在帮助安全研究人员快速进行常见的网络资产发现和安全检测。

## ✨ 功能特性

- 🖥️ **主机发现** - ARP扫描发现存活主机
- 🔌 **端口扫描** - 多线程TCP端口扫描
- 🗄️ **服务弱口令检测** - 支持MySQL、Redis、SSH等服务
- 🌐 **子域名枚举** - 快速发现目标域名的子域名
- 🎨 **炫酷界面** - 随机彩色Banner展示
- ⚡ **高效多线程** - 充分利用系统资源加速扫描
- 🧩 **模块化设计** - 易于扩展新功能

## 🛠️ 安装使用

### 环境要求

- Python 3.6+
- 以下Python库：
  - scapy
  - pymysql
  - redis
  - paramiko
  - requests

### 安装步骤

1. 克隆项目到本地：
```bash
git clone https://gitee.com/Chicomalo/chicomalo-tools.git
cd CM-Security-Tools
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行工具：
```bash
python cmtools.py --help
```

## 📋 使用指南

### IP主机发现
```bash
python cmtools.py ip -H 192.168.1.0 -N 24 -T 200
```

### 端口扫描
```bash
python cmtools.py port -H 192.168.1.1 -T 1000 -I 50
```

### MySQL弱口令扫描
```bash
python cmtools.py mysql -H 192.168.1.10 -P 3306 -u user.txt -p pass.txt -T 500
```

### Redis弱口令扫描
```bash
python cmtools.py redis -H 192.168.1.10 -P 6379 -p redis_pass.txt -T 500
```

### SSH弱口令扫描
```bash
python cmtools.py ssh -H 192.168.1.10 -P 22 -u user.txt -p pass.txt -T 500
```

### 子域名扫描
```bash
python cmtools.py subdomain -D example.com -S subdomains.txt -T 500
```

## 📁 项目结构

```
CM-Security-Tools/
├── cmtools.py              # 主程序入口
├── getTools.py             # 工具调用模块
├── Tools/                  # 工具模块目录
│   ├── scanip.py           # IP扫描模块
│   ├── scanport.py         # 端口扫描模块
│   ├── scanmysql.py        # MySQL扫描模块
│   ├── scanredis.py        # Redis扫描模块
│   ├── scanssh.py          # SSH扫描模块
│   └── scansubdomains.py   # 子域名扫描模块
├── resource/               # 资源文件目录
│   ├── commoncolors.py     # 颜色定义
│   ├── mnzneuxlog.py       # Logo和Banner
│   ├── user.dict           # 用户名字典
│   ├── passwd.dict         # 密码字典
│   └── subdomainsdict.txt  # 子域名字典
└── README.md               # 项目说明
```

## 🎯 功能模块详解

### 1. 主机发现 (IP Scan)
使用ARP协议扫描指定网段内存活的主机，显示IP和MAC地址。

### 2. 端口扫描 (Port Scan)
TCP连接式端口扫描，支持自定义线程数和扫描间隔。

### 3. MySQL弱口令检测
多线程测试MySQL数据库的弱口令，支持自定义用户名字典和密码字典。

### 4. Redis弱口令检测
检测Redis未授权访问和弱口令漏洞。

### 5. SSH弱口令检测
暴力破解SSH服务的登录凭证。

### 6. 子域名枚举
通过字典爆破发现目标的子域名。

## ⚠️ 免责声明

本工具仅用于安全测试和教育目的，使用者应遵守当地法律法规。开发者不对任何误用或损害承担责任。在使用本工具前，请确保您已获得适当的授权。

## 🤝 贡献指南

欢迎提交Issue和Pull Request来帮助改进这个项目！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👥 开发者团队

- **万能小魏** - 核心指导
- **Chico Malo** - 核心开发
- **MnznEux** - Logo设计及功能优化

---

**注意**: 请负责任地使用此工具，仅在对您拥有合法权限的系统上进行测试。
