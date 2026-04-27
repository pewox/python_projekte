import yaml
from collections import defaultdict

groups = set(['webserver','dbserver','idxserver','webserver','fileserver','appserver','ubuntu','oracle','sles'])
vm_obj = [
    {
        'name': 'vm1',
        'tags': ['small_web1','ubuntu', 'webserver'],
    },
    {
        'name': 'vm2',
        'tags': ['med_db1','ubuntu', 'dbserver'],
    },
    {
        'name': 'vm3',
        'tags': ['small_idx1','oracle', 'idxserver'],
    },
    {
        'name': 'vm4',
        'tags': ['med_web2','oracle', 'webserver'],
    },
    {
        'name': 'vm5',
        'tags': ['med_filesrv1','oracle', 'fileserver'],
    },
    {
        'name': 'vm6',
        'tags': ['small_appsrv1','sles', 'appserver'],
    },
    {
        'name': 'vm7',
        'tags': ['med_db2','ubuntu'],
    }
]

out_file = 'inventory_defaultdict.yaml'

def create_inventory(groups, vm_obj, out_file):
    inventory = defaultdict(list)
    for i in range(len(vm_obj)):
        intersect = groups & set(vm_obj[i]['tags'])
        for grp in intersect:
            inventory[grp].append(vm_obj[i]['name'])
    with open(f'{out_file}','w') as inv:
        inv.write('---\n' + yaml.safe_dump(dict(inventory)) + '\n---')

    print(type(inventory))

if __name__=='__main__':
    create_inventory(groups, vm_obj, out_file)