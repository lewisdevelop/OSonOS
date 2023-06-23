from handler import *

vfs = VirtualFileSystem("file_table.json")
vfs.create_file("test", "Arguements!!")
appSelecter = input("Select an app to run:>")
if appSelecter == "terminal":
    terminal("/")