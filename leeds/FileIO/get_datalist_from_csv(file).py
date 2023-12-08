import csv

def display_playlist(file):
    # check if the file is found
    try:
        with open(file) as fileObject:
            # create a 'csv reader' from the file object
            reader = csv.reader(fileObject)

            # create a list from the reader
            data = list(reader)

            # print the header
            print("-".ljust(74, "-"))
            print('|{}|{}|{}|{}|'.
                  format(data[0][0].ljust(21, " "), data[0][1].ljust(14, " "),
                         data[0][2].ljust(21, " "), data[0][3].ljust(5, " ")))
            print("-".ljust(74, "-"))

            # print the data
            for x in data[1:]:
                print('|{}|{}|{}|{}|'
                      .format(x[0].ljust(21, " "), x[1].ljust(14, " "),
                              x[2].ljust(21, " "), x[3].ljust(5, " ")))
            print("-".ljust(74, "-"))
    except FileNotFoundError:
        print("File not found.")
    

display_playlist("geek_music.csv")