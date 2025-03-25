
document.getElementById('downloadForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const url = document.getElementById('urlInput').value;
    const format = document.getElementById('formatSelect').value;
    const status = document.getElementById('status');
    const loading = document.getElementById('loading');

    // Reset status dan tampilkan loading
    status.innerHTML = '';
    loading.classList.remove('hidden');

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'url': url,
                'format': format
            })
        });

        const data = await response.json();
        loading.classList.add('hidden');
        status.textContent = data.message;
        status.className = `status ${data.status}`;

        if (data.status === 'success') {
            const downloadLink = document.createElement('a');
            downloadLink.href = `/get-file/${data.filename}`;
            downloadLink.download = data.filename;
            downloadLink.textContent = 'Klik di sini untuk mengunduh file';
            downloadLink.style.color = '#ff6b6b';
            downloadLink.style.textDecoration = 'none';
            downloadLink.style.fontWeight = '600';
            status.appendChild(document.createElement('br'));
            status.appendChild(downloadLink);
        }
    } catch (err) {
        loading.classList.add('hidden');
        status.textContent = 'Error: Gagal menghubungi server!';
        status.className = 'status error';
        console.error(err);
    }
});
