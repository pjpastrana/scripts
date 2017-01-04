#!/usr/bin/python

import sys
import os

class OutputDetails:
    extension = ""
    codec = ""

VALID_INPUT_EXTENSIONS = ["aif", "aiff", "AIF", "AIFF", "wav", "WAV", "flac", "FLAC"]
VALID_OUTPUT_EXTENSIONS = ["mp3", "flac"]
VALID_OUTPUT_CODECS = {
    "mp3": "-acodec libmp3lame -ab 192000 -ar 44100",
    "flac": "-af aformat=s16:44100"
}

#*****************************************************
def main(argv):
    usage()
#*****************************************************

def usage():
    print "\nImplement __main__\n"


def convert_to(format):
    get_output_extension(format)
    convert_valid_files()
    

def get_output_extension(format):
    extension = ""
    try:
        idx = VALID_OUTPUT_EXTENSIONS.index(format)
        output_format = VALID_OUTPUT_EXTENSIONS[idx]
        extension = "."+output_format
        OutputDetails.extension = extension
        OutputDetails.codec = VALID_OUTPUT_CODECS[output_format]
    except ValueError:
        print "ERROR: Unknown output format"
        exit(1)

def convert_valid_files():
    root = os.getcwd()
    for dirpath, dnames, files in os.walk(root):
        print "dirpath ", dirpath
        print "dirnames ", dnames
        print "fnames ", files
        for f in files:
            file_path = os.path.join(dirpath, f)
            (is_extension_valid, file_ext) = file_is_valid(file_path)
            if is_extension_valid:
                convert_file(file_path, file_ext)

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

def convert_file(file_path, file_ext):
    if file_ext == OutputDetails.extension:
        return
    print "Converting ", file_path
    print "Input Extension ", file_ext
    print "Output Extension ", OutputDetails.extension
    print "Output Codec ", OutputDetails.codec
    file_changed_extension = file_path.replace(file_ext, OutputDetails.extension)
    os.system("ffmpeg -i "+shellquote(file_path)+" "+OutputDetails.codec+" "+shellquote(file_changed_extension))

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"


#*****************************************************


if __name__ == "__main__":
    main(sys.argv)
