def get_data_file_selection():
    return input("Enter path to data file: ")


def get_derive_events_selection():
    print('Would you like to display derived events?')
    while True:
        selection = input('Y/N/Q to Quit: ').upper()
        if selection == "Y":
            return True
        elif selection == "N":
            return False
        elif selection == "Q":
            print('Thank you for using Periodicity, Goodbye')
            exit()


def get_prediction_period():
    print('Averaging period for prediction (default 4)')
    while True:
        selection = input(': ')
        if selection == '':
            return 4
        elif selection.isdigit():
            return int(selection)
