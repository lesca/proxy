[中文](README.md)
## Proxy Guidance

### Prerequisites
* `miniconda` is installed on your computer.

### Getting Started

Open the proxy.py file and modify the `TARGET_HOST` and `TARGET_PORT` variables to your target server and port.

Run the script:
```bash
./run.sh
```

For the first time, the script will automatically install `mitmproxy` and the dependencies in `requirements.txt`.

### Explaining the lists

* `FORWARD_DOMAINS`: List of domains to forward.
* `EXCLUDED_DOMAINS`: List of domains to NOT forward.
* `LOG_KEYWORDS`: List of keywords to log.


## Trust mitmproxy CA (Mandatory)

It's recommended to refer to the official guide [https://docs.mitmproxy.org/stable/concepts-certificates/](https://docs.mitmproxy.org/stable/concepts-certificates/).

After `mitmproxy` is installed, it creates several files in the `~/.mitmproxy` directory.

List mitmproxy CA files:
```bash
$ ls -1 ~/.mitmproxy 
mitmproxy-ca-cert.cer
mitmproxy-ca-cert.p12
mitmproxy-ca-cert.pem
mitmproxy-ca.p12
mitmproxy-ca.pem
mitmproxy-dhparam.pem
```

Here is a brief guide for different operating systems.

### MacOS

Open **KeyChain** and import the `mitmproxy-ca-cert.pem` file to the **System** keychain.

By default, the certificate is not trusted. Double click on the certificate and select **Trust** -> **When using this certificate** -> **Always Trust**.

It's done.

### Windows

Use `mitmproxy-ca-cert.p12` file to import the certificate to the **Trusted Root Certification Authorities** store. Both **Current User** and **Local Machine** are OK. If you have admin access, it's better to import it to **Local Machine** store.

It's done.

## Credits

* [https://docs.mitmproxy.org/stable/concepts-certificates/](https://docs.mitmproxy.org/stable/concepts-certificates/)
* [https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)
