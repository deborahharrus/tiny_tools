# Check Online

A simple Python script to check if a set of URLs are accessible or not. This tool is useful for verifying the status of multiple URLs at once, such as checking if bookmarks, links, or resources are still available.

## Features

- **Batch URL checking**: Process multiple URLs from a text file
- **Status reporting**: Shows whether each URL is accessible, has content issues, or failed to load
- **Error handling**: Graceful handling of network errors and timeouts
- **Content validation**: Checks for "Page not found" messages in addition to HTTP status codes
- **Timeout protection**: 10-second timeout to prevent hanging on slow responses

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install requests
   ```

## Usage

### Basic Usage

```bash
python check_online.py <path_to_text_file>
```

### Input File Format

Create a text file with one URL per line. For example:

```
https://www.google.com
https://www.github.com
https://www.example.com
https://www.invalid-url-that-does-not-exist.com
```

### Example

1. Create a file called `urls.txt` with your URLs:
   ```
   https://www.google.com
   https://www.github.com
   https://www.example.com
   ```

2. Run the script:
   ```bash
   python check_online.py urls.txt
   ```

3. View the results:
   ```
   Results:
   https://www.google.com: Accessible (200)
   https://www.github.com: Accessible (200)
   https://www.example.com: Content issue (200)
   ```

## Output

The script provides three types of status:

- **Accessible**: URL returns HTTP 200 and doesn't contain "Page not found"
- **Content issue**: URL returns HTTP 200 but contains "Page not found" or similar content
- **Failed**: URL failed to load (network error, timeout, etc.)

## Error Handling

- **File not found**: Displays an error message if the input file doesn't exist
- **Network errors**: Catches and reports connection issues, timeouts, and other network problems
- **Invalid URLs**: Handles malformed URLs gracefully

## Author

Deborah Harrus

## Version

1.0 (2024-12-04) - Initial version 
