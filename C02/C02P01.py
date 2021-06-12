def reduce_file_path(path):
    directory = [el for el in path.split('/') if not el == '']
    result = []

    for d in directory:
        if d == '.':
            continue
        elif d == '..':
            if result:
                result.pop()

        else:
            result.append(d)

    return '/' + '/'.join(result)