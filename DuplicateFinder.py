from flask import Flask, render_template, make_response, request, redirect
import os
import hashlib
import click
import pathlib

app = Flask(__name__)

source_path = ""
archive_path = ""

@click.command()
@click.option ("--source", help="path of the source folder")
@click.option ("--archive", help="path of the archive folder")
def start_server (source, archive):
    global source_path, archive_path
    source_path = source
    archive_path = archive
    app.run(debug=True)

@app.route ("/")
def find_duplicates ():
    #files is a dictionary with the file size as the key and a list of names of files as the value
    files = {}
    folder = os.listdir (source_path)
    #populates the dictionary
    for file_name in folder:
        file_path = source_path + "/" + file_name
        file_size = os.stat (file_path).st_size
        
        l = files.get(file_size, [])
        l.append(file_path)
        files[file_size] = l

    #hash_dict is a dictionary with the hash as the key and a list of file names with that hash as the value
    hash_dict = {}
    #creates hash for files with same size
    for size in files:
        file_list = files[size]
        if len (file_list) > 1:
            for file_path in file_list:
                with open (file_path, "rb") as f:
                    file_content = f.read()
                    hash = hashlib.sha224(file_content).hexdigest()
                    l = hash_dict.get(hash, [])
                    l.append(file_path)
                    hash_dict[hash] = l

    duplicate_file_names = []
    for h in hash_dict:
        duplicate_file_names.append (hash_dict[h])
    
    return render_template ("find_duplicates.html", duplicate_file_names=duplicate_file_names, source_path=source_path)

@app.route("/image_file")
def image_file():
    filename = request.args.get('filename', '')
    with open(filename, 'rb') as f:
        data = f.read()

    response = make_response(data)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'attachment', filename=filename)

    return response

@app.route("/move_duplicates", methods=["POST"])
def move_duplicates():
    duplicate_filepaths = request.form.getlist('filename')

    #saves one image
    saved = ""
    for filepath in duplicate_filepaths:
        if not "copy" in filepath:
            saved = filepath
            break
    if saved == "":
        saved = duplicate_filepaths[0]

    #moves the duplicates to the archive folder
    for filepath in duplicate_filepaths:
        if filepath != saved:
            path = pathlib.PurePath(filepath)
            print(path.name)
            os.rename(source_path + "/" + path.name, archive_path + "/" + path.name)

    return redirect("/")

if __name__ == '__main__':
    start_server()