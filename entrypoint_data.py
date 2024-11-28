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

    R1_url = "https://raw.githubusercontent.com/sorensandgaard/ob_anonymization_dataloss_d1/main/TEST_S1_L001_R1_001.fastq.gz"
    R2_url = "https://raw.githubusercontent.com/sorensandgaard/ob_anonymization_dataloss_d1/main/TEST_S1_L001_R2_001.fastq.gz"

    data_R1_file = os.path.join(output_dir, f'{name}_S1_L001_R1_001.fastq.gz')
    data_R2_file = os.path.join(output_dir, f'{name}_S1_L001_R2_001.fastq.gz')

    create_file(data_R1_file,R1_url)
    create_file(data_R2_file,R2_url)

    # Temporarily: Try to run R-script
    # log_file = os.path.join(output_dir, f'{name}.log.txt')
    # R_script_url = "https://raw.githubusercontent.com/sorensandgaard/ob_anonymization_dataloss_d1/main/testing.R"
    # script_R_file = os.path.join(output_dir, f'testing.R')
    # create_file(script_R_file,R_script_url)
    # R_command = f"Rscript {script_R_file} testing_arguments {name}"
    # a = subprocess.run(R_command.split(),capture_output=True,text=True)

    # content = a.stdout

    # with open(log_file, 'w') as file:
    #    file.write(content)

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
