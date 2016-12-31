#!/usr/bin/python

import sys
import os

VALID_INPUT_EXTENSIONS = ["aif", "aiff", "AIF", "AIFF", "wav", "WAV", "flac", "FLAC"]
VALID_OUTPUT_EXTENSIONS = ["MP3", "mp3"]

#*****************************************************
def main(argv):
    usage()
#*****************************************************

def usage():
    print "\nImplement __main__\n"


def convert_to(format):
    (cwd, files) = list_directory_content()
    output_extension = get_output_extension(format)
    convert_valid_files(cwd, files, output_extension)
    

def get_output_extension(format):
    output_format = ""
    try:
        idx = VALID_OUTPUT_EXTENSIONS.index(format)
        output_format = "."+VALID_OUTPUT_EXTENSIONS[idx]
    except ValueError:
        print "ERROR: Unknown output format"
        exit(1)
    return output_format

def list_directory_content():
    # get directory where script is executing
    cwd = os.getcwd()
    # list files in cwd
    files = os.listdir(os.getcwd())
    return(cwd, files)

def convert_valid_files(cwd, files, output_extension):
    for f in files:
        file_path = os.path.join(cwd, f)
        (is_extension_valid, file_ext) = file_is_valid(file_path)
        if is_extension_valid:
            convert_file(file_path, file_ext, output_extension)

def file_is_valid(file_path):
    is_extension_valid = False
    file_ext = ""
    for ext in VALID_INPUT_EXTENSIONS:
        if file_path.endswith(ext):
            is_extension_valid = True
            file_ext = "."+ext
            break
    valid = (not os.path.isdir(file_path) and os.path.isfile(file_path) and is_extension_valid)
    return (valid, file_ext)

# TODO: Extend to other output formats and their codec dependency
# converting only to mp3 for now.
def convert_file(file_path, file_ext, output_extension):
    print "converting ", file_path
    file_changed_extension = file_path.replace(file_ext, output_extension)
    os.system("ffmpeg -i "+shellquote(file_path)+" -acodec libmp3lame -ab 192000 -ar 44100 "+shellquote(file_changed_extension))

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"


#*****************************************************


if __name__ == "__main__":
    main(sys.argv)
