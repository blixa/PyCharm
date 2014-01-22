import csv


MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse (raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""
    #open csv-file
    opened_file = open(raw_file, "rU")

    #read csv-file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    #empty list
    parsed_data = []
    #first line for headers
    fields = csv_data.next()
    #iterate over rows of csv, zip field > value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    #close csv-file
    opened_file.close()
    return parsed_data


def main():
    #call parse func with parameters
    new_data = parse(MY_FILE, ",")
    f= open ("abd.txt", "a")
    f.write(str(new_data) + "\n")
    f.close()
    print new_data

if __name__ == "__main__":
    main()

