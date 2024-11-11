import argparse
import os


def create_file(file_name):
    with open(file_name, 'w') as outfile:
        outfile.write(f'1. Created dataset file {file_name}.\n')
	outfile.write(f'Testing whether this works')


def materialize_dataset(output_dir, name):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create dataset files
    data_counts_file = os.path.join(output_dir, f'{name}.txt.gz')
    data_meta_file = os.path.join(output_dir, f'{name}.meta.json')
    data_specific_params_file = os.path.join(output_dir, f'{name}_params.txt')

    create_file(data_counts_file)
    create_file(data_meta_file)
    create_file(data_specific_params_file)


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
