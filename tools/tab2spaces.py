import os
import sys
from pathlib import Path

spaces = '    '

if __name__ == '__main__':
    args = sys.argv[1:]
    input_folder = args[0]

    files = [e for e in Path(input_folder).iterdir() if e.is_file()]
    # print(files)
    for file_path in files:
        if file_path.suffix.lower() == '.py':
            file_posix_path = file_path.as_posix()
            print(file_posix_path)
            file = open(file_posix_path, 'r')
            content = file.read()
            content = content.replace("\t", spaces)
            file.close()
            file = open(file_posix_path, 'w')
            file.write(content)
            file.close()
