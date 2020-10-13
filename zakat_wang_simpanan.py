import datetime as dt
import time
import sys

def delay_print(text, t=0.02):
    '''Prints the text 'text' character by character at a speed of ~t 
    (defaulted at 0.03) seconds.

    Args:
        text (str): the text to print
        t (int): the time difference between two characters being printed

    Returns:
        str
    '''
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(t)

# nisab in RM
nisab = 15762.00

# haul is in days
haul = 365

# zakat rate
zakat_rate = 0.025

yes_list = ['Y', 'yes', 'Yes', 'YES', 'y', 'ya', 'Ya', 'YA']
no_list = ['N', 'no', 'No', 'NO', 'n', 'tidak', 'Tidak', 'TIDAK']

done = False

while not done:
    while True:
        delay_print('Insert amount in RM, separated by a comma: \n')
        user_input = input()

        if ',' in user_input:
            user_input = user_input.replace(',', '')
        
        str_list = user_input.split()    
        try:
            int_list = [round(float(i), 2) for i in str_list]
        except ValueError:
            delay_print(
                'Oops! You have not input valid number(s). Try again... \n')
        else:
            break
    
    total = sum(int_list)
    zakat_pay = round(total * zakat_rate, 2)
    per_month = round(zakat_pay / 12, 2)
    per_day = round(zakat_pay / 365, 2)

    time.sleep(0.5)

    delay_print(f'Amount to pay zakat for the year is RM {zakat_pay}.\n')
    delay_print(f'This is equivalent to RM {per_month} per month,'
                f' which is approx. RM {per_day} per day.\n')
    
    time.sleep(0.5)

    while True:
        delay_print('Do you want to do another calculation?\n')
        print('YES or NO:')
        user_ans = input()

        if user_ans not in (yes_list + no_list):
            delay_print('Oops! Please only answer with a YES or NO.\n')
        elif user_ans in yes_list:
            break
        else: 
            delay_print(
                'Thank you for being zakat-aware. See you for next year!\n')
            done = True
            break

