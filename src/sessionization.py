import csv
import datetime
import sys
import heapq

if len(sys.argv) < 4:
    print("Please enter 2 input files and 1 output file.")
    sys.exit(0)

csvFile = sys.argv[1]
textFile = sys.argv[2]
outFile = sys.argv[3]


map = dict()
heap = []
file = open(textFile, "r")
check_time = int(file.read())
file.close()


try:
    outfile = open(outFile, "a")
except IOError:
    print("Unable to open "+outFile+".")


def process_data():
    count = 0
    with open(csvFile, 'rb') as csvfile:
        session_reader = csv.reader(csvfile)
        next(session_reader, None)
        for line in session_reader:
            user = line[0]
            dt_obj = datetime.datetime.strptime(line[1]+" "+line[2], "%Y-%m-%d %H:%M:%S")

            for person in map.keys():
                if dt_obj > map[person]['time_count']:
                    write_to_file(person, map[person])
                    map.pop(person)

            if user not in map:
                map[user] = dict()
                map[user]['first_time'] = dt_obj
                map[user]['last_time'] = dt_obj
                map[user]['time_count'] = datetime.timedelta(seconds=check_time) + dt_obj
                map[user]['web_count'] = 1
                map[user]['count'] = count
                count += 1
            else:
                map[user]['last_time'] = dt_obj
                map[user]['web_count'] += 1
                map[user]['time_count'] = datetime.timedelta(seconds=check_time) + dt_obj

    for user in map:
        heapq.heappush(heap, [map[user]['count'], user])

    while heap:
        key, user = heapq.heappop(heap)
        write_to_file(user, map[user])


def write_to_file(id, line):
    session = int((map[id]['last_time'] - map[id]['first_time']
                                                 + datetime.timedelta(seconds=1)).total_seconds())
    first = line['first_time'].strftime("%Y-%m-%d %H:%M:%S")
    last = line['last_time'].strftime("%Y-%m-%d %H:%M:%S")
    string = id + ','+first+','+last+','+str(session)+','+str(line['web_count'])
    outfile.write(string+'\n')
    return


process_data()
csvFile.close()
outfile.close()
