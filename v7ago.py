import sys
import subprocess
import shutil
from pathlib import Path

def verificar_e_limpar_ambiente():
    pacotes = ['yt_dlp', 'imageio_ffmpeg']
    faltando = []

    for pacote in pacotes:
        try:
            __import__(pacote)
        except ImportError:
            faltando.append(pacote.replace('_', '-'))

    if faltando:
        print(f"[*] A instalar dependências em falta ({', '.join(faltando)})...")
        cmd = [sys.executable, "-m", "pip", "install", "--no-cache-dir"] + faltando
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            subprocess.run(cmd + ["--break-system-packages"], check=True)
        print("[+] Instalação concluída!\n")
    else:
        subprocess.run([sys.executable, "-m", "pip", "cache", "purge"], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        pastas_cache = [
            Path.home() / ".cache" / "yt-dlp",
            Path.home() / ".cache" / "imageio",
            Path.home() / ".cache" / "pip",
            Path.home() / "AppData" / "Local" / "pip" / "Cache",
            Path.home() / "AppData" / "Local" / "imageio"
        ]
        for pasta in pastas_cache:
            if pasta.exists():
                shutil.rmtree(pasta, ignore_errors=True)

def obter_pasta_downloads():
    home = Path.home()
    
    # Lê a configuração oficial de pastas do Linux (XDG)
    config_xdg = home / ".config" / "user-dirs.dirs"
    if config_xdg.exists():
        try:
            for linha in config_xdg.read_text().splitlines():
                if linha.startswith("XDG_DOWNLOAD_DIR"):
                    caminho = linha.split("=")[1].strip('"').replace("$HOME", str(home))
                    pasta_xdg = Path(caminho)
                    if pasta_xdg.exists():
                        return pasta_xdg
        except Exception:
            pass

    # Procura pelos nomes padrão em Inglês e Português
    for nome in ["Downloads", "Transferências", "Download", "Baixados"]:
        tentativa = home / nome
        if tentativa.exists() and tentativa.is_dir():
            return tentativa

    # Cria a pasta Downloads se não existir nenhuma
    pasta_padrao = home / "Downloads"
    pasta_padrao.mkdir(parents=True, exist_ok=True)
    return pasta_padrao

verificar_e_limpar_ambiente()

import yt_dlp
import imageio_ffmpeg

download_path = obter_pasta_downloads()
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

url = input("Digite a URL do video do Youtube: ").strip()

if url:
    ydl_opts = {
        'outtmpl': str(download_path / '%(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'ffmpeg_location': ffmpeg_exe,
        'merge_output_format': 'mp4',
        'cachedir': False,
    }

    try:
        print(f"\n[*] Pasta de destino: {download_path}")
        print("[*] A baixar em alta qualidade com áudio...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n[+] Download concluído com sucesso! Guardado em: {download_path}")

    except Exception as e:
        print(f"\n[!] Ocorreu um erro durante o processo: {e}")
