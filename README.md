# DH Tiny Tools

A collection of small, focused Python utilities designed to solve specific tasks efficiently. These tools are built with simplicity and reusability in mind.

## Tools Included

### 📡 [Check Online](check_online/)
A URL accessibility checker that processes multiple URLs from a text file and reports their status. Perfect for verifying if bookmarks, links, or resources are still available.

**Features:**
- Batch URL checking from text files
- Status reporting (accessible, content issues, failed)
- Error handling and timeout protection
- Content validation beyond HTTP status codes

**Quick Start:**
```bash
cd check_online
pip install requests
python check_online.py urls.txt
```

### 📥 [File Downloader](file_downloader/)
A powerful HTML parser and file downloader that can extract and download files of specific types from HTML pages or local HTML files.

**Features:**
- Parse HTML files to find file links of specified types
- Download files automatically with progress bars
- Handle both local HTML files and web URLs
- Organize downloads into folders
- Resume interrupted downloads
- Support for various file types (PDF, PSE, DOCX, etc.)

**Quick Start:**
```bash
cd file_downloader
pip install -r requirements.txt
python file_downloader.py --file "Biology Resources.html" --file-type pdf
```

### ✂️ [PNG Image Cropper](crop_png/)
A smart image cropping tool that automatically removes empty areas around content in PNG images. Perfect for cleaning up screenshots, diagrams, charts, or any images with unnecessary white space.

**Features:**
- Automatic content detection using pixel analysis
- Smart cropping to content boundaries
- Configurable margin settings
- Batch processing of multiple files
- Flexible file pattern matching
- Preserves original image quality

**Quick Start:**
```bash
cd crop_png
pip install -r requirements.txt
python crop_png_images.py image.png
```

### 📊 [CSV Column Filter](csvnator2/)
A powerful CSV processing tool for filtering specific columns with advanced data cleaning capabilities. Perfect for data analysis, cleaning, and transformation tasks.

**Features:**
- Column selection by index from CSV files
- Duplicate removal and data sorting
- Progress tracking for large files
- Robust error handling and logging
- Flexible input/output options
- Memory-efficient processing

**Quick Start:**
```bash
cd csvnator2
pip install -r requirements.txt
python csvnator2.py --input_file data.csv --output_file filtered.csv --column_indexes 0,1,3
```

### 📅 [Rota Table Generator](rota_table_generator/)
A simple tool to generate weekly rota CSV files for any given year. Each week starts on Monday and ends on Sunday. Perfect for creating schedule templates, planning calendars, or generating weekly rota tables.

**Features:**
- Year-based generation for any year
- Standard week format (Monday to Sunday)
- Clean CSV output format
- Custom output filenames
- No external dependencies
- 52-week coverage per year

**Quick Start:**
```bash
cd rota_table_generator
python generate_rota.py 2025
```

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/dh_tiny_tools.git
   cd dh_tiny_tools
   ```

2. Each tool has its own requirements. Navigate to the tool directory and install dependencies:
   ```bash
   cd tool_name
   pip install -r requirements.txt  # if requirements.txt exists
   ```

## Usage

Each tool is self-contained and can be used independently. Navigate to the specific tool directory and follow the instructions in its README file.

### Tool Directory Structure

```
dh_tiny_tools/
├── check_online/
│   ├── check_online.py
│   └── README.md
├── file_downloader/
│   ├── file_downloader.py
│   ├── example_usage.py
│   ├── README.md
│   └── requirements.txt
├── crop_png/
│   ├── crop_png_images.py
│   ├── crop_all_png.bat
│   ├── README.md
│   └── requirements.txt
├── csvnator2/
│   ├── csvnator2.py
│   ├── README.md
│   └── requirements.txt
├── rota_table_generator/
│   ├── generate_rota.py
│   └── README.md
└── README.md
```

## Contributing

These tools are designed to be simple and focused. If you'd like to contribute:

1. Keep tools small and focused on a single task
2. Include proper error handling
3. Add comprehensive documentation
4. Include example usage
5. Add a README.md file for each tool

## Author

**Deborah Harrus**

## License

This project is open source. Feel free to use, modify, and distribute these tools as needed.

## Future Tools

This collection will grow over time with additional tiny tools for various tasks. Each tool will be:
- **Focused**: Does one thing well
- **Simple**: Easy to understand and modify
- **Reusable**: Can be easily adapted for different use cases
- **Well-documented**: Clear instructions and examples

---

*"The best code is no code at all, but when you need code, make it tiny and focused."* 
