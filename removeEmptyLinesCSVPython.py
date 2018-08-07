#from multiprocessing import pool
import shutil
import csv
import os
from pathlib import Path

def changeExt(path):
    # run before fixing the emtpy rows, so that all files are CSV
    print("Staring Checking the extensions: ", path)
    
    for filename in os.listdir(path):
        if filename.endswith(".csv"): 
            print(filename)
            newPath = os.path.join(path, filename)
        elif filename.endswith(".txt"):
            oldPath = os.path.join(path, filename)
            newName = os.path.splitext(oldPath)[0] + ".csv"
            newPath = os.path.join(path, newName)

            os.rename(oldPath, newPath)
            print("New extension: ", newPath)

        removeEmptyRows(newPath)



def removeEmptyRows(path):
    print("Remove the empty rows of the CSVs")
    print("Current File: ", path)

    folder, name = os.path.split(path)
    outname = os.path.join(folder, name + 'mod')

    inFile = open(path, 'r', newline = '')
    outFile = open(outname, 'w', newline='')

    reader = csv.reader(inFile, delimiter='\t')
    writer  = csv.writer(outFile, delimiter=';')

    for row in reader:
        if row:
            #print(row)
            writer.writerow(row)
        #else:
            #print("Row is empty")

    inFile.close()
    outFile.close()
    shutil.move(outname, path)

    print("Finished: ", path)




if __name__ == '__main__':
    changeExt('C:\localdata\RD5766\SkySpark Development\OptiPro Docs')