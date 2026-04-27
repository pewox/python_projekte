
from argparse import ArgumentParser

def ip_port(ipaddress='', port='', user=''):
    return f'https://{user}@' + ':'.join([ipaddress,port])

parser = ArgumentParser()
parser.add_argument('-p', '--port', type=str, default='<port>')
parser.add_argument('-a', '--ipaddress', type=str ,default='<ip>')
parser.add_argument('-u', '--user', type=str, default='<user>')
args = parser.parse_args()

print(ip_port(args.ipaddress, args.port, args.user))
print(args.port, args.user, args.ipaddress)