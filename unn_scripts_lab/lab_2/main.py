import argparse
import os
import time
from mem_use_win32 import get_memory_usage
from stonks import Investor, Stock
from work import EnumStrategy, DynamicStrategy
import sys
import traceback

__version__ = '1.0'


class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(-1)


class TaskLauncher:
    def __init__(self):
        self.args = self.parse_args()
        self.exit_code = 0

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description='Investor task')

        parser.add_argument('--input_file', '-i', type=str, action='store',
                            help='Path to input file', required=True)
        parser.add_argument('--output_path', '-o', type=str, action='store',
                            help='Path to output file, for example: /home/sdk/', required=True)
        parser.add_argument('-v', '--version', action='version', help='Show version and exit',
                            version=__version__)
        parser.add_argument('--algorithm', '-a', action='store', type=str,
                            help='Algorithm (enum, dynamic)', required=True)

        _args = parser.parse_args()

        return _args

    @staticmethod
    def header():
        print('=' * 79)
        print(f'Investor task (knapsack problem): {__version__}')
        print('=' * 79)
        print(f'Command:     {sys.argv}')
        print('Python:      {0}; {1}'.format(sys.executable, sys.version.replace('\n', '')))
        print('=' * 79)

    def main(self):
        try:
            self.header()

            input_file = self.args.input_file
            if not os.path.isfile(input_file):
                raise ValueError('Input file required as a parameter')

            output_path = self.args.output_path
            if not os.path.isdir(output_path):
                raise ValueError('Output file required as a parameter')
            output_path = os.path.join(output_path, 'output.txt')

            with open(input_file, 'r') as input_file:
                stocks = []

                lines = input_file.readlines()
                n, m, s = lines[0].split()
                investor = Investor(int(n), int(m), int(s))

                for line in lines[1:]:
                    stocks.append(Stock.add(line))

            strategy = None

            algorithm = self.args.algorithm
            if algorithm == 'enum':
                strategy = EnumStrategy()
            elif algorithm == 'dynamic':
                strategy = DynamicStrategy()

            time_start = time.time()

            result = strategy.investor_work(investor, stocks)

            time_finish = time.time() - time_start

            print(f'Time: {time_finish * 100} MS')
            print(f'Memory: {get_memory_usage() / (1024. * 1024.)} MB')

            print('=' * 79)

            with open(output_path, 'w') as output_path:
                output_path.write(f'{investor.get_result()}\n')
                for stock in result:
                    output_path.write(f'{stock}\n')

        except KeyboardInterrupt:
            print('=' * 79)
            print('PROGRAM WAS INTERRUPTED')
            self.exit_code = -1
        except Exception as ex:
            print('=' * 79)
            print('Something goes wrong **FAILED**:\n{} '.format(ex))
            print('Error: {}'.format(traceback.format_exc()))
            self.exit_code = -2
        return self.exit_code


if __name__ == "__main__":
    sys.exit(TaskLauncher().main())
