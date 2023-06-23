import json
import os
from RestrictedPython import compile_restricted, safe_builtins

# VFS, do not touch
class VirtualFileSystem:
    def __init__(self, filename):
        self.filename = filename
        self.file_table = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.file_table = json.load(f)

    def save_to_disk(self):
        with open(self.filename, 'w') as f:
            json.dump(self.file_table, f)

    def create_file(self, name, content):
        if name in self.file_table:
            print(f"File '{name}' already exists.")
            return
        self.file_table[name] = content
        self.save_to_disk()

    def delete_file(self, name):
        if name not in self.file_table:
            print(f"File '{name}' does not exist.")
            return
        del self.file_table[name]
        self.save_to_disk()

    def run_file(self, name):
        if name not in self.file_table:
            print(f"File '{name}' does not exist.")
            return
        byte_code = compile_restricted(self.file_table[name], '<inline>', 'exec')
        safe_globals = {'__builtins__': safe_builtins}
        exec(byte_code, safe_globals)
        return safe_globals

    def list_files(self):
        return list(self.file_table.keys())

# Applications

def terminal(filepath):
    runningApp = True
    while runningApp:
        terminalPrompt = input(f"{filepath}:>")