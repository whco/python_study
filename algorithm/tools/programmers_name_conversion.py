name = '최대공약수와 최소공배수'
append_suffix = True


def convert(name, append_suffix):
    converted_list = [c if c != ' ' else '_' for c in name]
    converted_list.extend(['.','p','y'] if append_suffix else [])
    print(''.join(converted_list))


if __name__ == '__main__':
    convert(name, append_suffix);