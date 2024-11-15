import argparse
import os
import requests

def create_file(out_filename,in_url):

    r = requests.get(in_url, allow_redirects=True)
    open(out_filename, 'wb').write(r.content)

#    with open(file_name, 'w') as outfile:
#        outfile.write(f'1. Created dataset file {file_name}.\n')
#        outfile.write(f'Testing whether this works')


def materialize_dataset(output_dir, name):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    #R1_url = "https://github.com/sorensandgaard/ob_anonymization_dataloss_d1/blob/main/TEST_S1_L001_R1_001.fastq.gz"
    R1_url = "https://raw.githubusercontent.com/sorensandgaard/ob_anonymization_dataloss_d1/main/TEST_S1_L001_R1_001.fastq.gz"
    R2_url = "https://raw.githubusercontent.com/sorensandgaard/ob_anonymization_dataloss_d1/main/TEST_S1_L001_R2_001.fastq.gz"


#    R1_reads = "TEST_S1_L001_R1_001.fastq.gz"
#    R2_reads = "TEST_S1_L001_R2_001.fastq.gz"

    # Create dataset files
#    data_R1_file = os.path.join(output_dir, R1_reads)
#    data_R2_file = os.path.join(output_dir, R2_reads)

    data_R1_file = os.path.join(output_dir, f'{name}_S1_L001_R1_001.fastq.gz')
    data_R2_file = os.path.join(output_dir, f'{name}_S1_L001_R2_001.fastq.gz')

    create_file(data_R1_file,R1_url)
    create_file(data_R2_file,R2_url)

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
