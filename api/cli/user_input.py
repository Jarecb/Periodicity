def get_data_file_selection():
    data_file = input("Enter path to data file: ")
    if data_file == '':
        data_file = "RealData/dates.csv"
    return data_file


def get_derive_events_selection():
    print('Would you like to display derived events?')
    while True:
        selection = input('Y/N/Q to Quit: ').upper()
        if selection == "Y":
            return True
        elif selection == "N":
            return False
        elif selection == "Q":
            print("Thank you for using Periodicity, goodbye")
            exit()


def get_prediction_period():
    print('Averaging period for prediction (enter for no prediction)')
    while True:
        selection = input(': ')
        if selection == '':
            return 0
        elif selection.isdigit():
            return int(selection)
