import os
import sys
import argparse


def batch_rename(work_dir, old_ext, new_ext):
    #global newfile

    for filename in os.listdir(work_dir):
        file_ext = os.path.splitext(filename)[1]
        #print(file_ext)

        if old_ext == file_ext:
            name_list = list(filename)
            print(name_list)
            name_list[len(name_list) - len(old_ext):] = list(new_ext)

            newfile = ''.join(name_list)

            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


def get_parser():
        parser = argparse.ArgumentParser(description = 'change extension of files in a working directory')
        parser.add_argument('work_dir', metavar = 'WORK_DIR', type = str, nargs = 1, help='the directory where to change extension')
        parser.add_argument('old_ext', metavar = 'OLD_EXT', type = str, nargs = 1, help = 'old extension')
        parser.add_argument('new_ext', metavar = 'NEW_EXT', type = str, nargs = 1, help = 'new extension')
        return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    new_ext = args['new_ext'][0]

    batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()
