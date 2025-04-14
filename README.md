# YouTube Downloader

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/Flask-Web_Framework-lightgrey" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

## Overview

**YouTube Downloader** adalah aplikasi web sederhana dan efisien yang dibangun menggunakan Flask untuk mengunduh video dan audio dari YouTube. Alat ini memungkinkan pengguna untuk memasukkan URL YouTube, memilih format yang diinginkan (MP4 untuk video atau MP3 untuk audio), dan mengunduh konten langsung ke perangkat mereka.

---

## Fitur

- ⚡ Unduh video YouTube dalam format MP4 (video + audio kualitas terbaik)
- 🎵 Ekstrak dan unduh audio dalam format MP3
- 🧠 Antarmuka web yang user-friendly
- ♻️ Pembersihan otomatis unduhan sebelumnya
- ❌ Penanganan kesalahan URL tidak valid
- 📱 Desain responsif untuk desktop & mobile

---

## Prasyarat

Sebelum memulai, pastikan Anda telah menginstal berikut ini di sistem Anda:

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **yt-dlp** — Alat command-line untuk mengunduh dari YouTube
- **FFmpeg** — Untuk ekstraksi audio dan konversi format

---

## Instalasi

### 1. Kloning Repositori
```bash
git clone https://github.com/r00tH3x/youtube-downloader.git
cd youtube-downloader
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instal Dependensi Python
```bash
pip install flask
```

### 4. Instal yt-dlp
```bash
pip install yt-dlp
```

### 5. Instal FFmpeg

#### Windows:
- [Download FFmpeg](https://ffmpeg.org/download.html) lalu tambahkan ke PATH

#### macOS:
```bash
brew install ffmpeg
```

#### Linux:
```bash
# Debian/Ubuntu
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg
```

---

## Cara Penggunaan

### 1. Jalankan Aplikasi
```bash
python app.py
```

Aplikasi akan berjalan di: `http://localhost:5000`

### 2. Akses Antarmuka Web
Buka browser dan kunjungi `http://localhost:5000`. Masukkan URL YouTube dan pilih format (MP4 / MP3).

### 3. Unduh Konten
- Masukkan URL YouTube yang valid (contoh: `https://www.youtube.com/watch?v=XXXX`)
- Pilih format: `MP4` (video) atau `MP3` (audio)
- Klik **"Unduh Sekarang"** untuk mulai proses pengunduhan

---

## Lisensi

Distribusikan di bawah lisensi MIT. Lihat file `LICENSE` untuk detail lengkapnya.

---

## Kontribusi

Pull request sangat diterima! Untuk perubahan besar, silakan buka issue terlebih dahulu untuk diskusi.

---

> **r00tH3x** — Tools built to educate, not to exploit.
