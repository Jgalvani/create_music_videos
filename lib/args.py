import argparse

# Command line options
parser = argparse.ArgumentParser(prog='change_tone', description='Create multiple tones for the same sound file')
parser.add_argument('-d', '--directories', type=str, help='sound file directory')
args = parser.parse_args()