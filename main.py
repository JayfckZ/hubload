from flask import Flask, render_template, request, send_file
from pytubefix import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/a', methods=['POST'])
def baixarvideo():
    url = request.form.get('url')
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        caminho_arquivo = stream.download(output_path='downloads')
        return send_file(caminho_arquivo, as_attachment=True)
    except Exception as e:
        return f"Erro ao baixar vídeo: {e}"
    
    
@app.route('/b', methods=['POST'])
def baixaraudio():
    url = request.form.get('url')
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        caminho_arquivo = stream.download(output_path='downloads')
        return send_file(caminho_arquivo, as_attachment=True)
    except Exception as e:
        return f"Erro ao baixar áudio: {e}"


if __name__ == '__main__':
    app.run(debug=True)