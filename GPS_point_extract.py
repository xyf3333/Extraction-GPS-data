import csv
import sys


def dataExtract(im_data, out_name):
    print (sys.version)
    INPUT_FILENAME = im_data
    OUTPUT_FILENAME = out_name
    with open(INPUT_FILENAME, 'r') as input_file:
        with open(OUTPUT_FILENAME, 'w') as output_file:
            # create a csv reader object from the input file (nmea files are basically csv)
            reader = csv.reader(input_file)

            # create a csv writer object for the output file
            writer = csv.writer(output_file, delimiter=',', lineterminator='\n')

            # write the header line to the csv file
            writer.writerow(
               ['Latitude', 'Longitude', 'Geographic position'])

            for row in reader:
                if row[0].startswith('$GPGLL'):
                    Longitude = row[1]
                    Latitude = row[3]
                    Geographic_position = row[5]
                    #print(Longitude, Latitude, Geographic_position)
                    writer.writerow([Longitude, Latitude, Geographic_position])


if __name__ == '__main__':

    dataExtract('2021-10-18_115232_serial-COM3.ubx', 'out.csv')