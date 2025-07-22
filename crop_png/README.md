# PNG Image Cropper

A Python script that automatically crops PNG images to remove empty areas around content by detecting content boundaries. Perfect for cleaning up screenshots, diagrams, charts, or any images with unnecessary white space.

## Features

- **Automatic content detection**: Finds the boundaries of actual content in images
- **Smart cropping**: Removes empty white/light areas while preserving content
- **Configurable margin**: Add custom padding around detected content
- **Batch processing**: Process single files or entire directories
- **Flexible patterns**: Support for custom file patterns and filters
- **Error handling**: Graceful handling of processing errors

## Use Cases

- **Screenshots**: Remove unnecessary white space from screenshots
- **Charts and diagrams**: Crop to just the chart area
- **Photos**: Remove empty borders from scanned photos
- **UI mockups**: Clean up design mockups
- **Documentation**: Prepare images for documentation or presentations

## Requirements

- Python 3.x
- Pillow (PIL)
- NumPy

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start (Windows)
Double-click `crop_all_png.bat` to process all PNG files in the current directory.

### Command Line Usage

#### Process a single file:
```bash
python crop_png_images.py image.png
```

#### Process a single file with custom output:
```bash
python crop_png_images.py image.png -o cropped_image.png
```

#### Process all PNG files in current directory:
```bash
python crop_png_images.py . -p "*.png"
```

#### Process specific file patterns:
```bash
python crop_png_images.py . -p "*_screenshot.png"
```

#### Adjust margin around content:
```bash
python crop_png_images.py . -p "*.png" -m 20
```

### Command Line Options

- `path`: Path to image file or directory
- `-o, --output`: Output path (for single file processing)
- `-m, --margin`: Margin to add around content (default: 10 pixels)
- `-p, --pattern`: File pattern for directory processing (default: *.png)

## How It Works

The script uses intelligent content detection:

1. **Image Analysis**: Converts image to RGB format and analyzes pixel values
2. **Content Detection**: Identifies non-white pixels (RGB values < 240) as content
3. **Boundary Calculation**: Finds the minimum bounding box containing all content
4. **Smart Cropping**: Crops to content boundaries plus configurable margin
5. **Quality Preservation**: Maintains original image quality and format

## Examples

```bash
# Crop all PNG files with 15px margin
python crop_png_images.py . -p "*.png" -m 15

# Crop a specific screenshot
python crop_png_images.py screenshot.png

# Crop all screenshots in a directory
python crop_png_images.py /path/to/screenshots -p "*_screenshot.png"

# Process with custom output
python crop_png_images.py diagram.png -o clean_diagram.png
```

## Configuration

### Threshold Settings
The script considers pixels with RGB values above 240 as "empty". This works well for:
- White backgrounds
- Light gray backgrounds
- Transparent areas

### Margin Settings
- **Default**: 10 pixels around content
- **Small content**: Use 5-10 pixels
- **Large content**: Use 15-20 pixels
- **Documentation**: Use 20-30 pixels for better presentation

## Notes

- Original files are overwritten unless an output path is specified
- The script handles errors gracefully and reports success/failure for each file
- Works best with images that have clear content boundaries
- Supports any PNG image regardless of content type
- Maintains original image quality and transparency

## Author

Deborah Harrus

## Version

1.0 - Initial version 
