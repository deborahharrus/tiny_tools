# File Downloader Script

This Python script can automatically identify and download files of any specified type from HTML pages or local HTML files.

## Features

- ✅ Parse HTML files to find file links of any type
- ✅ Download files from web URLs
- ✅ Resume interrupted downloads
- ✅ Progress bars for downloads
- ✅ Organize downloads into folders
- ✅ Handle both relative and absolute URLs
- ✅ Duplicate link detection
- ✅ Support for any file extension (PDF, PSE, DOCX, XLSX, etc.)

## Installation

1. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Command Line Interface

Download PDFs from a local HTML file:
```bash
python file_downloader.py --file "Biology Resources.html" --file-type pdf
```

Download PSE files from a local HTML file:
```bash
python file_downloader.py --file "Chemistry Resources.html" --file-type pse
```

Download PDFs from a web URL:
```bash
python file_downloader.py --url "https://chemistrylearningresources.weebly.com/biology-resources.html" --file-type pdf
```

Specify a custom download directory:
```bash
python file_downloader.py --file "Biology Resources.html" --file-type pdf --download-dir "my_pdfs"
```

### Method 2: Python Script

```python
from file_downloader import FileDownloader

# Initialize downloader for PDFs
downloader = FileDownloader(download_dir="downloads", file_type="pdf")

# Download PDFs from HTML file
downloader.download_from_html_file("Biology Resources.html")

# Initialize downloader for PSE files
downloader = FileDownloader(download_dir="pse_files", file_type="pse")

# Download PSE files from HTML file
downloader.download_from_html_file("Chemistry Resources.html")

# Download from web URL
downloader.download_from_url("https://chemistrylearningresources.weebly.com/biology-resources.html")
```

### Method 3: Run the Example

```bash
python example_usage.py
```

## Command Line Options

- `--file`: Path to local HTML file
- `--url`: URL of webpage to scrape
- `--file-type`: File extension to download (default: "pdf", examples: "pse", "docx", "xlsx")
- `--download-dir`: Directory to save files (default: "downloads")
- `--no-resume`: Don't resume interrupted downloads

## Example Output

```
Processing HTML file: Biology Resources.html
Found 25 PDF links:
  1. https://chemistrylearningresources.weebly.com/uploads/1/1/1/2/111279665/ta1_-_biochemistry_basics.pdf
  2. https://chemistrylearningresources.weebly.com/uploads/1/1/1/2/111279665/ta2_-_amino_acids.pdf
  ...

Starting download of 25 PDF files...
Files will be saved to: C:\Users\dharrus\Documents\Deborah-EBI-SVN\Biblio\PDBeProject\downloads

[1/25] Downloading: https://chemistrylearningresources.weebly.com/uploads/1/1/1/2/111279665/ta1_-_biochemistry_basics.pdf
ta1_-_biochemistry_basics.pdf: 100%|██████████| 2.5MB/2.5MB [00:05<00:00, 512KB/s]
✓ Downloaded: ta1_-_biochemistry_basics.pdf

Download complete!
✓ Successful: 25
✗ Failed: 0
```

## Supported File Types

The script can download any file type by specifying the `--file-type` argument:

- **PDF files**: `--file-type pdf`
- **PSE files** (PyMOL sessions): `--file-type pse`
- **DOCX files**: `--file-type docx`
- **XLSX files**: `--file-type xlsx`
- **ZIP files**: `--file-type zip`
- **Any other extension**: Just specify the extension without the dot

## Requirements

- Python 3.6+
- requests
- beautifulsoup4
- tqdm
- lxml

## Notes

- The script will create a `downloads` folder (or your specified folder) to store files
- If a file already exists, it will be skipped (unless `--no-resume` is used)
- The script includes a small delay between downloads to be respectful to servers
- Progress bars show download speed and completion percentage 
