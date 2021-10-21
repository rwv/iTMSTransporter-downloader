# iTMSTransporter-downloader

<a href="https://github.com/rwv/iTMSTransporter-downloader/actions/workflows/download.yml">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/rwv/iTMSTransporter-downloader/Download%20iTMSTransporter%20components">
</a>

Download `~/Library/Caches/com.apple.amp.itmstransporter` manually to avoid network issue using [Transporter](https://apps.apple.com/us/app/transporter/id1450874784?mt=12).

Use [GitHub Actions](https://github.com/rwv/iTMSTransporter-downloader/actions) to update automatically.

## Usage

``` bash
python download.py
```

## Download dependencies pack manually

Go to [Actions · rwv/iTMSTransporter-downloader](https://github.com/rwv/iTMSTransporter-downloader/actions) and download the latest artifact. Put `com.apple.amp.itmstransporter.tar.gz.zip` under the root of repository and run `download.py`.

