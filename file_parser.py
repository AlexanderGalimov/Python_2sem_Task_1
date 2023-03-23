def read_list(file):
    data = []
    with open(file) as f:
        line = f.readline()
        data.extend([int(x) for x in line.split()])
    f.close()

    return data


def write_list_to_file(data, file):
    f = open(file, 'w')
    f.write(" ".join([str(x) for x in data]))
    f.close()
