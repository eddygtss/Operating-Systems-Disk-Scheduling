import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--requests', type=str, help='comma-delimited list of integers of cylinder requests')
parser.add_argument('--head_pos', type=int, help='the starting position of the head')
parser.add_argument('--algo', type=str, help='type of algorithm to use. Acceptable values are FCFS, SCAN, and CSCAN')
args = parser.parse_args()
global size, cylinders


def fcfs(head, req):
    current = head
    for position in req:
        print(str(current) + '->' + position)
        current = position


def scan(head, req):
    current = head
    next_pos = 0

    for i in range(0, len(req)):

        dif_1 = int(req[i]) - current
        for j in range(len(req)):
            dif_2 = int(req[j]) - current

            if abs(dif_2) <= abs(dif_1) and dif_2 > 0 and abs(dif_2) + abs(dif_1) != 0:
                next_pos = int(req[j])
                dif_1 = dif_2
            elif dif_2 > 0 and abs(dif_1) == 0:
                next_pos = int(req[j])
                dif_1 = dif_2
            elif current == next_pos and j == (len(req) - 1):
                dif_1 = 0

        print(str(current) + '->' + str(next_pos))
        current = next_pos

    print(req)


def cscan(head, req):
    for i in range(len(req)):

        min_sort = i
        for j in range(i + 1, len(req)):
            if int(req[min_sort]) > int(req[j]):
                min_sort = j

        req[i], req[min_sort] = req[min_sort], req[i]


if __name__ == '__main__':
    request = args.requests.split(',')
    algorithm = args.algo
    head_pos = args.head_pos

    size = len(algorithm)
    cylinders = 200

    if algorithm.lower() == 'fcfs':
        fcfs(head_pos, request)
    elif algorithm.lower() == 'scan':
        scan(head_pos, request)
    elif algorithm.lower() == 'cscan':
        cscan(head_pos, request)
