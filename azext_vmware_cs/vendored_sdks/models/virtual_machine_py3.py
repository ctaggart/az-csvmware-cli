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


class VirtualMachine(Model):
    """Virtual machine model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id:
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName}
    :vartype id: str
    :param location: Required. Azure region
    :type location: str
    :ivar name: {virtualMachineName}
    :vartype name: str
    :param amount_of_ram: Required. The amount of memory
    :type amount_of_ram: int
    :ivar controllers: The list of Virtual Disks' Controllers
    :vartype controllers:
     list[~azure.mgmt.vmwarecloudsimple.models.VirtualDiskController]
    :param disks: The list of Virtual Disks
    :type disks: list[~azure.mgmt.vmwarecloudsimple.models.VirtualDisk]
    :ivar dnsname: The DNS name of Virtual Machine in VCenter
    :vartype dnsname: str
    :param expose_to_guest_vm: Expose Guest OS or not
    :type expose_to_guest_vm: bool
    :ivar folder: The path to virtual machine folder in VCenter
    :vartype folder: str
    :ivar guest_os: The name of Guest OS
    :vartype guest_os: str
    :ivar guest_os_type: The Guest OS type. Possible values include: 'linux',
     'windows', 'other'
    :vartype guest_os_type: str or
     ~azure.mgmt.vmwarecloudsimple.models.GuestOSType
    :param nics: The list of Virtual NICs
    :type nics: list[~azure.mgmt.vmwarecloudsimple.models.VirtualNic]
    :param number_of_cores: Required. The number of CPU cores
    :type number_of_cores: int
    :param password: Password for login
    :type password: str
    :param private_cloud_id: Required. Private Cloud Id
    :type private_cloud_id: str
    :ivar provisioning_state: The provisioning status of the resource
    :vartype provisioning_state: str
    :ivar public_ip: The public ip of Virtual Machine
    :vartype public_ip: str
    :param resource_pool: Virtual Machines Resource Pool
    :type resource_pool: ~azure.mgmt.vmwarecloudsimple.models.ResourcePool
    :ivar status: The status of Virtual machine. Possible values include:
     'running', 'suspended', 'poweredoff', 'updating', 'deallocating',
     'deleting'
    :vartype status: str or
     ~azure.mgmt.vmwarecloudsimple.models.VirtualMachineStatus
    :param template_id: Virtual Machine Template Id
    :type template_id: str
    :param username: Username for login
    :type username: str
    :param v_sphere_networks: The list of Virtual VSphere Networks
    :type v_sphere_networks: list[str]
    :ivar vm_id: The internal id of Virtual Machine in VCenter
    :vartype vm_id: str
    :ivar vmwaretools: VMware tools version
    :vartype vmwaretools: str
    :param tags: The list of tags
    :type tags: dict[str, str]
    :ivar type: {resourceProviderNamespace}/{resourceType}
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
        'name': {'readonly': True, 'pattern': r'^[-a-zA-Z0-9]+$'},
        'amount_of_ram': {'required': True},
        'controllers': {'readonly': True},
        'dnsname': {'readonly': True},
        'folder': {'readonly': True},
        'guest_os': {'readonly': True},
        'guest_os_type': {'readonly': True},
        'number_of_cores': {'required': True},
        'private_cloud_id': {'required': True},
        'provisioning_state': {'readonly': True},
        'public_ip': {'readonly': True},
        'status': {'readonly': True},
        'vm_id': {'readonly': True},
        'vmwaretools': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'amount_of_ram': {'key': 'properties.amountOfRam', 'type': 'int'},
        'controllers': {'key': 'properties.controllers', 'type': '[VirtualDiskController]'},
        'disks': {'key': 'properties.disks', 'type': '[VirtualDisk]'},
        'dnsname': {'key': 'properties.dnsname', 'type': 'str'},
        'expose_to_guest_vm': {'key': 'properties.exposeToGuestVM', 'type': 'bool'},
        'folder': {'key': 'properties.folder', 'type': 'str'},
        'guest_os': {'key': 'properties.guestOS', 'type': 'str'},
        'guest_os_type': {'key': 'properties.guestOSType', 'type': 'GuestOSType'},
        'nics': {'key': 'properties.nics', 'type': '[VirtualNic]'},
        'number_of_cores': {'key': 'properties.numberOfCores', 'type': 'int'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'private_cloud_id': {'key': 'properties.privateCloudId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'public_ip': {'key': 'properties.publicIP', 'type': 'str'},
        'resource_pool': {'key': 'properties.resourcePool', 'type': 'ResourcePool'},
        'status': {'key': 'properties.status', 'type': 'VirtualMachineStatus'},
        'template_id': {'key': 'properties.templateId', 'type': 'str'},
        'username': {'key': 'properties.username', 'type': 'str'},
        'v_sphere_networks': {'key': 'properties.vSphereNetworks', 'type': '[str]'},
        'vm_id': {'key': 'properties.vmId', 'type': 'str'},
        'vmwaretools': {'key': 'properties.vmwaretools', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, location: str, amount_of_ram: int, number_of_cores: int, private_cloud_id: str, disks=None, expose_to_guest_vm: bool=None, nics=None, password: str=None, resource_pool=None, template_id: str=None, username: str=None, v_sphere_networks=None, tags=None, **kwargs) -> None:
        super(VirtualMachine, self).__init__(**kwargs)
        self.id = None
        self.location = location
        self.name = None
        self.amount_of_ram = amount_of_ram
        self.controllers = None
        self.disks = disks
        self.dnsname = None
        self.expose_to_guest_vm = expose_to_guest_vm
        self.folder = None
        self.guest_os = None
        self.guest_os_type = None
        self.nics = nics
        self.number_of_cores = number_of_cores
        self.password = password
        self.private_cloud_id = private_cloud_id
        self.provisioning_state = None
        self.public_ip = None
        self.resource_pool = resource_pool
        self.status = None
        self.template_id = template_id
        self.username = username
        self.v_sphere_networks = v_sphere_networks
        self.vm_id = None
        self.vmwaretools = None
        self.tags = tags
        self.type = None
