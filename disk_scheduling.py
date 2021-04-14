import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--requests', type=str, help='comma-delimited list of integers of cylinder requests')
parser.add_argument('--head_pos', type=int, help='the starting position of the head')
parser.add_argument('--algo', type=str, help='type of algorithm to use. Acceptable values are FCFS, SCAN, and CSCAN')
args = parser.parse_args()
global req_size, cylinders


def fcfs(head, req):
    current = head
    for position in req:
        print(str(current) + '->' + str(position))
        current = position


def scan(head, req):
    current = head
    next_pos = 0
    count = 0
    list_req = []

    for j in range(size):
        list_req.append(int(req[j]))

    list_req.append(cylinders - 1)
    list_req.sort()

    while True:

        if list_req[count] < head and count == 0:
            temp = list_req[count]
            list_req.pop(count)
            list_req.append(temp)
            continue
        elif list_req[count] < list_req[size] and count > 0:
            temp = list_req[count]
            list_req.pop(count)
            list_req.append(temp)
        else:
            next_pos = list_req[count]
            count += 1
            print(str(current) + '->' + str(next_pos))
            current = next_pos
        if count == size + 1:
            break


def cscan(head, req):
    current = head
    next_pos = 0
    count = 0
    list_req = []

    for j in range(size):
        list_req.append(int(req[j]))

    list_req.append(cylinders - 1)
    list_req.append(0)
    list_req.sort()

    while True:

        if list_req[count] < head and count == 0:
            temp = list_req[count]
            list_req.pop(count)
            list_req.append(temp)
            continue
        else:
            next_pos = list_req[count]
            count += 1
            print(str(current) + '->' + str(next_pos))
            current = next_pos
        if count == size + 2:
            break


if __name__ == '__main__':
    request = args.requests.split(',')
    algorithm = args.algo
    head_pos = args.head_pos
    cylinders = 200
    size = len(request)

    for i in range(len(request)):
        request[i] = int(request[i])

    if algorithm.lower() == 'fcfs':
        fcfs(head_pos, request)
    elif algorithm.lower() == 'scan':
        scan(head_pos, request)
    elif algorithm.lower() == 'cscan':
        cscan(head_pos, request)
