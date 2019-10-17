# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GuestOSNICCustomization(Model):
    """Guest OS nic customization.

    :param allocation: IP address allocation method. Possible values include:
     'static', 'dynamic'
    :type allocation: str or ~azure.mgmt.vmwarecloudsimple.models.enum
    :param dns_servers: List of dns servers to use
    :type dns_servers: list[str]
    :param gateway: Gateway addresses assigned to nic
    :type gateway: list[str]
    :param ip_address: Static ip address for nic
    :type ip_address: str
    :param mask: Network mask for nic
    :type mask: str
    :param primary_wins_server: primary WINS server for Windows
    :type primary_wins_server: str
    :param secondary_wins_server: secondary WINS server for Windows
    :type secondary_wins_server: str
    """

    _attribute_map = {
        'allocation': {'key': 'allocation', 'type': 'str'},
        'dns_servers': {'key': 'dnsServers', 'type': '[str]'},
        'gateway': {'key': 'gateway', 'type': '[str]'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'mask': {'key': 'mask', 'type': 'str'},
        'primary_wins_server': {'key': 'primaryWinsServer', 'type': 'str'},
        'secondary_wins_server': {'key': 'secondaryWinsServer', 'type': 'str'},
    }

    def __init__(self, *, allocation=None, dns_servers=None, gateway=None, ip_address: str=None, mask: str=None, primary_wins_server: str=None, secondary_wins_server: str=None, **kwargs) -> None:
        super(GuestOSNICCustomization, self).__init__(**kwargs)
        self.allocation = allocation
        self.dns_servers = dns_servers
        self.gateway = gateway
        self.ip_address = ip_address
        self.mask = mask
        self.primary_wins_server = primary_wins_server
        self.secondary_wins_server = secondary_wins_server
