
import audio_metadata
import pathlib
import os
import sys

path = sys.argv[1]


total_duration = 0
item_formats = ["mp3", "flac", "dsf"]

music_files = []
for entry in os.walk(path):
    path = entry[0]
    files = entry[2]
    for file in files:
        try:
            file_extension = file.split(".")[1]
            if file_extension in item_formats:
                file_path = pathlib.Path(path + "/" + file)
                music_files.append(file_path)
        except IndexError:
            continue


def album_length(music_collection):
    duration = 0
    for item in music_collection:
        try:
            metadata = audio_metadata.load(item)
            duration += metadata.streaminfo['duration']
        except:
            print("exception of file", item)
            continue
    return duration


print(album_length(music_files))
