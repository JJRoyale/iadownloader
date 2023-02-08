import argparse
import os
import requests

def download_item(item_id, output_dir, keyword=None, file_type=None, max_files=None, verbose=False):
    # Make a GET request to the API to retrieve information about the item
    response = requests.get(f"https://archive.org/metadata/{item_id}")
    metadata = response.json()

    # Find all files in the item
    files = metadata.get("files", [])

    # Filter files by keyword and file type
    filtered_files = [file for file in files if (not keyword or keyword in file['name']) and (not file_type or file_type in file['format'])]

    # Download each file
    for i, file in enumerate(filtered_files):
        if max_files and i >= max_files:
            break

        file_url = f"https://archive.org/download/{item_id}/{file['name']}"
        response = requests.get(file_url, stream=True)
        filename = file['name']
        if output_dir:
            filename = f"{output_dir}/{filename}"
        with open(filename, "wb") as f:
            content_length = int(response.headers.get("Content-Length", 0))
            downloaded = 0
            for data in response.iter_content(chunk_size=4096):
                downloaded += len(data)
                f.write(data)
                if verbose:
                    percent = 100 * downloaded / content_length
                    print(f"File {filename} downloaded: {percent:.2f}%")
        if verbose:
            print(f"File {filename} downloaded successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download files from the Internet Archive.')
    parser.add_argument('item_id', type=str, help='The ID of the item to download.')
    parser.add_argument('-o', '--output-dir', type=str, help='The directory to save the downloaded files.')
    parser.add_argument('-k', '--keyword', type=str, help='A keyword to search for in file names.')
    parser.add_argument('-t', '--file-type', type=str, help='The type of files to download.')
    parser.add_argument('-m', '--max-files', type=int, help='The maximum number of files to download.')
    parser.add_argument('-l', '--verbose', action='store_true', help='Print the name of each file as it is downloaded.')
    args = parser.parse_args()

    item_id = args.item_id
    output_dir = args.output_dir
    keyword = args.keyword
    file_type = args.file_type
    max_files = args.max_files
    verbose = args.verbose

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    download_item(item_id, output_dir, keyword, file_type, max_files, verbose)
