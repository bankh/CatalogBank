import os
import random
import shutil
import csv
import sys

def main(sample_folder, target_folder, num_pdfs):
    # Ensure the target directory exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Create the _pdfs and _images directories in the target folder
    target_pdf_dir = os.path.join(target_folder, "_pdfs")
    target_image_dir = os.path.join(target_folder, "_images")

    if not os.path.exists(target_pdf_dir):
        os.makedirs(target_pdf_dir)

    if not os.path.exists(target_image_dir):
        os.makedirs(target_image_dir)

    # Initialize the global counter for file enumeration
    global_counter = 1
    total_pdfs_picked = 0  # Track the total number of PDFs processed

    # Create a CSV file for tracking
    csv_file = os.path.join(target_folder, "filename_mapping.csv")
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Source Filename", "Target Filename"])

    # Loop through each catalog in the source folder
    for catalog in os.listdir(sample_folder):
        catalog_path = os.path.join(sample_folder, catalog)
        pdf_folder = os.path.join(catalog_path, "_pdfs")
        image_folder = os.path.join(catalog_path, "_images")

        if not os.path.exists(pdf_folder) or not os.path.exists(image_folder):
            continue  # Skip if the folder structure is incorrect

        # Collect all PDFs in the catalog
        pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

        if not pdf_files:
            continue  # Skip if no PDFs are found

        # Calculate how many PDFs can still be processed
        remaining_pdfs = num_pdfs - total_pdfs_picked
        if remaining_pdfs <= 0:
            break  # Stop if we've already picked the desired number of PDFs

        # Randomly select the appropriate number of PDFs from this catalog
        selected_pdfs = random.sample(pdf_files, min(remaining_pdfs, len(pdf_files)))

        for selected_pdf in selected_pdfs:
            selected_pdf_base = os.path.basename(selected_pdf).replace(".pdf", "")

            # Copy and rename the selected PDF
            pdf_target_name = f"pdf_{global_counter:06}.pdf"
            shutil.copy2(selected_pdf, os.path.join(target_pdf_dir, pdf_target_name))

            # Log the PDF filename change
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([selected_pdf, os.path.join(target_pdf_dir, pdf_target_name)])

            # Find associated images and text files in the _images folder
            associated_files = []
            for file in os.listdir(image_folder):
                if selected_pdf_base in file:
                    associated_files.append(os.path.join(image_folder, file))

            # Copy and rename associated images and text files
            for file in associated_files:
                file_extension = os.path.splitext(file)[1]
                base_name = os.path.basename(file)

                if "_ann" in base_name:
                    new_filename = f"img_{global_counter:06}_ann{file_extension}"
                elif "_ori" in base_name:
                    new_filename = f"img_{global_counter:06}_ori{file_extension}"
                else:
                    new_filename = f"txt_{global_counter:06}{file_extension}"

                shutil.copy2(file, os.path.join(target_image_dir, new_filename))

                # Log the filename change
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([file, os.path.join(target_image_dir, new_filename)])

            # Increment the counters
            global_counter += 1
            total_pdfs_picked += 1

            if total_pdfs_picked >= num_pdfs:
                break  # Stop if we've reached the desired number of PDFs

    print(f"{total_pdfs_picked} PDFs have been processed and copied from the catalogs.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py ./sample_folder ./target_folder number_of_pdfs_to_pick")
    else:
        sample_folder = sys.argv[1]
        target_folder = sys.argv[2]
        num_pdfs = int(sys.argv[3])
        main(sample_folder, target_folder, num_pdfs)
