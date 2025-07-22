#!/usr/bin/env python3
"""
Example usage of the file downloader script
"""

from file_downloader import FileDownloader

def main():
    # Example 1: Download PDFs from the Biology Resources HTML file
    print("Example 1: Downloading PDFs from Biology Resources HTML file")
    print("=" * 60)
    
    downloader = FileDownloader(download_dir="biology_pdfs", file_type="pdf")
    
    # Process the HTML file
    html_file = "Biology Resources.html"
    downloader.download_from_html_file(html_file)
    
    print("\n" + "=" * 60)
    print("Example 2: Download PSE files from Chemistry Resources HTML file")
    print("=" * 60)
    
    # Example 2: Download PSE files (PyMOL session files)
    downloader = FileDownloader(download_dir="chemistry_pse_files", file_type="pse")
    html_file = "Chemistry Resources.html"
    downloader.download_from_html_file(html_file)
    
    print("\n" + "=" * 60)
    print("Example 3: Download from web URL")
    print("=" * 60)
    
    # Example 3: Download from web URL (uncomment to use)
    # downloader = FileDownloader(download_dir="web_downloads", file_type="pdf")
    # url = "https://chemistrylearningresources.weebly.com/biology-resources.html"
    # downloader.download_from_url(url)

if __name__ == "__main__":
    main() 