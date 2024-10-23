import sys
import PySimpleGUI as sg

from settings import Settings


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_pysimplegui_version() -> str:
    return sg.version


def display_simple_window() -> None:
    layout = [
        [sg.Text(f'Hello PySimpleGUI using Python {get_python_version()}')],
    ]
    settings = Settings()
    print(f'{settings=}')
    title: str = f'PySimpleGUI version {get_pysimplegui_version()}'
    window = sg.Window(title, layout, size=(settings.scaled_width, settings.scaled_height))
    while True:
        event, values = window.read()
        # print(f'{event==sg.WIN_CLOSED}')
        # if event == sg.WIN_CLOSED or event == 'Exit':
        # NOTE: it appears tht sg.WIN_CLOSED is the same as None
        if event in (sg.WIN_CLOSED, None, 'Exit'):
            # print(f'{event=}, {sg.WIN_CLOSED=}')
            break
    window.close()
    print('end simple window demo')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    msg = f'Python version {get_python_version()} and PySimpleGUI version {get_pysimplegui_version()}'
    print(msg)
    display_simple_window()
