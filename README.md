# YouTube Video & Audio Downloader

A lightweight, cross-platform command-line tool for downloading YouTube videos in **MP4** (best quality with audio) or **MP3** (audio only). Downloads are automatically saved to the system's `Downloads` folder.

Both Linux and Windows launchers are included. The tool uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to retrieve media and [`imageio-ffmpeg`](https://github.com/imageio/imageio-ffmpeg) to merge streams or convert audio without requiring a heavy system-wide FFmpeg installation.

## Features

- **Format selection:** Choose between **MP4** (video + audio) or **MP3** (192kbps audio extraction).
- **Zero system bloat:** Uses a portable FFmpeg binary via Python (`imageio-ffmpeg`) and automatically clears package caches (`pip`, `yt-dlp`, `imageio`) to save disk space.
- **Smart path detection:** Automatically locates (or creates) the user's `Downloads` directory across Linux (XDG support) and Windows.
- **Auto-setup:** Automatically checks for and installs required Python packages (`yt-dlp[default]`, `yt-dlp-ejs`, `imageio-ffmpeg`) on first run.

## Project Structure

```text
.
├── baixar.sh          # Linux launcher (or "Download videos.sh")
├── baixar.bat         # Windows launcher
└── v7ago.py           # Core Python script (cross-platform)
