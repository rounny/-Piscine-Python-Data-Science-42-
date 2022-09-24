import csv

def read_and_write():
    with open('ds.csv', 'r') as file_csv:
        with open('ds.tsv', 'w') as file_tsv:
            new_text = file_csv.read().replace('\",', '\"\t')
            new_text = new_text.replace('false,', 'false\t')
            new_text = new_text.replace('true,', 'true\t')
            file_tsv.write(new_text)


if __name__ == '__main__':
    read_and_write()
