import openstack
import logging
import json

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.INFO,
    )
LOG = logging.getLogger('test')

cloud = 'pw1019'
conn = openstack.connection(cloud=cloud)
dat_file = 'd1019_data.json'

with open(dat_file, 'r') as dat:
    data = json.load(dat)

def make_net(conn, data):
    net = conn.network.find_network(f'{data['proj_nr']}-net')
    if not net:
        net = conn.network.create_network(
            name = f'{data['proj_nr']}-net',
            dns_domain = f'{data['proj_nr']}.ct.thvc.de.',
            admin_state_up = True
            )
        LOG.info(f'Netz OK: {net}')
    return net

def make_snet_pool(conn, data):
    snet_pool = conn.network.find_subnet_pool(f'{data['proj_nr']}-snet-pool')
    if not snet_pool:
        snet_pool = conn.network.create_subnet_pool(
            ip_version = 4,
            name = f'{data['proj_nr']}-snet-pool',
            prefixes = data['snet_pool_pref']
        )
        LOG.info(f"Subnet-Pool OK: {snet_pool}")
    return snet_pool

def make_subnet(conn, data, net, snet_pool):
    snet = conn.network.find_subnet(f'{data['proj_nr']}-subnet')
    if not snet:
        snet = conn.network.create_subnet(
            name = f'{data['proj_nr']}-subnet',
            network_id = net.id,
            ip_version = 4,
            cidr = f'{data['cidr']}',
            dns_publish_fixed_ip = True,
            subnet_pool_id = snet_pool.id
        )
        LOG.info(f"Subnet OK: {snet}")
    return snet

def make_rbac(conn, data, net):
    rbac = conn.network.rbac_policies(data['rbac_obj_type'],)
    if not rbac:
        rbac = conn.network.create_rbac_policy(
            project_id = data['start_proj_id'],
            object_type = data['rbac_obj_type'],
            object_id = net.id,
            target_project_id = data['target_proj_id']
        )
        LOG.info(f"RBAC-Policy OK: {rbac}")
    return rbac

def make_port(conn, data, net, snet):
    port = conn.network.find_port(data[f'{data['transfer_port']}'])
    if not port:
        port = conn.network.create_port(
            name = data['transfer_port'],
            network_id = net.id,
            fixed_ips = [snet.id]
        )