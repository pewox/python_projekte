import openstack
import logging
import json

logging.basicConfig(
    filename='app.log',
    #filemode='w',
    level=logging.INFO,
    )
LOG = logging.getLogger('test')

cloud = 'pw1070'
dat_file = 'data.json'
conn = openstack.connection(cloud=cloud)

with open(dat_file, 'r') as dat:
    data = json.load(dat)

def make_net(conn, data):
    net = conn.network.find_network("1070-net")
    if not net:
        net = conn.network.create_network(
            name = "1070-net",
            dns_domain = '.meins.de.',
            admin_state_up = True
            )
        LOG.info(f"Netz erstellt: {net}")
    return net

def make_snet_pool(conn, net, data):
    snet_pool = conn.network.find_subnet_pool('1070-snet-pool')
    if not snet_pool:
        snet_pool = conn.network.create_subnet_pool(
            ip_version = 4,
            name = '1070-snet-pool',
            prefixes = ['10.0.0.0/23']
        )
        LOG.info(f"Subnet-Pool erstellt: {snet_pool}")
    return snet_pool

def make_subnet(conn, net, snet_pool):
    snet = conn.network.find_subnet("1070-subnet", network_id=net.id, subnet_pool_id=snet_pool.id, ignore_missing=False)
    if not snet:
        snet = conn.network.create_subnet(
            name = "1070-subnet",
            network_id = net.id,
            ip_version = 4,
            cidr = "10.0.0.0/24",
            dns_publish_fixed_ip = True,
            subnet_pool_id = snet_pool.id
        )
        LOG.info(f"Subnet erstellt {snet}")
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
        LOG.info(f"RBAC-Policy erstellt {rbac}")
    return rbac
