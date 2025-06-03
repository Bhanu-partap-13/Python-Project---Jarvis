# MEGA PROJECT 1 - Jarvis

## Introduction
Jarvis is a virtual assistant built using Python. It is designed to perform various tasks such as opening websites, playing music, fetching news, and answering general queries using OpenAI's GPT-3.5 model. Jarvis mimics the functionality of popular assistants like Alexa and Google Assistant.

# Demo video
0

## Features
- **Voice Recognition**: Jarvis listens for commands using speech recognition.
- **Web Navigation**: Opens popular websites like Google, Facebook, YouTube, and LinkedIn.
- **Music Playback**: Plays songs from a predefined music library.
- **News Fetching**: Retrieves top headlines from a news API.
- **AI Responses**: Answers general queries using OpenAI's GPT-3.5 model.

## How It Works
1. **Voice Activation**: Jarvis listens for the wake word "Jarvis".
2. **Command Processing**: After activation, Jarvis processes the user's voice command.
3. **Task Execution**: Based on the command, Jarvis performs the requested task (e.g., opening a website, playing music, fetching news).

## Setup Instructions

### Prerequisites
1. Install Python 3.11 or higher.
2. Ensure `pip` is installed and updated:
   ```powershell
   python -m pip install --upgrade pip
   ```

### Install Required Packages
Run the following commands to install the necessary Python libraries:
```powershell
pip install openai SpeechRecognition pyttsx3 requests gtts pygame
```

#### Install PyAudio
If you encounter issues with PyAudio installation, follow these steps:
1. Download the appropriate `.whl` file for your Python version from [PyAudio Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
2. Install the `.whl` file using:
   ```powershell
   pip install <path_to_downloaded_whl_file>
   ```

### Secure OpenAI API Key
Replace the hardcoded OpenAI API key in `clientmegaproject.py` and `mainmegaproject.py` with an environment variable for security:
```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```
Set the environment variable `OPENAI_API_KEY` in your system:
```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

### Run the Project
1. Navigate to the project directory:
   ```powershell
   cd C:\Python\Projects\MEGA PROJECT 1 - Jarvis
   ```
2. Run the main script:
   ```powershell
   python mainmegaproject.py
   ```
3. Test the OpenAI client script:
   ```powershell
   python clientmegaproject.py
   ```

## What It Does
- **Opens Websites**: Jarvis can open Google, Facebook, YouTube, and LinkedIn.
- **Plays Music**: Jarvis plays songs from a predefined library.
- **Fetches News**: Retrieves top headlines from a news API.
- **Answers Queries**: Provides answers to general questions using OpenAI's GPT-3.5 model.

## Future Enhancements
- **Custom Music Library**: Allow users to add their own songs.
- **Dynamic News Categories**: Fetch news based on user preferences.
- **Extended AI Capabilities**: Integrate more advanced AI models for complex tasks.
- **Task Scheduling**: Add functionality to schedule tasks.

## Troubleshooting
### Common Errors
1. **PyAudio Not Found**:
   - Ensure PyAudio is installed correctly.
   - Use precompiled binaries if installation fails.

2. **PermissionError for `temp.mp3`**:
   - Ensure `pygame.mixer.quit()` is called to release the file.

3. **Missing API Key**:
   - Set the `OPENAI_API_KEY` environment variable.

### Debugging
- Use print statements to debug issues.
- Check the logs for error messages.

## Conclusion
Jarvis is a powerful virtual assistant that demonstrates the capabilities of Python in building interactive applications. With further enhancements, it can become even more versatile and user-friendly.
