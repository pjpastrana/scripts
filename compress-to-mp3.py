#!/usr/bin/python

import sys
import os


#*****************************************************
def main(argv):
    # usage()
    compress_audio_files_in_dir_to_mp3()
#*****************************************************

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
            print "there are valid files"
        else:
            print "no valid files to compress"
        
    # print os.path.dirname(os.path.realpath(__file__))
    # print os.getcwd()
    # print os.listdir(os.getcwd())

def file_is_valid(file_path):
    valid_extensions = ["aif", "aiff", "AIF", "AIFF", "wav", "WAV"]
    is_extension_valid = False
    for ext in valid_extensions:
        if file_path.endswith(ext):
            is_extension_valid = True
            break
    return (not os.path.isdir(file_path) and os.path.isfile(file_path) and is_extension_valid)

def usage():
    print "\nNo usage yet\n"

#*****************************************************


if __name__ == "__main__":
    main(sys.argv)