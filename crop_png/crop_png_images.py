#!/usr/bin/env python3
"""
Script to automatically crop PNG images to remove empty areas around content.
Detects content boundaries and crops to the minimum area containing the actual content.
Works with any type of image content - charts, diagrams, photos, etc.
"""

import os
import sys
from PIL import Image
import numpy as np
from pathlib import Path

def find_content_boundaries(image):
    """
    Find the boundaries of content in an image by detecting non-white pixels.
    
    Args:
        image: PIL Image object
        
    Returns:
        tuple: (left, top, right, bottom) coordinates of content boundaries
    """
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert to numpy array for easier processing
    img_array = np.array(image)
    
    # Define what we consider "empty" (white or very light colors)
    # We'll use a threshold to detect non-empty pixels
    threshold = 240  # Pixels with RGB values above this are considered empty
    
    # Create a mask for non-empty pixels
    non_empty_mask = np.any(img_array < threshold, axis=2)
    
    if not np.any(non_empty_mask):
        # If no content found, return the full image dimensions
        return (0, 0, image.width, image.height)
    
    # Find the boundaries of non-empty content
    rows = np.any(non_empty_mask, axis=1)
    cols = np.any(non_empty_mask, axis=0)
    
    # Get the first and last rows/columns with content
    top = np.argmax(rows)
    bottom = len(rows) - np.argmax(rows[::-1])
    left = np.argmax(cols)
    right = len(cols) - np.argmax(cols[::-1])
    
    return (left, top, right, bottom)

def crop_image(image_path, output_path=None, margin=10):
    """
    Crop an image to remove empty areas around the content.
    
    Args:
        image_path: Path to the input image
        output_path: Path for the output image (if None, overwrites original)
        margin: Additional margin to add around the content (in pixels)
        
    Returns:
        bool: True if cropping was successful, False otherwise
    """
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Find content boundaries
            left, top, right, bottom = find_content_boundaries(img)
            
            # Add margin
            left = max(0, left - margin)
            top = max(0, top - margin)
            right = min(img.width, right + margin)
            bottom = min(img.height, bottom + margin)
            
            # Check if cropping is needed
            if left == 0 and top == 0 and right == img.width and bottom == img.height:
                print(f"No cropping needed for {image_path}")
                return True
            
            # Crop the image
            cropped_img = img.crop((left, top, right, bottom))
            
            # Determine output path
            if output_path is None:
                output_path = image_path
            
            # Save the cropped image
            cropped_img.save(output_path, 'PNG')
            
            print(f"Cropped {image_path} from {img.size} to {cropped_img.size}")
            return True
            
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

def process_directory(directory_path, pattern="*.png", margin=10):
    """
    Process all PNG files matching the pattern in a directory.
    
    Args:
        directory_path: Path to the directory containing images
        pattern: Glob pattern to match files (default: all PNG files)
        margin: Additional margin to add around content
    """
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Directory {directory_path} does not exist.")
        return
    
    # Find all matching PNG files
    png_files = list(directory.glob(pattern))
    
    if not png_files:
        print(f"No PNG files found matching pattern '{pattern}' in {directory_path}")
        return
    
    print(f"Found {len(png_files)} PNG files to process:")
    for file in png_files:
        print(f"  - {file.name}")
    
    # Process each file
    successful = 0
    for file_path in png_files:
        if crop_image(file_path, margin=margin):
            successful += 1
    
    print(f"\nProcessing complete: {successful}/{len(png_files)} files cropped successfully.")

def main():
    """Main function to handle command line arguments."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Crop PNG images to remove empty areas around content")
    parser.add_argument("path", help="Path to image file or directory")
    parser.add_argument("-o", "--output", help="Output path (for single file processing)")
    parser.add_argument("-m", "--margin", type=int, default=10, 
                       help="Margin to add around content (default: 10 pixels)")
    parser.add_argument("-p", "--pattern", default="*.png",
                       help="File pattern for directory processing (default: *.png)")
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_file():
        # Process single file
        if crop_image(path, args.output, args.margin):
            print("File processed successfully.")
        else:
            print("Failed to process file.")
            sys.exit(1)
    
    elif path.is_dir():
        # Process directory
        process_directory(path, args.pattern, args.margin)
    
    else:
        print(f"Path {args.path} does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main() 