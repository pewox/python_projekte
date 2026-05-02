import openstack
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.INFO,
    )
LOG = logging.getLogger('test')

conn = openstack.connection(cloud='pw1070')

def make_net(conn):
    """
        [1] https://docs.openstack.org/openstacksdk/latest/user/proxies/network.html
        [2] https://docs.openstack.org/openstacksdk/latest/user/resources/identity/v3/project.html#openstack.identity.v3.project.Project
        [3] https://docs.openstack.org/openstacksdk/latest/user/resources/network/v2/subnet.html#openstack.network.v2.subnet.Subnet
    """

    # https://docs.openstack.org/openstacksdk/latest/user/resources/network/v2/network.html#openstack.network.v2.network.Network
    net = conn.network.find_network("1070-net")
    if not net:
        net = conn.create_network(
            name = "1070-net",
            dns_domain = '.meins.de.',
            admin_state_up = True
            )
        LOG.info(f"Neues Netz erstellt: {net}")

    snet_pool = conn.network.find_subnet_pool('1070-snet-pool')
    if not snet_pool:
        snet_pool = conn.network.create_subnet_pool(
            ip_version = 4,
            name = '1070-snet-pool',
            prefixes = ['10.0.0.0/23']
        )
        LOG.info(f"Neuen Subnet-Pool erstellt: {snet_pool}")

    # https://docs.openstack.org/openstacksdk/latest/user/resources/network/v2/subnet.html#openstack.network.v2.subnet.Subnet
    snet = conn.find_subnet("1070-subnet", network_id=net.id, subnet_pool_id=snet_pool.id, ignore_missing=False)
    if not snet:
        snet = conn.network.create_subnet(
            name = "1070-subnet",
            network_id = net.id,
            ip_version = 4,
            cidr = "10.0.0.0/24",
            dns_publish_fixed_ip = True,
            subnet_pool_id = snet_pool.id
        )
        LOG.info(f"Neues Subnet erstellt {snet}")

    return snet
