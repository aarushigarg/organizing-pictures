# Organising Pictures

## Description
This repository finds duplicate images in a folder and displays them on a webpage. The user has an option to move duplicate images to a different folder provided.

## Installation

![alt-text](https://github.com/aarushigarg/organizing-pictures/blob/main/OrganizingPicturesVideo.gif)

### Create a virtual environment and activate it.
https://docs.python.org/3/library/venv.html

### Clone the repository.
1. Open command line and go to the directory in which you want the code.

2. Use this command line code.
```bash
git clone https://github.com/aarushigarg/organizing-pictures.git
```

### Install requirements
1. Set your working directory to the repository.

2. Keep the virtual environment activated.

3. Use this command line code.
```bash
pip install -r requirements.txt
```

## Usage
1. Set your working directory to the repository.

2. Keep the virtual environment activated.

3. Find the path of the source folder which contains the images.

4. Find the path of the archive folder which will store the duplicate images.

5. Use this command line code replacing /source-path and /archive-path with the paths of the folders.
```bash
python DuplicateFinder.py --source /source-path --archive /archive-path
```

6. A link will be given for the webpage. Open it in a browser to see all duplicate images. 

7. Press move duplicates button for the images you want to move.