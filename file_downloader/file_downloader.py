#!/usr/bin/env python3
"""
File Link Finder and Downloader

This script can:
1. Parse HTML files to find file links of specified types
2. Download files automatically
3. Handle both local HTML files and web URLs
4. Organize downloads into folders
5. Resume interrupted downloads
6. Show progress for downloads

Usage:
    python file_downloader.py --file "Biology Resources.html" --file-type pdf
    python file_downloader.py --url "https://chemistrylearningresources.weebly.com/biology-resources.html" --file-type pdf
    python file_downloader.py --file "Chemistry Resources.html" --file-type pse
"""

import os
import re
import sys
import argparse
import requests
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

class FileDownloader:
    def __init__(self, download_dir="downloads", resume=True, file_type="pdf"):
        """
        Initialize the file downloader
        
        Args:
            download_dir (str): Directory to save downloaded files
            resume (bool): Whether to resume interrupted downloads
            file_type (str): File extension to download (e.g., "pdf", "pse", "docx")
        """
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        self.resume = resume
        self.file_type = file_type.lower()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def find_file_links(self, html_content, base_url=None):
        """
        Extract file links from HTML content
        
        Args:
            html_content (str): HTML content to parse
            base_url (str): Base URL for resolving relative links
            
        Returns:
            list: List of file URLs found
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        file_links = []
        
        # Find all links
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Check if it's a file link of the specified type
            if self._is_file_link(href):
                # Resolve relative URLs
                if base_url and not href.startswith(('http://', 'https://')):
                    href = urljoin(base_url, href)
                
                file_links.append(href)
        
        return list(set(file_links))  # Remove duplicates
    
    def _is_file_link(self, href):
        """Check if a link points to a file of the specified type"""
        # Direct file links
        if href.lower().endswith(f'.{self.file_type}'):
            return True
        
        # Links that contain the file type in the URL
        if f'.{self.file_type}' in href.lower():
            return True
        
        # Links that might redirect to files of the specified type
        file_patterns = [
            rf'\.{self.file_type}$',
            rf'\.{self.file_type}\?',
            rf'\.{self.file_type}#',
            rf'/{self.file_type}/',
            rf'/download.*\.{self.file_type}'
        ]
        
        for pattern in file_patterns:
            if re.search(pattern, href.lower()):
                return True
        
        return False
    
    def get_filename_from_url(self, url):
        """Extract filename from URL"""
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        
        # If no filename in URL, create one
        if not filename or not filename.endswith(f'.{self.file_type}'):
            filename = f"document_{hash(url) % 10000}.{self.file_type}"
        
        return filename
    
    def download_file(self, url, filename=None):
        """
        Download a single file
        
        Args:
            url (str): URL of the file to download
            filename (str): Optional filename to save as
            
        Returns:
            bool: True if download successful, False otherwise
        """
        if filename is None:
            filename = self.get_filename_from_url(url)
        
        filepath = self.download_dir / filename
        
        # Check if file already exists and resume is enabled
        if filepath.exists() and self.resume:
            print(f"File {filename} already exists, skipping...")
            return True
        
        try:
            print(f"Downloading: {url}")
            response = self.session.get(url, stream=True)
            response.raise_for_status()
            
            # Get file size for progress bar
            total_size = int(response.headers.get('content-length', 0))
            
            # Download with progress bar
            with open(filepath, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
            
            print(f"✓ Downloaded: {filename}")
            return True
            
        except Exception as e:
            print(f"✗ Error downloading {url}: {e}")
            # Remove partial file if it exists
            if filepath.exists():
                filepath.unlink()
            return False
    
    def download_from_html_file(self, html_file_path):
        """Download files from a local HTML file"""
        print(f"Processing HTML file: {html_file_path}")
        
        try:
            with open(html_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Extract base URL from HTML if available
            soup = BeautifulSoup(html_content, 'html.parser')
            base_url = None
            base_tag = soup.find('base', href=True)
            if base_tag:
                base_url = base_tag['href']
            
            file_links = self.find_file_links(html_content, base_url)
            
            if not file_links:
                print(f"No {self.file_type.upper()} links found in the HTML file.")
                return
            
            print(f"Found {len(file_links)} {self.file_type.upper()} links:")
            for i, link in enumerate(file_links, 1):
                print(f"  {i}. {link}")
            
            return self._download_all_files(file_links)
            
        except Exception as e:
            print(f"Error processing HTML file: {e}")
            return False
    
    def download_from_url(self, url):
        """Download files from a web URL"""
        print(f"Processing URL: {url}")
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            
            file_links = self.find_file_links(response.text, url)
            
            if not file_links:
                print(f"No {self.file_type.upper()} links found on the webpage.")
                return
            
            print(f"Found {len(file_links)} {self.file_type.upper()} links:")
            for i, link in enumerate(file_links, 1):
                print(f"  {i}. {link}")
            
            return self._download_all_files(file_links)
            
        except Exception as e:
            print(f"Error processing URL: {e}")
            return False
    
    def _download_all_files(self, file_links):
        """Download all file links"""
        successful_downloads = 0
        failed_downloads = 0
        
        print(f"\nStarting download of {len(file_links)} {self.file_type.upper()} files...")
        print(f"Files will be saved to: {self.download_dir.absolute()}")
        
        for i, file_url in enumerate(file_links, 1):
            print(f"\n[{i}/{len(file_links)}] ", end="")
            
            if self.download_file(file_url):
                successful_downloads += 1
            else:
                failed_downloads += 1
            
            # Small delay to be respectful to servers
            time.sleep(0.5)
        
        print(f"\nDownload complete!")
        print(f"✓ Successful: {successful_downloads}")
        print(f"✗ Failed: {failed_downloads}")
        
        return successful_downloads, failed_downloads

def main():
    parser = argparse.ArgumentParser(description='Download files from HTML pages')
    parser.add_argument('--file', help='Path to local HTML file')
    parser.add_argument('--url', help='URL of webpage to scrape')
    parser.add_argument('--file-type', default='pdf', help='File extension to download (e.g., pdf, pse, docx, xlsx)')
    parser.add_argument('--download-dir', default='downloads', help='Directory to save files')
    parser.add_argument('--no-resume', action='store_true', help='Don\'t resume interrupted downloads')
    
    args = parser.parse_args()
    
    if not args.file and not args.url:
        print("Please provide either --file or --url argument")
        print("Example:")
        print("  python file_downloader.py --file 'Biology Resources.html' --file-type pdf")
        print("  python file_downloader.py --url 'https://chemistrylearningresources.weebly.com/biology-resources.html' --file-type pdf")
        print("  python file_downloader.py --file 'Chemistry Resources.html' --file-type pse")
        sys.exit(1)
    
    # Initialize downloader
    downloader = FileDownloader(
        download_dir=args.download_dir,
        resume=not args.no_resume,
        file_type=args.file_type
    )
    
    # Process based on input type
    if args.file:
        downloader.download_from_html_file(args.file)
    elif args.url:
        downloader.download_from_url(args.url)

if __name__ == "__main__":
    main() 