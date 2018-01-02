#! python3
#Program to change tab characters in text file to 4-spaces instead.
import os, sys, argparse, fileinput

def checkPaths(filePaths):
    corrPaths = []
    for path in filePaths:
        if(not os.path.isfile(path)):
            print(path + " is not a valid path, please enter the valid path next time.")
        else:
            corrPaths += [path]
    return corrPaths

def parser():
    parser = argparse.ArgumentParser(description='Converts Hard Tabs into Four Spaces for Text Documents')
    parser.add_argument('-fps', '--filePaths', nargs = '+', help='Enter one or more filepaths.', required = True)
    return parser.parse_args()

def tabs2Spaces(filePaths):
    for pat in filePaths:
        os.chdir(os.path.dirname(pat))
        with open(pat, 'r') as fin: 
            with open(os.path.splitext(pat)[0] + "- Edited.txt", 'w+') as fout:
                print(os.path.splitext(pat)[0] + "- Edited.txt is being added... )
                for line in fin:
                    fout.write(line.replace('\t', '    '))
    

def main():
    args = parser()
    filePaths = args.filePaths
    pathsExist = checkPaths(filePaths)
    tabs2Spaces(pathsExist)
                
    

if __name__ == "__main__":
    main()
