import csv
import networkx as nx
import pylab as plt

def readcsv(file):
    useridarray = []
    newidarray = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                useridarray = [row[5], row[0], row[1], row[2], row[3], row[4]]
                newidarray.append(useridarray)
                line_count += 1
        print(f'\nProcessed {line_count} users.')
        return newidarray


def readedges(file):
    G = nx.Graph()
    with open(file) as csv_file:
        line_count = 0
        useridarray = []
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                useridarray.append(row[0])
                G.add_edge(int(row[0]), int(row[1]))
                line_count += 1

        print(f'Processed {line_count} users.')
        return G

ids = readcsv("E:\\SJSUSP2020\\1\\ENGB\\PTBR\\musae_PTBR_target.csv")

def getchanneldata(ids):
    import twitchread as tw
    userdata = tw.getchannelinfo(ids)
    if userdata == None:
        return None
    if userdata != None and 'game' in userdata:
        return userdata
    elif 'game' not in userdata:
        print(userdata)
        print("NO GAME")
    else:
        print("Error")
    return userdata

def writecsv(ids):
    import twitchread as tw
    from csv import reader
    from csv import writer
    import itertools
    with open('E:\\SJSUSP2020\\1\\ENGB\\PTBR\\musae_PTBR_target.csv', 'r', encoding="utf-8") as read_obj, \
            open('E:\\SJSUSP2020\\1\\ENGB\\PTBR\\musae_PTBR_target_new.csv', 'w', newline='', encoding="utf-8") as write_obj:

        header = ['id', 'days', 'mature', 'views', 'partner', 'new_id', 'display_name', 'game', 'followers' ]
        #writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csvreader = reader(read_obj)
        csvwriter = writer(write_obj)
        csvwriter.writerow(header)
        next(csvreader)
        for row in csvreader:
            print(row[1] + " " + row[0])
            userdata = getchanneldata(row[0])
            if userdata == None:
                print("No user found")
                row.append("Not Found")
                csvwriter.writerow(row)
                continue
            else:
                print(userdata['display_name'])
                row.append(userdata['display_name'])
                row.append(userdata['game'])
                row.append(userdata['followers'])
                csvwriter.writerow(row)

writecsv(ids)
