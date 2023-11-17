__author__ = "Jarec Basham"
__version__ = "0.0.1"

from cli.flows import load_flow

SEPARATOR = "========================================"


def start():
    print_banner()
    load_flow()


def print_banner():
    print(SEPARATOR)
    print('Periodicity')
    print(f'Author: {__author__}')
    print(f'Version: {__version__}')


if __name__ == '__main__':
    start()
