import argparse
import os, sys, shutil, glob

def arguments(argsval):
    parser = argparse.ArgumentParser()
    parser.add_argument('-fol', '--folder', type=str, required=False, help="""Specifies the target folder which node_module remover need to act.""")
    return parser.parse_args(argsval)

def main(def_args=sys.argv[1:]):
    args = arguments(def_args)
    directory = args.folder
    if directory is None:
        directory = './'

    remover(directory)
    print('done 💪')

def remover(directory):
     for directory, dirs, files in os.walk(directory):
        for subdir in dirs:
            print(os.path.join(directory, subdir))
            if subdir == 'node_modules':
                try:
                    print('🤔 removing node_modules, it will take some time. please be patient! ⏳')
                    shutil.rmtree(os.path.join(directory,subdir))
                except Exception as e:
                    print(e)
        

if __name__ == "__main__":
    main()