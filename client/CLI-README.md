# CURRENTLY IN DEVELOPMENT
...
## OVERVIEW


## PRE-REQUISITES
The following software must be installed within your PC before executing this
program:
- PyCharm IDE
- PySide 6
- Python 3.11
- Git

## INSTALLATION

### Step 1: Clone the Repository (or Download Zip)
If you have not cloned the repository in any of the previous
steps above, you can either clone it using Git or download the 
project as a zip file and then extract it.\
**Option 1: Cloning the Repository**: Open your terminal or 
command prompt and run the following command to clone the repository:
```commandline
git clone [Project URL]
```

**Option 2: Download Zip**: If you prefer not to use Git, you can download
the project as a zip file from the repository's GitHub page and extract
it to a directory of your choice.

### Step 2: Open the Project in Your IDE (PyCharm)
Launch your PyCharm IDE, and select "Open Folder" or "Open Project" 
from the IDE's menu. Navigate to the directory where you cloned or extracted
the project and select it.

### Step 3: Set up the Virtual Environment (venv)
To keep the project dependencies isolated, it's recommended to set up a virtual
environment within your PyCharm IDE. The steps for creating a virtual
environment may vary based on the IDE you are using:

- [How to create a virtual environment in PyCharm] (https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

### Step 4: Install Dependencies (if not using virtual environment)
If you haven't set up a virtual environment, you can install the project dependencies
globally by opening a terminal or command prompt within your PyCharm IDE and running 
the following command:
```commandline
pip install -r client/requirements.txt
```
### Step 5: Configure the Project (Optional)
If the project requires configuration, make any adjustments within your
PyCharm IDE. This could include setting environment variables or updating
configuration files.

### Step 6: Run the Project
Now you are ready to run the **[Program Name]** tool from
your IDE. You can run the main script by right-clicking it in the IDE's
file explorer and selecting "Run" or "Debug".
## PROJECT STRUCTURE

## BUILD
To deploy a build of the current project, ensure that you are running it on 
the targeted system (Windows/MACOS). After that has been accounted for, continue
with the steps below:

Note: Update the version info of the versionfile.txt and the program code in
gui_main respectively.

### Step 1: Install or Update Pyinstaller
```commandline
pip install Pyinstaller
```

### Step 2: Run Pyinstaller on the ".Spec" file found on the root directory
```commandline
Pyinstaller [.Spec File here]
```

### Step 3 (Optional): Run the following command on the root directory

#### Windows:
```commandline

```

### Step 4: Launch the application found on the /dist/VT/ directory

## License
MIT License

Copyright (c) 2023 Alfy Lorenzo, Carlos Montilla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

Emails: lorenzoalfy@gmail.com, carlos.jonikes18@icloud.com
