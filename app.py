from flask import Flask, render_template, request, send_file, jsonify
import os
import requests
import shutil

app = Flask(__name__)

# Folder untuk menyimpan video yang diunduh
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Konfigurasi API YouTube Media Downloader dari RapidAPI
API_KEY = os.getenv("API_KEY", "044d8892a9msh51b5c0e40615619p104023jsnbb634a112907")  # Ganti dengan API key-mu
API_HOST = "youtube-media-downloader.p.rapidapi.com"
API_URL = "https://youtube-media-downloader.p.rapidapi.com/api/youtube"

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

    try:
        # Kirim permintaan ke API YouTube Media Downloader
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        params = {
            "url": url
        }
        response = requests.get(API_URL, headers=headers, params=params)
        data = response.json()

        if data.get("status") != "success":
            return jsonify({'status': 'error', 'message': data.get("message", "Gagal mengunduh video!")})

        # Unduh file dari URL yang diberikan oleh API
        video_url = data["video"]["download_url"]
        video_filename = data["video"]["title"] + f".{format}"
        video_path = os.path.join(DOWNLOAD_FOLDER, video_filename)

        with open(video_path, 'wb') as f:
            video_response = requests.get(video_url, stream=True)
            for chunk in video_response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return jsonify({
            'status': 'success',
            'message': 'Video berhasil diunduh!',
            'filename': video_filename
        })

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
