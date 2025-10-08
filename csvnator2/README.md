# CSV Column Filter and Processor

A powerful Python script for filtering specific columns from CSV files with advanced processing options. Perfect for data cleaning, column extraction, and CSV manipulation tasks.

## Features

- **Column Selection**: Extract specific columns by index from CSV files
- **Duplicate Removal**: Remove duplicate rows from the output
- **Sorting**: Sort output by the first selected column
- **Progress Tracking**: Visual progress bar for large files
- **Error Handling**: Robust error handling and logging
- **Flexible Input**: Support for various CSV formats and encodings

## Use Cases

- **Data Analysis**: Extract relevant columns for analysis
- **Data Cleaning**: Remove duplicates and organize data
- **Report Generation**: Create filtered datasets for reports
- **Data Migration**: Transform CSV structure for different systems
- **Data Validation**: Process and clean data before analysis

## Requirements

- Python 3.x
- tqdm (for progress bars)

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python csvnator2.py --input_file data.csv --output_file filtered_data.csv --column_indexes 0,1,3
```

### Advanced Usage

```bash
# Filter columns, remove duplicates, and sort
python csvnator2.py --input_file data.csv --output_file clean_data.csv --column_indexes 0,1,3,7 --remove_duplicates --sort_output
```

### Command Line Options

- `--input_file`: Path to the input CSV file (required)
- `--output_file`: Path to save the filtered CSV file (required)
- `--column_indexes`: Comma-separated list of column indexes to keep (zero-based, required)
- `--remove_duplicates`: Remove duplicate rows from the output (optional)
- `--sort_output`: Sort the output by the first selected column (optional)

## Examples

### Extract Specific Columns

```bash
# Keep columns 0, 2, and 4 from a CSV file
python csvnator2.py --input_file sales_data.csv --output_file filtered_sales.csv --column_indexes 0,2,4
```

### Clean and Organize Data

```bash
# Extract columns, remove duplicates, and sort
python csvnator2.py --input_file messy_data.csv --output_file clean_data.csv --column_indexes 0,1,3 --remove_duplicates --sort_output
```

### Process Large Files

```bash
# Process a large CSV file with progress tracking
python csvnator2.py --input_file large_dataset.csv --output_file processed_data.csv --column_indexes 0,1,2,5,8
```

## How It Works

1. **File Reading**: Opens and reads the input CSV file with proper encoding
2. **Column Filtering**: Extracts only the specified columns by index
3. **Header Preservation**: Maintains the original header row
4. **Duplicate Removal**: Removes duplicate rows if requested
5. **Sorting**: Sorts data by the first selected column if requested
6. **Progress Tracking**: Shows progress bar for large files
7. **Output Generation**: Saves the processed data to the output file

## Column Indexing

Column indexes are zero-based:
- Column 0: First column
- Column 1: Second column
- Column 2: Third column
- etc.

Example: To keep the 1st, 3rd, and 5th columns, use `--column_indexes 0,2,4`

## Error Handling

The script includes comprehensive error handling:
- **File not found**: Clear error message if input file doesn't exist
- **Invalid column indexes**: Handles out-of-range column indexes gracefully
- **Empty files**: Detects and reports empty CSV files
- **Encoding issues**: Handles various text encodings properly

## Performance

- **Progress tracking**: Visual progress bar for large files
- **Memory efficient**: Processes files row by row
- **Fast processing**: Optimized for large CSV files
- **Logging**: Detailed logging for monitoring and debugging

## Output

The script provides:
- **Progress updates**: Real-time progress bar
- **Logging information**: Detailed processing logs
- **Success confirmation**: Confirmation when processing completes
- **Error reporting**: Clear error messages for troubleshooting

## Notes

- Original files are never modified (output goes to a new file)
- Headers are preserved in the output
- Column indexes are zero-based
- Supports various CSV formats and encodings
- Works with files of any size (memory efficient)

## Author

Deborah Harrus

## Version

1.0 - Initial version
