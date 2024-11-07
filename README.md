[English](README_EN.md)

## 代理指南

### 先决条件
* 已安装 `miniconda`

### 入门

打开 proxy.py 文件并将 `TARGET_HOST` 和 `TARGET_PORT` 变量修改为您的目标服务器和端口。

运行脚本：
```bash
./run.sh
```

第一次执行会自动安装 `mitmproxy` 和 `requirements.txt` 中的依赖项。

### 解释列表

* `FORWARD_DOMAINS`：要转发的域名列表。
* `EXCLUDED_DOMAINS`：不转发的域名列表。
* `LOG_KEYWORDS`：要记录的关键字列表。

## 信任 mitmproxy CA (必须)

建议参考官方指南 [https://docs.mitmproxy.org/stable/concepts-certificates/](https://docs.mitmproxy.org/stable/concepts-certificates/)。

安装 `mitmproxy` 后，它会在 `~/.mitmproxy` 目录中创建几个文件。

列出 mitmproxy CA 文件：
```bash
$ ls -1 ~/.mitmproxy 
mitmproxy-ca-cert.cer
mitmproxy-ca-cert.p12
mitmproxy-ca-cert.pem
mitmproxy-ca.p12
mitmproxy-ca.pem
mitmproxy-dhparam.pem
```

下面是针对不同操作系统的简要指南。

### MacOS

打开 **钥匙串访问** 并将 `mitmproxy-ca-cert.pem` 文件导入到 **系统** 钥匙串。

默认情况下，证书不被信任。双击证书并选择 **信任** -> **使用此证书时** -> **始终信任**。

完成。

### Windows

使用 `mitmproxy-ca-cert.p12` 文件将证书导入到 **受信任的根证书颁发机构** 存储。**当前用户** 和 **本地计算机** 都可以。如果您有管理员权限，最好将其导入到 **本地计算机** 存储。

完成。

## 致谢

* [https://docs.mitmproxy.org/stable/concepts-certificates/](https://docs.mitmproxy.org/stable/concepts-certificates/)
* [https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

