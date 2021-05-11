import time
import sys
import logging
from playsound import playsound
import os
import cv2
from PIL import Image

frame_interval = 1.0 / 25
ASCII_CHARS = ["%","p", "#", "?", "s", "+", ";", ":", "*", ",", " "][::-1]
frame_size=100
os.system('cls' if os.name == 'nt' else 'clear')
# Checking if frames are avaialble , if not the create  
def Cap_frame():
    if not os.path.exists('ExtractedFrames'):
        os.makedirs('ExtractedFrames')
    chk_frames=0

    for i in range(0,6571):
        file_path=r'ExtractedFrames'+'/'+'s'+str(i)+'.jpeg'
        if os.path.isfile(file_path):
            chk_frames+=1
    if chk_frames > 6000:
        sys.stdout.write('Frames are avaialbe , countinuing..')
    else:
        sys.stdout.write('\nFrames are missing , creating frames..')
        vid=cv2.VideoCapture('BadApple.mp4')
        i=0
        print('\nStarted capturing Frames')
        for i in range (0,6571):
            nm='ExtractedFrames'+'\\'+'s'+str(i)+'.jpeg'
            ret,frame=vid.read()
            cv2.imwrite(nm,frame)
        vid.release()
        print('\nDone capturing Frames')
        return

def pic_to_ascii():
    if not os.path.exists('TextFiles'):
        os.makedirs('TextFiles')
    chk_files=0
    for i in range(0,6571):
        file_path=r'TextFiles'+'/'+'read'+str(i)+'.txt'
        if os.path.isfile(file_path):
            chk_files+=1
    if chk_files > 6000:
        sys.stdout.write('\nFiles are avaialbe , countinuing..')
    else:
        sys.stdout.write('\nFiles are missing , creating files..')
        for i in range(0,6571):

            def resize_image(image_frame):
                width, height = image_frame.size
                aspect_ratio = (height / float(width * 2.5))
                new_height = int(aspect_ratio * frame_size)
                resized_image = image_frame.resize((frame_size, new_height))
                return resized_image

            # Greyscale
            def greyscale(image_frame):
                return image_frame.convert("L")

            def main():
            # attempt to open image from user-input
                path='ExtractedFrames\\s'+str(i)+'.jpeg'
                image = Image.open(path)
                return image
                
            # Convert pixels to ascii
            def pixels_to_ascii(image):
                pixels = image.getdata()
                characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
                return characters


            # Open image => Resize => Greyscale => Convert => Print
            def ascii_generator(image_frame):
                resized_image = resize_image(image_frame)  # resize the image
                greyscale_image = greyscale(resized_image)  # convert to greyscale
                ascii_characters = pixels_to_ascii(greyscale_image)  # get ascii characters
                pixel_count = len(ascii_characters)
                ascii_image = "\n".join([ascii_characters[index:(index + frame_size)] for index in range(0, pixel_count, 100)])
                return ascii_image

            image=main()
            img=ascii_generator(image)
            file = open('TextFiles'+'\\'+'read'+str(i)+'.txt', 'w')
            file.write(img)
            file.close()
        sys.stdout.write('\nFiles are avaiable , countinuing..')
        return
# play bad-apple-audio.mp3 
def play_audio():
    playsound("bad-apple-audio.mp3", block=False)

#play ascii video
def play_video():
    for frame_number in range(0, 6571):
        start_time = time.time()
        file_name = r"TextFiles/" + "read" + str(frame_number) + ".txt"
        with open(file_name, 'r') as f:
            sys.stdout.write("\r" + f.read())
        compute_delay = float(time.time() - start_time)
        delay_duration = frame_interval - compute_delay
        logging.info(str(delay_duration))
        if delay_duration < 0:
            delay_duration = 0
        time.sleep(delay_duration)

# Delete extracted frames and .txt files
def delete_assets():
    for index in range(0, 6572):
        frame_name = "ExtractedFrames/" + "s" + str(index) + ".jpeg"
        try:
            os.remove(frame_name)
        except:
           continue
            

    for index in range(0, 6572):
        file_name = "TextFiles/" + "read" + str(index) + ".txt"
        try:
            os.remove(file_name)
        except:
            continue
    sys.stdout.write("Done Deleting")

# Main Function
def main():
    logging.basicConfig(filename='compute_delay.log', level=logging.INFO)
    print('1.Play')
    print('2.Delete Assests')
    print('3.Quit')
    c=int(input('Your Choice: '))
    if c==1:
        
        Cap_frame()
        pic_to_ascii()
        play_audio()
        #os.system('cls' if os.name == 'nt' else 'clear') # clearing terminal  before playing video
        play_video()
    elif c==2:
        delete_assets()
    elif c==3:
        return
    else:
        print('Unknown Choice!')

# Calling main function
main()


