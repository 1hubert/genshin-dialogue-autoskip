def exit_program():
    def on_press(key):
        if str(key) == 'Key.f8':
            main.status = 'pause'
            user_input = input('Program paused, continue? (y/n) ')

            while user_input != 'y' and user_input !='n':
                user_input = input('Incorrect input, try either "y" or "n" ')
            
            if user_input == 'y':
                main.status = 'run'
            elif user_input == 'n':
                main.status = 'exit'
                exit()