from termcolor import colored

def main():
    while True:
        try:
            sleep_time = int(input("What time are you sleeping: "))
            if sleep_time > 12:
                error_msg()
            else:
                break
        except TypeError:
            error_msg()
        except ValueError:
            error_msg()
            
    sleep_hours_wanted = 7
    
    # The additional hours body needed to shut down
    body_sleep_hours_required = 1
    
    adjusted_hours = sleep_hours_wanted + body_sleep_hours_required

    wakeup_time = (sleep_time + adjusted_hours) % 12
    print(colored(
        f"Set your alarm at: {wakeup_time} AM. Have a good sleep!", 'green'))

def error_msg():
    err_msg = "Error: Time must be an int between 1 and 12."
    print(colored(err_msg, 'red'))
    

if __name__ == '__main__':
    main()