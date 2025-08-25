import argparse
import os
import requests
import subprocess

def create_file(out_filename,in_url):
    r = requests.get(in_url, allow_redirects=True)
    open(out_filename, 'wb').write(r.content)

def materialize_dataset(output_dir, name):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    command = f"{output_dir}/touch test.txt"
    a = subprocess.run(command.split(),capture_output=True,text=True)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Materialize dataset files.')

    # Add arguments
    parser.add_argument('--output_dir', type=str, help='output directory where dataset files will be saved.')
    parser.add_argument('--name', type=str, help='name of the dataset')

    # Parse arguments
    args = parser.parse_args()

    materialize_dataset(args.output_dir, args.name)


if __name__ == "__main__":
    main()
