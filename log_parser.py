import csv
import re
import sys

log_file = sys.argv[1]
output_file = 'output.csv'

pattern = re.compile(r'(.+):(\d+):\s+warning:\s+(.+)')

with open(log_file) as infile, open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['File', 'Line', 'Message'])
    for line in infile:
        match = pattern.match(line)
        if match:
            writer.writerow(match.groups())
