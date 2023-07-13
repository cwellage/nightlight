#ref https://microsoft.github.io/IoT-For-Beginners/#/1-getting-started/lessons/1-introduction-to-iot/virtual-device

cd nightlight
#Now run the following to create a virtual environment in the .venv folder
#You need to explicitly call python3 to create the virtual environment just in case you have Python 2 installed in addition to Python 3 (the latest version). If you have Python2 installed then calling python will use Python 2 instead of Python 3
python3 -m venv .venv

#Activate the virtual environment:

#On Windows:

#If you are using the Command Prompt, or the Command Prompt through Windows Terminal, run:

.venv\Scripts\activate.bat
#If you are using PowerShell, run:

.\.venv\Scripts\Activate.ps1

#Once the virtual environment has been activated, the default python command will run the version of Python that was used to create the virtual environment. Run the following to get the version:

python --version
#The output should contain the following:

(.venv) ➜  nightlight python --version
Python 3.9.1

#Run the following commands to install the Pip packages for CounterFit. These packages include the main CounterFit app as well as shims for Grove hardware. These shims allow you to write code as if you were programming using physical sensors and actuators from the Grove ecosystem but connected to virtual IoT devices.

pip install CounterFit
pip install counterfit-connection
pip install counterfit-shims-grove


=============================================================================

#copy haarcascade_frontalface_default.xml file from nightlight\.venv\Lib\site-packages\cv2\data to root folder  


#When VS Code launches, it will activate the Python virtual environment. The selected virtual environment will appear in the bottom status bar:

#VS Code showing the selected virtual environment

#From the VS Code terminal, launch the CounterFit app with the following command:>

counterfit  
#this will by default launch in localhost:5000
#or you can change the port 
counterfit --port 4999