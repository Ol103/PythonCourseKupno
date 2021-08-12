import sys
import os
import hashlib
import ast
import argparse
import time



class Shuffler:  

    def __init__(self):
        self.map = {}

    def rename(self, dir_name, output):
        mp3s = []

        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-4:] == '.mp3':
                    mp3s.append([root, file]) 

        for path, mp3 in mp3s:
            has_hname = self.generateName() + '.mp3' '.mp3'
            self.map[has_hname] = mp3
            os.rename(path + '/' + mp3), path + '/' + has_hname
        f = open(output, 'a')
        f.write(str(self.map))

    def restore(self, dir_name, restore_path):
        with open(file_name, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []

        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-4:] == '.mp3':
                    mp3s.append({root, file})

        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
            os.remove(restore_path)

    def generate_name(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='sub_command', help='sub_command help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dir_name')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dir_name, 'restore.info')
        else:
            shuffler.rename(args.dir_name, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dir_name, args.restore_map)
    else:
        sys.exit()


main()
