#!/usr/bin/env bash

# Entra automaticamente na pasta onde o script está guardado
cd "$(dirname "$0")"

echo "[*] A verificar dependências e armazenamento..."

# Verifica se yt_dlp e imageio_ffmpeg já estão instalados no Python
if python3 -c "import yt_dlp, imageio_ffmpeg" &> /dev/null; then
    echo "[*] Bibliotecas encontradas! A limpar caches desnecessários..."
    python3 -m pip cache purge &> /dev/null
    rm -rf ~/.cache/yt-dlp ~/.cache/imageio ~/.cache/pip
else
    echo "[*] A instalar dependências leves (sem guardar lixo no disco)..."
    python3 -m pip install --no-cache-dir yt-dlp imageio-ffmpeg --break-system-packages || \
    python3 -m pip install --no-cache-dir yt-dlp imageio-ffmpeg
    echo "[+] Instalação concluída!"
fi

echo ""
# Executa o script Python
python3 v7ago.py
