def group_by_owners(files):
    count_user = {}
    for i,j in files.items():
        for j in files.items():
            count_user[j] = files.count(j)
    print(count_user)

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
