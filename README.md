# Bad Apple ASCII Console Player

A fun experimental project that brings the iconic *Bad Apple!!* video to life — entirely in your terminal — using ASCII art and synchronized music playback.

##  What It Does

This project reads each frame of the *Bad Apple!!* video, converts it into ASCII characters, and plays the animation in the console while syncing it with the original soundtrack. It's a nostalgic blend of art, tech, and creativity, demonstrating how visuals can be represented using nothing but text.

##  Features

- Converts video frames into ASCII in real-time or preprocessed format
- Synchronized music playback alongside ASCII animation
- Pure console-based experience — no GUI or external video players required
- Optimized for smooth rendering in terminals

## Technologies Used

- **Python** – Core scripting and frame processing
- **OpenCV** – Frame extraction and manipulation
- **PIL (Pillow)** – Image handling and ASCII conversion
- **playsound** – Audio playing
- **Terminal rendering** – Uses ANSI codes or `print()` for frame display

## Why This Project?

After discovering ASCII animations in terminal environments, this project was built purely out of curiosity and love for creative coding. *Bad Apple!!* is a perfect candidate because of its high-contrast visuals and cult status in animation communities.

## How It Works (Simplified)

1. Extract all frames from the video.
2. Resize and convert each frame to grayscale.
3. Map grayscale values to ASCII characters.
4. Display frames in sequence with correct timing.
5. Play the audio track in sync with the animation.

## Requirements

- Python 3.x
- `opencv-python`
- `pillow`
- `playsound`

## Running the Project

```bash
python play.py
