#!/usr/bin/env python3
"""
File:    check_online.py
Author:  Deborah Harrus
# README
## Summary
Script to check if a set of URLs are accessible or not.
## Updates
## Software version # Date
1.0 # 2024-12-04: initial version
"""
import requests
import sys

def check_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            url_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []

    results = []
    for url in url_list:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200 and "Page not found" not in response.text:
                results.append((url, "Accessible", response.status_code))
            else:
                results.append((url, "Content issue", response.status_code))
        except Exception as e:
            results.append((url, "Failed", str(e)))
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_online.py <path_to_text_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    results = check_urls(file_path)
    
    if not results:
        print("No URLs processed.")
    else:
        print("\nResults:")
        for url, status, info in results:
            print(f"{url}: {status} ({info})")
