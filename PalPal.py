import time
import sys
from playsound import playsound
import threading

# Function to play sound in background
def play_music():
    playsound("Pal Pal Afusic (pagalall.com).mp3")   # make sure file is in same folder

def print_lyrics():
    # Start music in separate thread
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

    lyrics = [
        "Mein ab kyun hosh may aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun torrun khud se jo thay waaday",
        "Ke ab yeh ishq nibhaana nahi?",
        "Mein morrun tum se jo yeh chehra",
        "Dobara nazar milana nahi?",
        "Yeh duniya jaanay mera dard",
        "Tujhe yeh nazar kyun aata nahi?"
    ]

    delays = [0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8, 0.8]

    print("\nPal Pal:\n")
    time.sleep(1.2)

    for line, delay in zip(lyrics, delays):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(delay)

# Run the function
print_lyrics()
