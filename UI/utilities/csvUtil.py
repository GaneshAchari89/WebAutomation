import csv


class CsvData:

    @staticmethod
    def readCsv(filePath):
        rows = []
        try:
            with open(filePath, 'r') as file:
                csvreader = csv.reader(file)
                next(csvreader)  # To skip header
                print(csvreader)
                for row in csvreader:
                    rows.append(row)
            return rows
        except Exception as e:
            print("Error while reading CSV file:", e)
