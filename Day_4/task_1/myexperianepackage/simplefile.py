import pandas as pd


def read_file(path, option='text'):
    with open(path, 'r') as file:
        if option == 'text':
            return file.read()
        elif option == 'lines':
            return file.readlines()


def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)


def read_excel(path):
    return pd.read_excel(path)


def write_excel(path, df):
    df.to_excel(path, index=False)
