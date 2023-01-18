# Organising Pictures

## Installation

### Create a virtual environment and activate it.
https://docs.python.org/3/library/venv.html

### Clone the repository.
Open command line and go to the directory in which you want the code.

Use this command line code.
```bash
git clone https://github.com/aarushigarg/organizing-pictures.git
```

### Install requirements
Set your working directory to the repository.

Keep the virtual environment activated.

Use this command line code.
```bash
pip install -r requirements.txt
```

## Usage
Set your working directory to the repository.

Keep the virtual environment activated.

Find the path of the source folder which contains the images.

Find the path of the archive folder which will store the duplicate images.

Use this command line code replacing /source-path and /archive-path with the paths of the folders.
```bash
python DuplicateFinder.py --source /source-path --archive /archive-path
```