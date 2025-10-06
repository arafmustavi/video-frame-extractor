import cv2
import os

video_dataset_folder = "./video_dataset"
output_directory = "./extracted_frames"

# load all the videos from the video dataset folder
video_clip_list = [f for f in os.listdir(video_dataset_folder)
                   if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
print('Total {} videos found in the folder'.format(len(video_clip_list)))

# create a directory for the extracted frames
os.makedirs(output_directory, exist_ok=True)
print("Output directory ready: {}".format(output_directory))

# extract frames from each video
for current_video in video_clip_list:
    video_path = os.path.join(video_dataset_folder, current_video)
    vidcap = cv2.VideoCapture(video_path)

    if not vidcap.isOpened():
        print(f"Could not open video: {current_video}")
        continue

    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS for {current_video}: {int(fps)}")

    success, image = vidcap.read()
    frame_count = 0
    extracted_name, _ = os.path.splitext(current_video)

    while success:
        # if frame_count % 15 == 0:
        frame_filename = f"{output_directory}/{extracted_name}-frame{frame_count}.jpg"
        cv2.imwrite(frame_filename, image)
        success, image = vidcap.read()
        frame_count += 1

    print(f"{frame_count} frames processed from {current_video}\n")
    vidcap.release()
