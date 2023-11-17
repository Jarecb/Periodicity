def get_data_file_selection():
    return input("Enter path to data file: ")


def get_derive_events_selection():
    print('Would you like to display derived events?')
    while True:
        selection = input('Y/N: ').upper()
        if selection == "Y":
            return True
        elif selection == "N":
            return False


def get_prediction_period():
    print('Averaging period for prediction (default 4)')
    while True:
        selection = input(': ')
        if selection == '':
            return 4
        elif selection.isdigit():
            return int(selection)
