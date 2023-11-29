def get_video_duration(filename):
   with open(filename, 'rb') as f:
       # Пропустить заголовок файла
       f.seek(4)
       # Прочитать и пропустить длину заголовка
       header_length = int.from_bytes(f.read(4), 'big')
       f.seek(header_length)
       # Прочитать и пропустить длину заголовка
       header_length = int.from_bytes(f.read(4), 'big')
       f.seek(header_length)
       # Прочитать и пропустить длину заголовка
       header_length = int.from_bytes(f.read(4), 'big')
       f.seek(header_length)
       # Прочитать и пропустить длину заголовка
       header_length = int.from_bytes(f.read(4), 'big')
       f.seek(header_length)
       # Прочитать и пропустить длину заголовка
       header_length = int.from_bytes(f.read(4), 'big')
       f.seek(header_length)
       # Прочитать продолжительность видео
       duration = int.from_bytes(f.read(4), 'big')
   return duration

print(get_video_duration("file_example_MP4_480_1_5MG.mp4"))