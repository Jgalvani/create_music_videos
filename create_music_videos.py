import os
from tqdm import tqdm
from lib.args import args
from moviepy.editor import AudioFileClip, ImageClip, ColorClip, CompositeVideoClip

height = 1080
video_width = 1920

def create_movie(path):
    # Save music and image filenames    
    audio_list = [os.path.join(path, file) for file in os.listdir(path) if file.split('.')[-1].lower() == 'mp3']
    image_list = [os.path.join(path, file) for file in os.listdir(path) if file.split('.')[-1].lower() in ['png', 'jpg', 'jpeg']]
    
    if not audio_list or not image_list:
        tqdm.write(f'missing image or music file to create a video in {path}')
        return
            
    # Load the audio file
    audio = AudioFileClip(audio_list[0])

    # Load the image file
    image = ImageClip(image_list[0])
    original_width, original_height = image.size
    new_width = int(original_width * height / original_height)
    image = image.resize((new_width, height))

    # Create a blank clip with the desired size
    blank_clip = ColorClip((video_width, height), color=(0, 0, 0))

    # Position the image in the center of the blank clip
    x_pos = (video_width - image.w) // 2
    y_pos = (height - image.h) // 2
    image_clip = image.set_position((x_pos, y_pos))

    # Create the video clip by combining the audio, image, and blank clips
    video = CompositeVideoClip([blank_clip, image_clip.set_audio(audio)])
    
    # Set the duration of the video to match the audio duration
    video = video.set_duration(audio.duration)
    
    # Write the video file
    base = os.path.basename(image_list[0].split('.')[0])
    dir = os.path.dirname(image_list[0].split('.')[0])
    filename =os.path.join(dir, base)
    video.write_videofile(f'{filename}.mp4', fps=1)
    
    
if args.unique:
        if not os.path.isdir(args.directories):
            print(f'{args.directories} is not a directory')
            exit()
            
        create_movie(args.directories)
        exit()
        
        
for directory in tqdm(os.listdir(args.directories), desc='directories', position=1):
    
    path = os.path.join(args.directories, directory)
    if not os.path.isdir(path):
        tqdm.write(f'{path} is not a directory')
        continue
    
    create_movie(path)
    
    
