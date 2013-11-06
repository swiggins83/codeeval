import sys

def uniquity(pathname):

    for line in open(pathname, 'r').readlines():
        uniques = []
        line = line.split(",")

        for entry in line:
            if entry.split("\n")[0] not in uniques:
                uniques.append(entry)

        for unique in uniques:
            if unique is uniques[len(uniques)-1]:
                sys.stdout.write(unique)
            else:
                sys.stdout.write(unique + ',')
        print


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        uniquity(arg)
