from moviepy.editor import AudioFileClip, ImageClip
import os

from lib.args import args
from lib.write import create_dirs

from tqdm import tqdm

if os.path.isfile(args.output) or os.path.islink(args.output):
    print ('output can\'t be a file or a link')
    exit()
    
create_dirs(args.output)

for directory in tqdm(os.listdir(args.directories), desc='directories', position=1):
    
    path = os.path.join(args.directories, directory)
    if not os.path.isdir(path):
        tqdm.write(f'{path} is not a directory')
        continue
    
    # Save music and image filenames    
    audio_list = [os.path.join(path, file) for file in os.listdir(path) if file.split('.')[-1] == 'mp3']
    image_list = [os.path.join(path, file) for file in os.listdir(path) if file.split('.')[-1] in ['png', 'jpg', 'jpeg']]
    
    if not audio_list or not image_list:
        tqdm.write(f'missing image or music file to create a video in {path}')
        continue
            
    # Load the audio file
    audio = AudioFileClip(audio_list[0])

    # Load the image file
    image = ImageClip(image_list[0])

    # Set the duration of the video to match the audio duration
    duration = audio.duration

    # Create the video clip with the image and audio
    video = image.set_duration(duration).set_audio(audio)

    # Write the video file
    filename = image_list[0].split('.')[0]
    video.write_videofile(f'{filename}.mp4', fps=1)