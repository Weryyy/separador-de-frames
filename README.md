# Separador de Frames

Código para separar frames en un video, se puede elegir cada cuántos frames se hace el corte siendo el mínimo frame a frame y convertirlos en fotos esos frames y guardarlos.

## Descripción

Este script permite extraer frames de un video y guardarlos como imágenes individuales. Puedes configurar el intervalo de extracción, desde extraer todos los frames (frame a frame) hasta extraer uno cada N frames.

## Requisitos

- Python 3.6 o superior
- OpenCV (opencv-python)

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/Weryyy/separador-de-frames.git
cd separador-de-frames
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Sintaxis básica

```bash
python separador_frames.py [video] [directorio_salida] [opciones]
```

### Parámetros

- `video`: Ruta al archivo de video a procesar
- `directorio_salida`: Directorio donde se guardarán los frames extraídos
- `-i, --interval`: (Opcional) Intervalo entre frames a extraer. Por defecto: 1 (frame a frame)

### Ejemplos

1. **Extraer todos los frames (frame a frame)**:
```bash
python separador_frames.py video.mp4 frames_output
```

2. **Extraer cada 10 frames**:
```bash
python separador_frames.py video.mp4 frames_output -i 10
```

3. **Extraer cada 30 frames**:
```bash
python separador_frames.py video.mp4 frames_output --interval 30
```

4. **Extraer cada 60 frames (aproximadamente 1 por segundo en video de 60 FPS)**:
```bash
python separador_frames.py video.mp4 frames_output --interval 60
```

## Características

- ✅ Extracción de frames con intervalo configurable (mínimo 1)
- ✅ Los frames se guardan como archivos JPG
- ✅ Nombres de archivo secuenciales (frame_000000.jpg, frame_000001.jpg, etc.)
- ✅ Muestra información del video (total de frames, FPS)
- ✅ Muestra progreso durante la extracción
- ✅ Crea el directorio de salida automáticamente si no existe
- ✅ Validación de errores (archivo no existe, formato inválido, etc.)

## Formatos de Video Soportados

El script soporta todos los formatos de video que OpenCV puede leer, incluyendo:
- MP4
- AVI
- MOV
- MKV
- FLV
- WMV
- Y muchos más

## Salida

Los frames se guardan con el formato:
```
frame_000000.jpg
frame_000010.jpg
frame_000020.jpg
...
```

El número en el nombre del archivo corresponde al número del frame en el video original.

## Ayuda

Para ver la ayuda completa:
```bash
python separador_frames.py --help
```

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
