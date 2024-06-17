import os
import shutil
import random
import csv
import argparse

# Function to generate new filenames
def generate_new_filename(file_type, index, ext):
    return f"{file_type}_{index:04d}{ext}"

def main(sample_dir, shuffled_dir):
    shuffled_pdfs_dir = os.path.join(shuffled_dir, '_pdfs')
    shuffled_images_dir = os.path.join(shuffled_dir, '_images')

    # Create the shuffled directories if they don't exist
    os.makedirs(shuffled_pdfs_dir, exist_ok=True)
    os.makedirs(shuffled_images_dir, exist_ok=True)

    # Collect all pdf and image files from the individual catalogs
    pdf_files = []
    image_files = []

    for root, dirs, files in os.walk(sample_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
            elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.txt'):
                image_files.append(os.path.join(root, file))

    # Shuffle the lists of files
    random.shuffle(pdf_files)
    random.shuffle(image_files)

    # Prepare a list to keep track of original and new file paths
    file_mappings = []

    # Copy the shuffled files to the new shuffled directories with new names and keep track
    for index, file in enumerate(pdf_files):
        new_filename = generate_new_filename('pdf', index, os.path.splitext(file)[1])
        new_filepath = os.path.join(shuffled_pdfs_dir, new_filename)
        shutil.copy(file, new_filepath)
        file_mappings.append({'original_path': file, 'new_path': new_filepath})

    for index, file in enumerate(image_files):
        new_filename = generate_new_filename('img', index, os.path.splitext(file)[1])
        new_filepath = os.path.join(shuffled_images_dir, new_filename)
        shutil.copy(file, new_filepath)
        file_mappings.append({'original_path': file, 'new_path': new_filepath})

    # Write the file mappings to a CSV file
    csv_path = os.path.join(shuffled_dir, 'file_mapping.csv')
    with open(csv_path, mode='w', newline='') as csv_file:
        fieldnames = ['original_path', 'new_path']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for mapping in file_mappings:
            writer.writerow(mapping)

    print("Files have been shuffled, renamed, and copied to the 'shuffled' folder.")
    print(f"File mapping has been recorded in '{csv_path}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shuffle and rename files from a sample directory.')
    parser.add_argument('sample_dir', type=str, help='The path to the sample directory containing the original files.')
    parser.add_argument('shuffled_dir', type=str, help='The path to the directory where shuffled files will be stored.')

    args = parser.parse_args()
    main(args.sample_dir, args.shuffled_dir)
