# Getting Started
You will find a lot of useful information in the [student Wiki](https://git.rwth-aachen.de/fst-tuda/projects/wiki/stud/-/wikis/home).

## Python and VS Code
### Install git
Install git on your operating system following [these instructions](https://git-scm.com/book/de/v2/Erste-Schritte-Git-installieren)

### Install VS Code
[Install VS Code](https://code.visualstudio.com/) on the operating system of your choice.

After the installation is finished, it is recommended to install the following extensions to assist you when writing code:
* Python
* Pylance
* Jupyter
* Python Docstring Generator (Nils Werner)
* Highlight Trailing Whitespace (Yves Baumes)

Note that there are hundreds of other extensions that can support you in various tasks - it is worth looking for tips and tricks online. We leave this up to you and name only the most basic ones for the start.

### Install anaconda
[Install Anaconda](https://docs.anaconda.com/anaconda/install/). If installing on Windows, open Anaconda prompt after installation and run

```bash
conda init
```
You might need to run this command also from the Windows PowerShell/cmd shell.

To check whether conda has been installed properly, run

```bash
conda --version
```
from the shell of your choice (e.g., cmd). If no errors pop up, you are ready to go!

### Clone this repository wherever you want to have it
Access the folder/directory of your choice and clone (make a local copy) of this repository on your machine by running

:warning: @WIMI: ADJUST THIS LINK
```bash
git clone https://git.rwth-aachen.de/fst-tuda/projects/emergencity/bt-minimalbetrieb.git
```

If the authentication fails, you might need to add the ssh key beforehands - this will be the case if you want to access GitLab from a new machine.


### Create a Conda environment to get the basic required packages
Run

```bash
conda env create -f environment.yml
```
This will create a conda environment with the packages that you need for the start. Activate the environment using

:warning: @WIMI: ADJUST THE NAME OF THE ENVIRONMENT IF NEEDED (e.g. with initials)
```bash
conda activate xy-dev
```
Update the `environment.yml` file when you install new packages.


