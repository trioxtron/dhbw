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


if __name__ == '__main__':
    for file in os.listdir('files'):
        if file[-4:] != '.pdf':
            continue
        print("Reading " + file)
        file = file.split('.')[0]
        full, cut = cut_pdf(file, file + '_cut')
        print("Cut " + str(full) + " -> " + str(cut) + " pages\n")
