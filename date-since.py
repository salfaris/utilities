import re
from termcolor import colored
from datetime import timedelta
from dateutil.parser import parse

def main():
    yes_pattern = r'^y(es)?$'
    no_pattern = r'^n(o)?$'
    
    while True:
        does_today_counts = input("Does start day counts as a day? [y/n]: ").lower()
        yes_match = re.match(yes_pattern, does_today_counts)
        no_match = re.match(no_pattern, does_today_counts)
        
        if not yes_match and not no_match:
            print("Please answer with y(es) or n(o).")
        else:
            break
    
    start_msg = "Enter start date (e.g. 20/6/2020): "
    date_start = date_prompt(start_msg)
    
    end_msg = "Enter end date (e.g. 20/6/2020): "
    date_end = date_prompt(end_msg)
    
    base_date_diff = date_end - date_start
    
    if yes_match:
        date_diff = base_date_diff + timedelta(days=1)
    else:
        date_diff = base_date_diff
    date_diff_days = abs(date_diff.days)
    print(colored(f"Day difference is: {date_diff_days} day(s).", 'green'))


def date_prompt(date_str):
    while True:
        try:
            date_prompt = parse(input(date_str), dayfirst=True)
            break
        except ValueError:
            print("Incorrect format. Please try again.")
            print()
    return date_prompt

if __name__ == '__main__':
    main()