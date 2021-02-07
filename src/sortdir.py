from argparse import ArgumentParser
from pathlib import Path


def parse_args():
    parser = ArgumentParser(
        description='Sorts the files in a directory based on their extensions'
    )

    parser.add_argument('path',
                        metavar='path',
                        type=Path,
                        help='the path to the directory to sort')

    relative_path = parser.parse_args().path
    abs_path = relative_path.resolve()

    if not Path.exists(abs_path):
        parser.error('path does not exist')

    if not Path.is_dir(abs_path):
        parser.error('path is not a directory')

    return abs_path


def sort_files(src_path: Path):
    file_paths = src_path.glob('*.*')

    for file_path in file_paths:
        if not file_path.is_file():
            continue

        dest_path = src_path / file_path.suffix[1:]

        dest_path.mkdir(exist_ok=True)

        file_path.rename(dest_path / file_path.name)


def main():
    path = parse_args()
    sort_files(path)


if __name__ == '__main__':
    main()
