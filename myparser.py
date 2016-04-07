def parser(filename, format_args,
           encoding='utf-8', separator='\t',
           filt=(lambda x: True),
           replacement=[],
           loglevel='INFO'):
    if loglevel == 'INFO':
        print(filename)
    with open(filename, 'r', encoding=encoding) as fn:
        data = fn.readlines()

    result = [[] for i in format_args]

    for line in data:
        if loglevel == 'DEBUG':
            print(line.strip(), filt(line))
        if not filt(line):
            continue
        line_ = line
        for src, tgt in replacement:
            if src in line:
                if loglevel == 'DEBUG':
                    print("Replace {} in {}".format(src, line))
                line_ = line_.replace(src, tgt)
        if loglevel == 'DEBUG':
            print(line_)
        try:
            new_line = split_line(line_.strip(), format_args, separator)
        except ValueError:
            continue
        except AssertionError:
            continue
        else:
            for mass, val in zip(result, new_line):
                mass.append(val)

    return result


def split_line(line, format_args, separator):
    new_line = line.split(separator)
    assert len(new_line) == len(format_args)
    array = zip(new_line, format_args)
    return [f(i) for (i, f) in array]
