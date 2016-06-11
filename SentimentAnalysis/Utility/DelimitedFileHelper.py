from tempfile import NamedTemporaryFile
import shutil
import csv


class DelimitedFileHelper(object):
    def __init__(self, file_path, delimiter=' ', escape_char='\n', quoting=csv.QUOTE_NONE, quote_char=''):
        self.file_path = file_path
        self.delimiter = delimiter
        self.escape_char = escape_char
        self.quoting = quoting
        self.quote_char = quote_char

    def update_row(self, id, row):
        temp_file = NamedTemporaryFile(mode='w', newline='', delete=False)

        with open(self.file_path, mode='r') as file, temp_file:
            reader = csv.reader(
                file,
                delimiter=self.delimiter,
                escapechar=self.escape_char,
                quoting=self.quoting,
                quotechar=self.quote_char)

            writer = csv.writer(
                temp_file,
                delimiter=self.delimiter,
                escapechar=self.escape_char,
                quoting=self.quoting,
                quotechar=self.quote_char)

            for temp_row in reader:
                tid = temp_row[0].title()
                if tid == id:
                    writer.writerow(row)
                else:
                    writer.writerow(temp_row)

        shutil.move(temp_file.name, self.file_path)

    def get_row(self, id):
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(
                file,
                delimiter=self.delimiter,
                escapechar=self.escape_char,
                quoting=self.quoting,
                quotechar=self.quote_char)

            for row in reader:
                tid = row[0].title()
                if tid == id:
                    return row

    def add_row(self, row):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(
                file,
                delimiter=self.delimiter,
                escapechar=self.escape_char,
                quoting=self.quoting,
                quotechar=self.quote_char)

            writer.writerow(row)

    def get_rows_by_id(self):
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(
                file,
                delimiter=self.delimiter,
                escapechar=self.escape_char,
                quoting=self.quoting,
                quotechar=self.quote_char)
            d = {}
            for row in reader:
                d[row[0].title()] = {}
                for index in range(1, len(row)):
                    d[row[0].title()][index] = row[index]
            return d
