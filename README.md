## README

**YouTube Video Downloader using Tkinter**

This project utilizes the Tkinter library in Python to build a simple but functional application for downloading YouTube videos.

**Features:**

* Download videos from YouTube based on their URL.
* Choose different video quality resolutions.
* Specify a download directory for the downloaded videos.
* Display download progress information.
* Provide feedback messages for success or failure.

**Requirements:**

* Python 3.x
* Tkinter library
* pytube library
* Optional: OpenCV library (for displaying progress bar with video thumbnail)

**Installation:**

1. Clone this repository:
```
git clone https://github.com/bard/youtube_downloader.git
```
2. Install the required libraries:
```
pip install tkinter pytube
pip install opencv-python (Optional)
```

**Usage:**

1. Run the `youtube_downloader.py` file:
```
python youtube_downloader.py
```
2. Enter the URL of the YouTube video you want to download.
3. Choose the desired video quality resolution from the available options.
4. Select the download directory where you want to save the video file.
5. Click the "Download" button.
6. The application will display the download progress and a message upon completion.

**Optional features:**

* If the OpenCV library is installed, the video thumbnail will be displayed alongside the download progress bar.
* You can modify the `youtube_downloader.py` file to customize the application behavior, such as default download directory or available video resolutions.

**Known limitations:**

* This application may not work for all YouTube videos due to changes in the website's structure or restrictions.
* Downloading copyrighted content may be illegal depending on your location and the video content.

**Contributing:**

We welcome contributions to this project. You can fork the repository and submit pull requests with your improvements and suggestions.

**Disclaimer:**

This project is for educational purposes only and does not endorse or encourage the download of copyrighted material. Please use this tool responsibly and respect copyright laws.
