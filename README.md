EnviroScope
By Andrew Appleman and Priya Riegle
Maine-Endwell Middle School

Install Python 3.10: This is the primary programming language that will be used
https://www.python.org/downloads/release/python-3100/
Later versions of Python are not compatible with Kivy
Optionally, install VS Code or your other favorite code editor
https://code.visualstudio.com/download
Switch to the path you want all the files in
Create python virtual environment
Open windows command prompt or terminal in VS Code
Update Python tools by typing:
python -m pip install --upgrade pip setuptools virtualenv
In Command Prompt, navigate to where the file is through your directories
Create a virtual environment, which will let you run Kivy. In the example below, “kivy_venv” is the name of the environment created which is also the name of the directory created
python -m venv kivy_venv
kivy_venv\Scripts\activate
You need to run this activation script to start the environment every time you open a new command prompt
Install Kivy: This is a Python framework that allows for graphics generation for the app frontend
https://kivy.org/doc/stable/gettingstarted/installation.html
Instructions are in the link but the major steps are below:
Install Kivy from examples codes:
python -m pip install "kivy[base]" kivy_examples
Install python package for android notifications
python -m pip install kivy plyer pymongo pillow pafy win10toast httpx pandas
Enter “git clone https://github.com/andrewtappleman/EnviroScope”
Make sure you already activated the virtual environment(the green highlighted common above)
python EnviroScope.py
Reach out with any questions: andrewtappleman@gmail.com
