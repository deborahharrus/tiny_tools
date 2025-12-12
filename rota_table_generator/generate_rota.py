#!/usr/bin/env python3
"""
Generate a rota CSV file for any given year.
Each week starts on Monday and ends on Sunday.
"""

import argparse
import csv
from datetime import datetime, timedelta


def get_first_monday_of_year(year):
    """
    Find the Monday of the week containing January 1st of the given year.
    If January 1st is already a Monday, return it. Otherwise, go back to the previous Monday.
    """
    jan_1 = datetime(year, 1, 1)
    # weekday() returns 0 for Monday, 6 for Sunday
    days_since_monday = jan_1.weekday()
    first_monday = jan_1 - timedelta(days=days_since_monday)
    return first_monday


def format_date(date):
    """Format date as 'Month Day, Year' (e.g., 'December 30, 2024')."""
    return date.strftime("%B %d, %Y")


def generate_rota_csv(year, output_file=None):
    """
    Generate a rota CSV file for the given year.
    
    Args:
        year: The year to generate the rota for
        output_file: Optional output filename. If not provided, defaults to 'rota{year}.csv'
    """
    if output_file is None:
        output_file = f"rota{year}.csv"
    
    # Get the first Monday of the year
    first_monday = get_first_monday_of_year(year)
    
    # Generate 52 weeks
    weeks = []
    current_monday = first_monday
    
    for week_num in range(1, 53):
        sunday = current_monday + timedelta(days=6)
        weeks.append({
            'week': f"Week {week_num:02d}",
            'from_date': format_date(current_monday),
            'to_date': format_date(sunday)
        })
        current_monday += timedelta(days=7)
    
    # Write to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Week', 'From date', 'To date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for week in weeks:
            writer.writerow({
                'Week': week['week'],
                'From date': week['from_date'],
                'To date': week['to_date']
            })
    
    print(f"Generated {output_file} with 52 weeks for year {year}")
    print(f"First week: {weeks[0]['from_date']} to {weeks[0]['to_date']}")
    print(f"Last week: {weeks[-1]['from_date']} to {weeks[-1]['to_date']}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate a rota CSV file for any given year. '
                    'Each week starts on Monday and ends on Sunday.'
    )
    parser.add_argument(
        'year',
        type=int,
        help='The year to generate the rota for (e.g., 2025)'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=None,
        help='Output filename (default: rota{year}.csv)'
    )
    
    args = parser.parse_args()
    
    if args.year < 1900 or args.year > 2100:
        print(f"Warning: Year {args.year} seems unusual. Proceeding anyway...")
    
    generate_rota_csv(args.year, args.output)


if __name__ == '__main__':
    main()

