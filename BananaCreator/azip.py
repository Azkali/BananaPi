#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import zipfile

def makeZip(path, outPath):
    path = os.path.normpath(path)
    if os.path.isdir(path):
        inName = os.path.join(os.path.basename(path) + '.zip')
        print("\n\nFilename: " + inName)
        print("\ninPath: " + path)
        print('\noutPath: ' + outPath)

        def zipDir(path, ziph):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if not file.endswith('.lock'):
                        filePath = path + '/' + file
                        print(file + ' ' + convert_size(os.path.getsize(filePath)))
                        os.chdir(outPath)
                        ziph.write(os.path.join(root, file),
                                   os.path.join(os.path.basename(path), os.path.join(root, file)[len(path)+len(os.sep):]))

        if os.path.isdir(outPath) and not os.path.isfile(outPath + '/' + inName):
            print("\nI'm making a zip")
            with zipfile.ZipFile(outPath + inName, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipDir(path, zipf)
            zipf.close()
            print('Done !')

        elif os.path.isfile(outPath + '/' + inName):
            print('File: ' + inName + ' already exists in: ' + '\'' + outPath + '\'' + ' !')
            testZip(inName, path, outPath)
            
    elif os.path.isfile(path):
        inName = './' + path + '.zip'
        zipfile.ZipFile(inName, mode='w').write(path)

def testZip(archiveName, path, outPath):
    archiveName = outPath + archiveName
    with zipfile.ZipFile(archiveName, 'r') as zipf:
        import datetime
        import time
        zipfile.is_zipfile(archiveName)
        zipf.testzip()
        for info in zipf.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) +
                  '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')
            for root, dirs, files in os.walk(path):
                for file in files:
                    #print(datetime.datetime(*info.date_time))
                    #print(time.ctime(os.path.getmtime(*file)))

                    t = datetime.datetime.strptime(time.ctime(
                        os.path.getmtime(file)), '%a %b %d %H:%M:%S %Y').timestamp()
                    d = datetime.datetime(*info.date_time).timestamp()

                    print(t)
                    print(d)
                    
                    if t == datetime.datetime(*info.date_time).timestamp():
                        print("hi: " + info.filename +
                              " is already up-to-date! ")
                    else:
                        print('it should write again')
                        pass

        print("\n\nTest: ")
        print(zipf.testzip())
        print("\nisZip: ")
        print(zipfile.is_zipfile(archiveName))
    zipf.close()

# Size convert Byte to B, KB, MB, GB ...
def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "{} {}".format(s, size_name[i])

if __name__ == "__main__":
    import sys
    print(sys.argv[1], sys.argv[2])
    makeZip(sys.argv[1], sys.argv[2])
    print('You should consider using the GUI :) !')