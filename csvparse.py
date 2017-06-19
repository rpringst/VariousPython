from re import finditer

def separate(data, f, m, l):
    for line in data:
        idx1 = line.find(",\"") + 2
        idx2 = line.find("\",")
        f.append(line[:idx1])
        m.append(line[idx1:idx2])
        l.append(line[idx2:])

def regularize(d):
    for i in xrange(len(d)):
        if d[i] == []:
            d[i] = [-1]
    return d

def main():
    f = open('metroStatAreas.txt')
    dataset = f.readlines()
    first, middle, last = [], [], []
    f.close()

    separate(dataset, first, middle, last)

    dashes = regularize([[i.start() for i in finditer('-', j)] for j in middle])
    endspace = [[i.rindex(' ')] for i in middle]

    for i in xrange(len(dashes)):
        print(middle[i][:endspace[i][0]])

main()
