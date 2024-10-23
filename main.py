from utils import read_video, save_video
import cv2
from trackers import * 

def main():
   
    video_frames = read_video('videoplayback.mp4')
    
    
    t = Tracker("models/best.pt")  
    
    tracks = t.get_object_tracks(video_frames)
    
   
    save_video(video_frames, 'output_videos/output_video.avi')

if __name__ == '__main__':
    main()
