# Facial Expression Detector v0.1

Author: Nasrul Muhaimin Mohd Zain

This is a simple web application that uses your webcam to detect faces and provides a placeholder for facial expression analysis (e.g., Happy, Sad, Neutral). It consists of a Python Flask backend for image processing and an HTML/JavaScript frontend for the user interface.

## 1. Prerequisites

Before you begin, make sure you have the following installed on your computer:

* **Python 3.x:** The programming language for our backend.

* **VS Code:** A popular code editor.

* **Git for Windows (Windows only):** If you're on Windows and want to use a Bash terminal in VS Code, install Git for Windows.

### How to Install Prerequisites:

#### **Python 3.x Installation:**

* **Windows:**

  1. Go to the official Python website: <https://www.python.org/downloads/windows/>

  2. Download the latest "Windows installer" (e.g., "Windows installer (64-bit)").

  3. Run the installer. **CRUCIAL STEP:** On the first screen, **check the box that says "Add python.exe to PATH"** before clicking "Install Now". This makes Python accessible from your terminal.

  4. Follow the rest of the installation prompts.

* **macOS (using Homebrew):**

  1. Open your Terminal application.

  2. Install Homebrew (if you don't have it):

     ```
     /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
     
     ```

  3. Install Python 3:

     ```
     brew install python
     
     ```

* **Linux (Debian/Ubuntu):**

  1. Open your Terminal.

  2. Update package list and install Python 3 and pip:

     ```
     sudo apt update
     sudo apt install python3 python3-pip
     
     ```

**Verify Python Installation:**
Open a **new** terminal or command prompt and type:

You should see a version number (e.g., `Python 3.9.7`).

#### **VS Code Installation:**

* Download and install VS Code from the official website: <https://code.visualstudio.com/>

## 2. Project Setup

1. **Create a Project Folder:**
   Create a new empty folder on your computer, for example, `facial_expression_detector`.

2. **Download Haar Cascade Classifier:**

   * Go to: <https://github.com/opencv/opencv/tree/master/data/haarcascades>

   * Click on `haarcascade_frontalface_default.xml`.

   * Click the "Raw" button.

   * Right-click on the raw XML content and choose "Save As..." (or Ctrl+S/Cmd+S).

   * Save this file as `haarcascade_frontalface_default.xml` directly inside your `facial_expression_detector` folder.

3. **Create `app.py`:**
   Inside your `facial_expression_detector` folder, create a file named `app.py` and paste the Python code for the Flask backend into it.

4. **Create `index.html`:**
   Inside the same `facial_expression_detector` folder, create a file named `index.html` and paste the HTML/CSS/JavaScript code for the frontend into it.

Your project folder structure should look like this:

## 3. VS Code Setup

1. **Open Project in VS Code:**

   * Open VS Code.

   * Go to `File` > `Open Folder...` and select your `facial_expression_detector` folder.

2. **Install VS Code Extensions:**

   * Go to the **Extensions** view (Ctrl+Shift+X or Cmd+Shift+X).

   * Search for and install:

     * **Python** (by Microsoft) - Essential for Python development.

3. **Set up VS Code Terminal (Optional, but Recommended):**
   By default, VS Code uses your system's default shell (PowerShell on Windows, Zsh/Bash on macOS/Linux). If you prefer Bash on Windows (after installing Git for Windows):

   * Go to `File` > `Preferences` > `Settings` (or `Code` > `Settings` > `Settings` on macOS).

   * Search for `terminal.integrated.defaultProfile`.

   * From the dropdown, select `Git Bash` (for Windows) or `bash` (for macOS/Linux).

   * Close and reopen your VS Code terminal (Terminal > New Terminal) for changes to take effect.

## 4. Python Environment Setup

It's best practice to use a virtual environment to manage project dependencies.

1. **Open Integrated Terminal:**
   In VS Code, open the Integrated Terminal (Terminal > New Terminal or Ctrl+` / Cmd+` ).

2. **Create Virtual Environment:**
   Type the following command and press Enter:


3. **Activate Virtual Environment:**

* **On Windows:**

  ```
  .\venv\Scripts\activate
  
  ```

* **On macOS/Linux:**

  ```
  source venv/bin/activate
  
  ```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

4. **Install Required Python Libraries:**
With the virtual environment activated, install the necessary libraries:

## 5. Running the Application

1. **Start the Python Flask Backend:**
In your VS Code terminal (with the virtual environment activated), run:

You should see output indicating the Flask app is running, typically on `http://0.0.0.0:5000` or `http://127.0.0.1:5000`.

2. **Open the Web Page:**
Open your web browser (Chrome, Firefox, Edge, etc.) and navigate to:


This will load the `index.html` file served by your Flask backend.

## 6. How to Use

1. **Start Webcam:** On the web page, click the **"Start Webcam"** button. Your browser will ask for permission to access your camera; grant it. You should see your live webcam feed.

2. **Position Face:** Ensure your face is clearly visible in the webcam feed.

3. **Analyze Expression:** Click the **"Analyze Expression"** button. The application will capture a frame and display a detected expression (e.g., "Happy", "Sad", "Neutral") below the buttons.

## 7. Important Notes

* **Backend Analysis:** When running the application locally via `http://localhost:5000`, the Python backend (`app.py`) will perform the actual face detection using OpenCV.

* **Expression Model (Placeholder):** The current Python backend uses a simple placeholder (random expression) for facial expression analysis. For real-world use, you would integrate a more advanced machine learning model (e.g., a deep learning model) to classify emotions from the detected face.

* **Canvas Preview Simulation:** If you are viewing this `index.html` file within a sandboxed environment (like a code editor's live preview or an online canvas), the `Analyze Expression` button will **simulate** the result directly in JavaScript, as direct connections to `localhost` are usually blocked in such environments.
