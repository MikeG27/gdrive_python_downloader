import argparse
import os

from google_drive_downloader import GoogleDriveDownloader as gdd

import config


def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-gdrive_id', type=str, default=config.GDRIVE_ID,
                        help='gdrive id')

    parser.add_argument('-file_name', type=str, default=config.GDRIVE_FILE
                        , help="file name ")

    parser.add_argument('-output', type=str, default=os.getcwd(),
                        help="output directory")

    parser.add_argument('-overwrite', type=bool, default=config.OVERWRITE,
                        help="Do you want overwrite exist file?")

    parser.add_argument('-unzip', type=bool, default=config.UNZIP,
                        help="Do you want unzip exist file?")

    args = parser.parse_args()

    return args


def download_file(file_id, dest_path, unzip=False,overwrite = True):
    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=dest_path,
                                        unzip=unzip, showsize=True, overwrite=overwrite)
    print("/ Data was downloaded ")


if __name__ == "__main__":
    args = parser()

    unzip = args.unzip
    overwrite = args.overwrite

    file_id = args.gdrive_id
    file_name = args.file_name
    dest_path = args.output

    filepath = os.path.join(dest_path, file_name)
    download_file(file_id, filepath,unzip,overwrite)
