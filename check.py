import csv
import re
import sys

class LogParser:
    def __init__(self, log_file, output_file='output.csv'):
        self.log_file = log_file
        self.output_file = output_file
        self.pattern = re.compile(r'(.+):(\d+):\s+warning:\s+(.+)')

    def parse(self):
        with open(self.log_file) as infile, open(self.output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['File', 'Line', 'Message'])
            for line in infile:
                match = self.pattern.match(line)
                if match:
                    writer.writerow(match.groups())

    def run(self):
        print(f"Parsing log file: {self.log_file}")
        self.parse()
        print(f"Output written to: {self.output_file}")


# Entry point
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    parser = LogParser(log_file)
    parser.run()
