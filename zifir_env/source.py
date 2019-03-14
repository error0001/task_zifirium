import csv


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["Date"],
              line["Campaign"],
              line["id"],
              line["ad_id"],
              line["os"],
              line["Installs"],
              line["app"])


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


if __name__ == "__main__":
    csv_path = "work_files/in_data_a.csv"
    with open(csv_path, "r") as f_obj:
        # csv_reader(f_obj)
        # Открыть с помощью DictReader
        csv_dict_reader(f_obj)