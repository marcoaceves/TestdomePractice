def group_by_owners(files):
    output={}
    for file  in files:
        new_key=files.get(file)
        print('file', new_key)
        if new_key in output:
            output[new_key].append(file)
            print('hello')
        else:
            output[new_key] = [file]

    return output
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))