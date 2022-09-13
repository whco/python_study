name = '가운데 글자 가져오기'
append_suffix = True


def convert(name, append_suffix):
    converted_list = [c if c != ' ' else '_' for c in name]
    converted_list.extend(['.','p','y'] if append_suffix else [])
    print(''.join(converted_list))


if __name__ == '__main__':
    convert(name, append_suffix);