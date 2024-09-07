YouTube Video Downloader with GUI

This is a simple **YouTube Video Downloader** built using Python and the `yt-dlp` library, with a graphical user interface (GUI) developed using **Tkinter** and **ttkbootstrap**. The application allows users to input a YouTube video URL, select a video quality, and download the video to their local machine, with a progress bar that updates in real-time.

Features
- Fetch available video formats (quality options) from YouTube.
- Select video quality before downloading.
- Real-time progress bar that updates every second during download.
- Clean and intuitive GUI using `ttkbootstrap` for a modern look.
- Easy-to-use and simple installation process.

Technologies Used
- **Python**: Main programming language for the application logic.
- **yt-dlp**: Library for downloading YouTube videos.
- **Tkinter**: Standard Python library for creating the GUI.
- **ttkbootstrap**: Themed widgets to enhance the look of the application.

Screenshots

![Main Window](https://user-images.githubusercontent.com/your-image-url)

Requirements
Make sure you have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).



Python Packages
You can install the required Python packages using `pip`. Open a terminal or command prompt and run the following command:

bash
pip install yt-dlp ttkbootstrap


How to Run:
Clone this repository:

git clone https://github.com/your-username/your-repo-name.git


Navigate to the project directory:


cd your-repo-name
Install the required dependencies:


pip install yt-dlp ttkbootstrap
Run the main.py file:


python main.py




Usage
Enter the YouTube video URL in the input field.
Click the Fetch Available Qualities button to retrieve the list of available video formats.
Select the desired video quality from the dropdown menu.
Click Download Video to start downloading the video.
A progress bar will appear, showing the progress of the download. Once the download is complete, the status will be updated.
Project Structure


.
├── main.py                # Main Python script to run the application
├── README.md              # Project documentation
└── requirements.txt       # Required dependencies for the project
Contribution
Feel free to fork this repository, make changes, and create a pull request! Any contributions to improve the project are welcome.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

javascript
Copy code

Notes:
1. Replace the placeholder URLs such as `https://github.com/your-username/your-repo-name.git` with your actual GitHub repository URL.
2. If you want to include a screenshot, you can take a screenshot of your running application and upload it to GitHub, then link it in the `README.md`.

Adding `requirements.txt`
Create a `requirements.txt` file that lists all the required dependencies:

txt
yt-dlp
ttkbootstrap
You can then reference it in the README as part of the installation instructions.

This README.md file should provide a solid base for your GitHub project, giving users all the information they need to get started. Let me know if you'd like to make any adjustments or add more details!
