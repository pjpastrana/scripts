#!/usr/bin/python

import sys
import os

VALID_EXTENSIONS = ["aif", "aiff", "AIF", "AIFF", "wav", "WAV"]

# TODO: expand to convert flac
# ffmpeg -i "$file" -ab 320k -map_metadata 0 -id3v2_version 3 "$file".mp3


#*****************************************************
def main(argv):
    # usage()
    compress_audio_files_in_dir_to_mp3()
#*****************************************************

def usage():
    print "\nNo usage yet\n"

def compress_audio_files_in_dir_to_mp3():
    # get directory where script is executing
    cwd = os.getcwd()
    # list files in cwd
    files = os.listdir(os.getcwd())
    compress_valid_files(cwd, files)

def compress_valid_files(cwd, files):
    for f in files:
        file_path = os.path.join(cwd, f)
        if file_is_valid(file_path):
            compress_file(file_path)

def file_is_valid(file_path):
    is_extension_valid = False
    for ext in VALID_EXTENSIONS:
        if file_path.endswith(ext):
            is_extension_valid = True
            break
    return (not os.path.isdir(file_path) and os.path.isfile(file_path) and is_extension_valid)

def compress_file(file_path):
    print "compressing ", file_path
    file_ext = get_file_extension(file_path)
    file_changed_extension = file_path.replace(file_ext, ".mp3")
    # TODO: os.system is deprecated, replace with subprocess.call
    os.system("ffmpeg -i "+shellquote(file_path)+" -f mp3 -acodec libmp3lame -ab 192000 -ar 44100 "+shellquote(file_changed_extension))

# TODO: dont like duplicating logic
def get_file_extension(file_path):
    file_ext = ""
    for ext in VALID_EXTENSIONS:
        if file_path.endswith(ext):
            file_ext = "."+ext
            break
    return file_ext

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"


#*****************************************************


if __name__ == "__main__":
    main(sys.argv)
