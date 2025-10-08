#!/usr/bin/env python3
"""
CSV Column Filter and Processor

A Python script to filter specific columns from CSV files with additional processing options.
Supports column selection, duplicate removal, and sorting capabilities.

Author: Deborah Harrus
Version: 1.0
"""

import csv
import argparse
import logging
import sys
from tqdm import tqdm

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def filter_csv(input_file, output_file, column_indexes, remove_duplicates, sort_output):
    """
    Filter specific columns from a CSV file with optional processing.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to save the filtered CSV file
        column_indexes (str): Comma-separated list of column indexes to keep
        remove_duplicates (bool): Whether to remove duplicate rows
        sort_output (bool): Whether to sort the output by the first column
    """
    try:
        column_indexes = [int(i) for i in column_indexes.split(',')]
        
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            rows = [row for row in reader]
            total_rows = len(rows)
            
            if not rows:
                logging.error("Input CSV file is empty.")
                sys.exit(1)
            
            header = rows[0]  # Preserve the header
            data_rows = rows[1:]  # Exclude the header for processing
            
            filtered_rows = [header]  # Keep header at the top
            with tqdm(total=total_rows - 1, desc="Processing", unit="row") as pbar:
                for idx, row in enumerate(data_rows):
                    filtered_row = [row[i] for i in column_indexes if i < len(row)]
                    filtered_rows.append(filtered_row)
                    pbar.update(1)
            
            # Remove duplicates if requested
            if remove_duplicates:
                unique_rows = list(map(list, set(map(tuple, filtered_rows[1:]))))
                filtered_rows = [header] + unique_rows
                logging.info("Duplicates removed from the output file.")
            
            # Sort the output if requested
            if sort_output:
                filtered_rows = [header] + sorted(filtered_rows[1:], key=lambda x: x[0] if x else "")
                logging.info("Output file sorted based on the first column.")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(filtered_rows)
        
        logging.info(f"Filtered CSV saved as {output_file}")
    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Filter specific columns from a CSV file.")
    parser.add_argument("--input_file", required=True, help="Path to the input CSV file")
    parser.add_argument("--output_file", required=True, help="Path to save the filtered CSV file")
    parser.add_argument("--column_indexes", required=True, help="Comma-separated list of column indexes to keep (zero-based index)")
    parser.add_argument("--remove_duplicates", action="store_true", help="Remove duplicate rows from the output file")
    parser.add_argument("--sort_output", action="store_true", help="Sort the output file based on the first column in the --column_indexes")
    
    args = parser.parse_args()
    filter_csv(args.input_file, args.output_file, args.column_indexes, args.remove_duplicates, args.sort_output)