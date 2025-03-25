from flask import Flask, render_template, request, send_file, jsonify
import os
import subprocess
import shutil

app = Flask(__name__)

# Folder untuk menyimpan video yang diunduh
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    format = request.form.get('format', 'mp4')  # Default ke mp4

    if not url:
        return jsonify({'status': 'error', 'message': 'URL tidak boleh kosong!'})

    # Bersihkan folder downloads sebelum unduh baru
    for file in os.listdir(DOWNLOAD_FOLDER):
        file_path = os.path.join(DOWNLOAD_FOLDER, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    # Tentukan format output
    output_template = os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s')
    if format == 'mp3':
        command = [
            'yt-dlp',
            '--proxy', 'http://91.107.130.145:11000',  # Ganti dengan proxy yang valid
            '--extract-audio',
            '--audio-format', 'mp3',
            '-o', output_template,
            url
        ]
    else:
        command = [
            'yt-dlp',
            '--proxy', 'http://91.107.130.145:11000',  # Ganti dengan proxy yang valid
            '-f', 'bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '-o', output_template,
            url
        ]

    try:
        # Jalankan perintah yt-dlp
        subprocess.run(command, check=True)

        # Cari file yang diunduh
        downloaded_files = os.listdir(DOWNLOAD_FOLDER)
        if not downloaded_files:
            return jsonify({'status': 'error', 'message': 'Gagal mengunduh video!'})

        # Ambil file pertama yang diunduh
        file_path = os.path.join(DOWNLOAD_FOLDER, downloaded_files[0])
        return jsonify({
            'status': 'success',
            'message': 'Video berhasil diunduh!',
            'filename': downloaded_files[0]
        })

    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': f'Error saat mengunduh: {str(e)}'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {str(e)}'})

@app.route('/get-file/<filename>')
def get_file(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({'status': 'error', 'message': 'File tidak ditemukan!'})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
