import argparse

# Command line options
parser = argparse.ArgumentParser(prog='create_music_video', description='Create a video in a directory including a song file and an image file')
parser.add_argument('-d', '--directories', type=str, help='sound file directory')
args = parser.parse_args()
