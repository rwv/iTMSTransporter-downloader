# iTMSTransporter-downloader

<a href="https://github.com/rwv/iTMSTransporter-downloader/actions/workflows/download.yml">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/rwv/iTMSTransporter-downloader/Download%20iTMSTransporter%20components">
</a>

[English version README.md](https://github.com/rwv/iTMSTransporter-downloader/blob/main/README-en.md)

手动下载 `~/Library/Caches/com.apple.amp.itmstransporter`，防止 [Transporter](https://apps.apple.com/us/app/transporter/id1450874784?mt=12) 上传时的网络问题。

使用 [GitHub Actions](https://github.com/rwv/iTMSTransporter-downloader/actions) 自动更新，保持最新版本。

## 使用方式

``` bash
python3 download.py
```

## 手动下载依赖包

前往 [Actions · rwv/iTMSTransporter-downloader](https://github.com/rwv/iTMSTransporter-downloader/actions) 下载最新生成的 Artifact，将下载的 `com.apple.amp.itmstransporter.tar.gz.zip` 放置在项目根目录下，并运行 `download.py`。

