from termcolor import colored

def main():
    # The additional hours body needed to shut down
    body_sleep_hours_required = 1
    
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
            
    while True:
        sleep_hours_wanted = input("How many hours do you want to sleep: ")
        if sleep_hours_wanted is None:
            sleep_hours_wanted = 7
            break
        else:
            try:
                sleep_hours_wanted = int(sleep_hours_wanted)
                break
            except TypeError:
                error_msg()
            except ValueError:
                error_msg()
        
    adjusted_hours = sleep_hours_wanted + body_sleep_hours_required
    wakeup_time = (sleep_time + adjusted_hours) % 12
    
    print(colored(
        f"Set your alarm at: {wakeup_time} AM. Have a good sleep!", 'green'))


def error_msg():
    err_msg = "Error: Time must be an int between 1 and 12."
    print(colored(err_msg, 'red'))
    

if __name__ == '__main__':
    main()