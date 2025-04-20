# copyright i use website neurotorium.org for pictures and videos
import cv2
import time
import threading


def display_video(video_path):
    cap = cv2.VideoCapture(video_path)
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q') or time.time() - start_time > 5:
            break

    cap.release()
    cv2.destroyAllWindows()


print("Hello to this amazing brain adventure game!")
choice1 = input("Wanna play? (yes/no): ").lower()
if choice1 == "yes":
    choice2 = input(
        "Do you want to go deeper or choose specific area you want go deeper/specific_area)?  ").lower()

    if choice2 == "deeper":
        print("You are going deeper into the brain.")
        video_path = r"C:\Users\Hubi\Downloads\Koala_39 (1).mp4"
        display_video(video_path)
    elif choice2 == "specific_area":
        choice3 = input(
            "Which area do you want to explore? (Cerebral cortex, Cerebellum, Brainstem, Medulla oblongata, Pons, Midbrain, Diencephalon, Pituitary gland, Pineal gland, Corpus callosum, Hippocampus, Amygdala, Hippocampal formation, Frontal lobe, Parietal lobe, Temporal lobe, Occipital lobe, Caudate nucleus, Lentiform nucleus, Thalamus, Hypothalamus, Basal ganglia, Insula, Cingulate gyrus, Fornix, Mammillary bodies, Anterior commissure, Posterior commissure, Internal capsule, External capsule, Claustrum, Putamen, Globus pallidus, Subthalamic nucleus, Substantia nigra, Red nucleus, Superior colliculus, Inferior colliculus, Periaqueductal gray, Reticular formation, Olfactory bulb, Olfactory tract.): ").lower()
        if choice3 == "cerebral cortex":
            print("You are going deeper into the brain.")
            video_path = r"C:\Users\Hubi\Downloads\Koala_39 (1).mp4"
            display_video(video_path)
else:
    print("Maybe next time! Have a great day!💙")

print("The game is over. Thanks for playing or not!")
video_path1 = r"C: \Users\Hubi\Videos\Nagrywanie 2025-04-20 131751.mp4"
display_video(video_path1)
