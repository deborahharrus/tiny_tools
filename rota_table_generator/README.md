# Rota Table Generator

A Python script to generate weekly rota CSV files for any given year. Each week starts on Monday and ends on Sunday. Perfect for creating schedule templates, planning calendars, or generating weekly rota tables for any year.

## Features

- **Year-based generation**: Generate rota tables for any year
- **Standard week format**: Weeks start on Monday and end on Sunday
- **CSV output**: Clean, structured CSV format for easy import
- **Custom filenames**: Specify custom output filenames
- **No dependencies**: Uses only Python standard library
- **52-week coverage**: Generates exactly 52 weeks per year

## Use Cases

- **Schedule planning**: Create weekly schedule templates
- **Rota management**: Generate staff rota tables
- **Calendar generation**: Create weekly calendar views
- **Project planning**: Set up weekly project timelines
- **Event scheduling**: Plan events by week

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this repository
2. No additional dependencies required (uses Python standard library)

## Usage

### Basic Usage

Generate a rota CSV file for a specific year:

```bash
python generate_rota.py 2025
```

This will create a file named `rota2025.csv` in the current directory.

### Custom Output Filename

Specify a custom output filename using the `-o` or `--output` option:

```bash
python generate_rota.py 2025 -o my_rota_2025.csv
```

or

```bash
python generate_rota.py 2025 --output my_rota_2025.csv
```

### Examples

Generate rota for different years:

```bash
# Generate rota for 2024
python generate_rota.py 2024

# Generate rota for 2026
python generate_rota.py 2026

# Generate rota for 2027 with custom filename
python generate_rota.py 2027 -o rota_2027_schedule.csv
```

## Output Format

The generated CSV file contains the following columns:
- **Week**: Week number (Week 01, Week 02, ..., Week 52)
- **From date**: Monday date in format "Month Day, Year" (e.g., "December 30, 2024")
- **To date**: Sunday date in format "Month Day, Year" (e.g., "January 5, 2025")

### Example Output

```csv
Week,From date,To date
Week 01,"December 30, 2024","January 5, 2025"
Week 02,"January 6, 2025","January 12, 2025"
Week 03,"January 13, 2025","January 19, 2025"
...
```

## How It Works

1. The script finds the Monday of the week containing January 1st of the specified year
2. If January 1st is already a Monday, it uses that date
3. If January 1st falls on another day, it goes back to the previous Monday
4. It then generates 52 consecutive weeks, each starting on Monday and ending on Sunday

## Command-Line Options

```
positional arguments:
  year                  The year to generate the rota for (e.g., 2025)

optional arguments:
  -h, --help            Show help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename (default: rota{year}.csv)
```

## Notes

- The script generates exactly 52 weeks per year
- Week 01 always starts on the Monday of the week containing January 1st
- Dates are formatted as "Month Day, Year" (e.g., "January 1, 2025")
- The output CSV uses UTF-8 encoding
- No external dependencies required - uses only Python standard library

## Author

Deborah Harrus

## Version

1.0 - Initial version
