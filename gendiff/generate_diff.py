import json


def generate_diff(path_to_file1, path_to_file2):
    dict1 = json.load(open(path_to_file1))
    dict2 = json.load(open(path_to_file2))
    result = []
    for i in dict1:
        if i in dict2:
            if dict1[i] == dict2[i]:
                result.append(f'  {i}: {dict1[i]}')
            else:
                result.append(f'- {i}: {dict1[i]}')
                result.append(f'+ {i}: {dict2[i]}')
        else:
            result.append(f'- {i}: {dict1[i]}')
    for i in dict2:
        if i not in dict1:
            result.append(f'+ {i}: {dict2[i]}')

    difference = sorted(result, key=lambda x: x[0] if x.isalpha() else x[2])
    return '{\n' + "\n".join(difference) + '\n}'


path_to_file_1 = '/home/georgiy/python-project-50/gendiff/file1.json'
path_to_file_2 = '/home/georgiy/python-project-50/gendiff/file2.json'
