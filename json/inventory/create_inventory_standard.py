import yaml

groups = ['webserver','dbserver','idxserver','webserver','fileserver','appserver','ubuntu','oracle','sles','win25','win22','wsus']
vm_dat = [
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
    },
    {
        'name': 'vm8',
        'tags': ['med_db2','win25','wsus'],
    },
    {
        'name': 'vm9',
        'tags': ['med_db2','win22','appserver'],
    },
]

file = 'inventory_standard.yaml'

def create_inventory(groups, vm_obj, out_file):
    inventory = {}
    for i in range(len(vm_obj)):
        intersect = set(groups) & set(vm_obj[i]['tags'])
        for grp in intersect:
            if grp in inventory:
                inventory[grp].append(vm_obj[i]['name'])
            else:
                inventory[grp] = [(vm_obj[i]['name'])]
    with open(f'{out_file}','w') as inv:
        inv.write(f'---\n{yaml.safe_dump(inventory,indent=2)}\n---')

if __name__=='__main__':
    create_inventory(groups, vm_dat, file)