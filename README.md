YouTube Downloader

Python Flask License

Aplikasi web sederhana dan efisien yang dibangun menggunakan Flask untuk mengunduh video dan audio dari YouTube. Alat ini memungkinkan pengguna untuk memasukkan URL YouTube, memilih format yang diinginkan (MP4 untuk video atau MP3 untuk audio), dan mengunduh konten langsung ke perangkat mereka.
Fitur
°Unduh video YouTube dalam format MP4 (kualitas video + audio terbaik).
°Ekstrak dan unduh audio dari video YouTube dalam format MP3.
°Antarmuka web yang sederhana dan ramah pengguna.
°Membersihkan unduhan sebelumnya secara otomatis untuk menghemat ruang.
°Penanganan kesalahan untuk URL yang tidak valid atau gagal mengunduh.
°Desain responsif untuk pengguna desktop dan mobile.

Prasyarat

Sebelum memulai, pastikan Anda telah menginstal hal-hal berikut di sistem Anda:

°Python 3.8+: Unduh Python

°yt-dlp: Alat baris perintah untuk mengunduh video YouTube.

°FFmpeg: Diperlukan untuk ekstraksi audio dan konversi format.

Instalasi
Ikuti langkah-langkah berikut untuk menyiapkan proyek secara lokal:
1. Kloning Repositori  

git clone https://github.com/CodeDarkSlayer/youtube-downloader.git
cd youtube-downloader

2. Buat Lingkungan Virtual (opsional tetapi disarankan)  

python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate

3. Instal Dependensi
Instal paket Python yang diperlukan menggunakan pip:

pip install flask

4. Instal yt-dlp
Instal yt-dlp menggunakan pip atau dengan mengunduh binari:

pip install yt-dlp

5. Instal FFmpeg  
Di Windows: Unduh FFmpeg dari sini dan tambahkan ke PATH sistem Anda.
Di macOS: Gunakan Homebrew:
brew install ffmpeg

Di Linux:
sudo apt-get install ffmpeg  # Untuk Debian/Ubuntu
sudo yum install ffmpeg      # Untuk CentOS/RHEL

Cara Penggunaan
1. Jalankan Aplikasi
Jalankan server Flask dengan perintah berikut:

python app.py

Aplikasi akan dihosting di http://localhost:5000 secara default.

2. Akses Antarmuka Web
Buka browser Anda dan kunjungi http://localhost:5000. Anda akan melihat antarmuka sederhana di mana Anda dapat memasukkan URL YouTube dan memilih format (MP4 atau MP3).

3. Unduh Video atau Audio  
Masukkan URL YouTube yang valid (contoh: https://www.youtube.com/watch?v=contoh).

Pilih format: MP4 (video) atau MP3 (audio).

Klik tombol "Unduh Sekarang" untuk memulai pengunduhan.

Setelah pengunduhan selesai, file akan otomatis diunduh ke perangkat Anda.
