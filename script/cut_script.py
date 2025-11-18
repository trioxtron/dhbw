import pypdf
import fitz
import os

def cut_pdf(input_file:str, output_file:str):
    """ Cut the PDF file to remove duplicate pages
    Parameters:
        input_file (str): The name of the input file in the 'files' directory
        output_file (str): The name of the output file in the 'results' directory
    Returns:
        int: The number of pages in the input file
        int: The number of pages in the output file
    """
    input_file = 'files/' + input_file + '.pdf'
    output_file = 'results/' + output_file + '.pdf'

    # First we need to find the pages to keep
    reader = pypdf.PdfReader(input_file)

    pages_to_keep = []

    for i in range(len(reader.pages) - 1):
        before = reader.pages[i].extract_text()
        current = reader.pages[i+1]
        if before in current.extract_text():
            continue
        pages_to_keep.append(i)

    pages_to_keep.append(len(reader.pages) - 1)


    # Now we can use PyMuPDF to cut the PDF

    file_handle = fitz.open(input_file)

    file_handle.select(pages_to_keep)

    file_handle.save(output_file)

    return len(reader.pages), len(pages_to_keep)



def concat_pdfs(pdf_files, output_file: str):
    print("📚 Available PDF files:")
    for i, fname in enumerate(pdf_files):
        print(f"{i+1}. {fname}")

    print("\n✏️ Enter the numbers (comma-separated) in the order you want to merge them (e.g. 2,1,3):")
    order = input("Order: ").strip()

    try:
        indices = [int(x) - 1 for x in order.split(",")]
    except ValueError:
        print("❌ Invalid input. Please enter numbers separated by commas.")
        return 0

    selected_files = []
    for idx in indices:
        if 0 <= idx < len(pdf_files):
            selected_files.append(pdf_files[idx])
        else:
            print(f"⚠️ Skipping invalid index: {idx+1}")

    if not selected_files:
        print("❌ No valid files selected.")
        return 0

    writer = pypdf.PdfWriter()

    for file in selected_files:
        path = os.path.join("results", file)
        print(f"📥 Adding {file}")
        reader = pypdf.PdfReader(path + ".pdf")
        for page in reader.pages:
            writer.add_page(page)

    os.makedirs("merged", exist_ok=True)
    output_path = os.path.join("merged", output_file + ".pdf")

    with open(output_path, "wb") as f:
        writer.write(f)

    # Confirm page count with fitz
    doc = fitz.open(output_path)
    total_pages = doc.page_count
    doc.close()

    print(f"\n✅ Merged {len(selected_files)} files into '{output_path}' with {total_pages} pages.")
    return total_pages


if __name__ == '__main__':
    for file in os.listdir('files'):
        continue
        if file[-4:] != '.pdf':
            continue
        print("Reading " + file)
        file = file.split('.')[0]
        full, cut = cut_pdf(file, file + '_cut')
        print("Cut " + str(full) + " -> " + str(cut) + " pages\n")



    pdf_files = [file[:-4] for file in os.listdir("results") if file.endswith(".pdf")]

    print("📚 Files to concatenate:", pdf_files)
    if not pdf_files:
        print("⚠️ No PDF files found in 'files' directory.")
        exit(1)

    accepted = input("Do you want to concatenate these files? (y/n): ").strip().lower()
    if accepted == 'y':
        total_pages = concat_pdfs(pdf_files, "merged_output")
    else:
        print("Concatenation cancelled by user.")
        exit(0)

