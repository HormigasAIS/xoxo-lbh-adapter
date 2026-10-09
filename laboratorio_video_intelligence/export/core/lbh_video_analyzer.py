#!/usr/bin/env python3

import os
import sys
import json
import time
import hmac
import hashlib
import subprocess
import shutil
import yt_dlp
import numpy as np

from PIL import Image
from datetime import datetime
import contextlib

# Configuración soberana
import sys as _sys
_sys.path.insert(0, '/data/data/com.termux/files/home/hormigasais-core/video_checker')

try:
    from cortex_hormiga import consultar_cortex
    CORTEX_OK = True
except:
    CORTEX_OK = False

HMAC_KEY = b'hormigasais-sovereign-2026'

BASE_DIR = os.path.expanduser(
    '~/xoxo-lbh-adapter/laboratorio_video_intelligence'
)

TMP_DIR = os.path.join(BASE_DIR, 'tmp')
FRAME_DIR = os.path.join(TMP_DIR, 'frames')

os.makedirs(FRAME_DIR, exist_ok=True)

def lbh_sig(payload):
    return hmac.new(
        HMAC_KEY,
        payload.encode(),
        hashlib.sha256
    ).hexdigest()[:16]

def descargar_video(url):

    tmp_video = os.path.join(TMP_DIR, 'buffer.mp4')

    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': tmp_video,
        'quiet': True,
        'no_warnings': True,
        'logtostderr': False
    }

    with open(os.devnull, 'w') as f, \
        contextlib.redirect_stdout(f), \
        contextlib.redirect_stderr(f):

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    return tmp_video

def extraer_frames(video_path):

    if os.path.exists(FRAME_DIR):
        shutil.rmtree(FRAME_DIR)

    os.makedirs(FRAME_DIR, exist_ok=True)

    output_pattern = os.path.join(
        FRAME_DIR,
        'frame_%04d.jpg'
    )

    cmd = [
        'ffmpeg',
        '-i',
        video_path,
        '-vf',
        'fps=1',
        output_pattern,
        '-hide_banner',
        '-loglevel',
        'error',
        '-y'
    ]

    subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def analizar_frames():

    archivos = sorted([
        f for f in os.listdir(FRAME_DIR)
        if f.endswith('.jpg')
    ])

    metricas = []

    for archivo in archivos[:10]:

        ruta = os.path.join(FRAME_DIR, archivo)

        try:
            img = Image.open(ruta).convert('L')

            arr = np.array(img)

            score = np.std(arr)

            metricas.append(score)

        except:
            pass

    if not metricas:
        return 50.0

    score_final = np.std(metricas) * 2

    return min(100, float(score_final))

def analizar_video_real(video_path):

    extraer_frames(video_path)

    return analizar_frames()

def procesar_analisis(url):

    try:

        video_path = descargar_video(url)

        score = analizar_video_real(video_path)

        es_humano = score > 45

        clasificacion = (
            "HUMANO_CONFIRMADO"
            if es_humano
            else "IA_DETECTADA"
        )

        ts = int(time.time())

        if CORTEX_OK:

            try:

                cortex = consultar_cortex(
                    url,
                    score,
                    {}
                )

                score = cortex['score_biologico']
                es_humano = cortex['es_humano']
                clasificacion = cortex['clasificacion']

            except:
                pass

        payload = f"{clasificacion}|{score}|{ts}"

        return {
            'url': url,
            'es_humano': es_humano,
            'score_biologico': round(score, 2),
            'clasificacion': clasificacion,
            'cortex_activo': CORTEX_OK,
            'feromona': {
                'type': 'LBH_FEROMONA',
                'sig_lbh': lbh_sig(payload),
                'ts': ts,
                'timestamp': datetime.now().isoformat()
            }
        }

    except Exception as e:

        return {
            "error": str(e)
        }

if __name__ == '__main__':

    url = sys.argv[1] if len(sys.argv) > 1 else None

    if url:

        resultado = procesar_analisis(url)

        sys.stdout.write(
            json.dumps(resultado) + '\n'
        )

    else:

        sys.stdout.write(
            json.dumps({
                "error": "URL no proporcionada"
            }) + '\n'
        )
