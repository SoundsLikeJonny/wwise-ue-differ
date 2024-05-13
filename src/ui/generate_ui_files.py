import glob
import os
from pathlib import Path


def main():
    """
    Creates the PySide6 Python UI files from .ui files
    Created in UCS Voice Naming Tool\\src\\ui\\gui
    """

    path_to_gui = Path().joinpath(os.getcwd(), 'gui')

    print(f"""
    #################
    #################
    #################
    #################

    {path_to_gui}

    #################
    #################
    #################
    #################
    """)

    for file in glob.glob(f"{path_to_gui}\\*.ui"):
        py_filename = Path(f'{path_to_gui}{file}').stem
        py_filepath = Path(f'{path_to_gui}\\{py_filename}.py')
        os.system(f'pyside6-uic "{file}" -o "{py_filepath}"')


if __name__ == "__main__":
    main()
