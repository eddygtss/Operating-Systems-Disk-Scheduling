import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--requests', type=str, help='comma-delimited list of integers of cylinder requests')
parser.add_argument('--head_pos', type=int, help='the starting position of the head')
parser.add_argument('--algo', type=str, help='type of algorithm to use. Acceptable values are FCFS, SCAN, and CSCAN')
args = parser.parse_args()


def fcfs(head, req):
    current = head
    for position in req:
        print(str(current) + '->' + position)
        current = position


def scan(head, req):
    current = head


def cscan(head, req):
    print(req)


if __name__ == '__main__':
    request = args.requests.split(',')
    algorithm = args.algo
    head_pos = args.head_pos

    if algorithm.lower() == 'fcfs':
        fcfs(head_pos, request)
    elif algorithm.lower() == 'scan':
        scan(head_pos, request)
    elif algorithm.lower() == 'cscan':
        cscan(head_pos, request)
