#!/usr/bin/env python3
"""
Separador de Frames
Script para extraer frames de un video y guardarlos como imágenes.
"""

import cv2
import os
import argparse
import sys
import math


def separar_frames(video_path, output_dir, frame_interval=1):
    """
    Extrae frames de un video y los guarda como imágenes.
    
    Los frames guardados mantienen su número original del video en el nombre
    del archivo (ej: frame_000000.jpg, frame_000010.jpg con intervalo=10).
    
    Args:
        video_path (str): Ruta al archivo de video
        output_dir (str): Directorio donde guardar los frames
        frame_interval (int): Intervalo entre frames a extraer (mínimo 1)
    
    Returns:
        int: Número de frames guardados
    """
    # Verificar que el video existe
    if not os.path.exists(video_path):
        print(f"Error: El archivo de video '{video_path}' no existe.")
        return 0
    
    # Validar intervalo de frames
    if frame_interval < 1:
        print("Error: El intervalo de frames debe ser al menos 1.")
        return 0
    
    # Crear directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directorio creado: {output_dir}")
    
    # Abrir el video
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print(f"Error: No se pudo abrir el video '{video_path}'.")
        return 0
    
    # Obtener información del video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Calcular frames a extraer
    frames_a_extraer = math.ceil(total_frames / frame_interval)
    
    print(f"\nInformación del video:")
    print(f"  - Total de frames: {total_frames}")
    print(f"  - FPS: {fps:.2f}")
    print(f"  - Intervalo de extracción: cada {frame_interval} frame(s)")
    print(f"  - Frames a extraer: {frames_a_extraer}\n")
    
    frame_count = 0
    saved_count = 0
    
    while True:
        # Leer el siguiente frame
        success, frame = video.read()
        
        if not success:
            break
        
        # Guardar frame si corresponde al intervalo
        if frame_count % frame_interval == 0:
            # Nombre del archivo de salida
            output_filename = os.path.join(output_dir, f"frame_{frame_count:06d}.jpg")
            
            # Guardar el frame
            cv2.imwrite(output_filename, frame)
            saved_count += 1
            
            # Mostrar progreso cada 100 frames guardados
            if saved_count % 100 == 0:
                print(f"Frames guardados: {saved_count}")
        
        frame_count += 1
    
    # Liberar recursos
    video.release()
    
    print(f"\n¡Proceso completado!")
    print(f"Total de frames procesados: {frame_count}")
    print(f"Total de frames guardados: {saved_count}")
    print(f"Directorio de salida: {output_dir}")
    
    return saved_count


def main():
    """Función principal con interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Separador de frames de video. Extrae frames de un video y los guarda como imágenes.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Extraer todos los frames (frame a frame)
  python separador_frames.py video.mp4 frames_output
  
  # Extraer cada 10 frames
  python separador_frames.py video.mp4 frames_output -i 10
  
  # Extraer cada 30 frames
  python separador_frames.py video.mp4 frames_output --interval 30
        """
    )
    
    parser.add_argument(
        'video',
        help='Ruta al archivo de video a procesar'
    )
    
    parser.add_argument(
        'output',
        help='Directorio donde guardar los frames extraídos'
    )
    
    parser.add_argument(
        '-i', '--interval',
        type=int,
        default=1,
        help='Intervalo entre frames a extraer (mínimo 1, por defecto: 1 = frame a frame)'
    )
    
    args = parser.parse_args()
    
    # Ejecutar la extracción de frames
    try:
        frames_guardados = separar_frames(args.video, args.output, args.interval)
        
        if frames_guardados == 0:
            sys.exit(1)
        else:
            sys.exit(0)
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
