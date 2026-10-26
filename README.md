<<<<<<< HEAD
=======
[README.md](https://github.com/user-attachments/files/33973316/README.md)
>>>>>>> feacca7f56329e258a76c53ec01821be1e4483d5
# Pseudo-Reader

Pseudo-Reader is a lightweight Windows desktop application designed for text analysis, code explanation, and prompt execution using the Qwen 3.8 27B language model via the Groq API.

---

## Features

- Modern Desktop Interface: Dark-mode UI built with CustomTkinter for high responsiveness.
- High-Performance Inference: Integrated directly with the Groq API for low-latency responses.
- Advanced Model Support: Powered by qwen/qwen3.8-27b, optimized for reasoning, code generation, and complex tasks.
- Asynchronous Execution: Multithreaded request handling keeps the UI responsive during processing.
- API Key Management: Supports environment variable detection (GROQ_API_KEY) and dynamic key entry in GUI settings.

---

## Prerequisites

- Operating System: Windows 10 or higher (64-bit)
- Python: Version 3.8 or above
- API Access: Active Groq Cloud account and API key

---

## Installation

1. Clone the Repository:
   git clone https://github.com/hunggmd/pseudo-reader.git
   cd pseudo-reader

2. Install Required Dependencies:
   pip install customtkinter groq

---

## Usage Guide

### Running from Source

Execute the script via Python:
python pseudo_reader_x64.py

### Configuring API Key

1. Launch the application and navigate to the Settings tab.
2. Enter your Groq API key (gsk_...).
3. Click Save API Key.
4. Navigate to Analyzation to begin sending prompts.

---

## Build Executable

To generate a standalone distribution using PyInstaller:

1. Install PyInstaller:
   pip install pyinstaller

2. Build the output directory:
   pyinstaller --onedir --noconsole pseudo_reader_x64.py

3. The generated executable will be located in dist/pseudo_reader_x64/pseudo_reader_x64.exe.

---

## Important Notes

- Token Limits: The application sets max_tokens=8192 per request to accommodate long outputs. Requests exceeding model context limits or Groq API rate limits may be truncated by the server.
- Scrollable Interface: The input and output containers support auto-scrolling to ensure long responses and large code files can be reviewed smoothly.

---

## License

<<<<<<< HEAD
Distributed under the MIT License. See `LICENSE` for more information.
=======
Distributed under the MIT License. See `LICENSE` for more information.
>>>>>>> feacca7f56329e258a76c53ec01821be1e4483d5
