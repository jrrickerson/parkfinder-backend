import sys
import csv
import json


def main(data_csv, outfile='out.json'):
    with open(data_csv, 'r', encoding='utf-8-sig') as datafile:
        reader = csv.DictReader(datafile)
        output = {
            'parks': [dict(row) for row in reader],
        }
        with open(outfile, 'w') as out:
            json.dump(output, out)


if __name__ == '__main__':
    infile, outfile = sys.argv[1], sys.argv[2]
    print('Writing data from {} to {}'.format(infile, outfile))
    main(sys.argv[1], sys.argv[2])

