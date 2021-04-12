import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--requests', type=str, help='comma-delimited list of integers of cylinder requests')
parser.add_argument('--head_pos', type=int, help='the starting position of the head')
parser.add_argument('--algo', type=str, help='type of algorithm to use. Acceptable values are FCFS, SCAN, and CSCAN')
args = parser.parse_args()


def fcfs(req):
    print(req)


if __name__ == '__main__':
    request = [line.split(",") for line in args.requests]
    fcfs(request)
