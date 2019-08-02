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


class VirtualDisk(Model):
    """Virtual disk model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param controller_id: Required. Disk's Controller id
    :type controller_id: str
    :param independence_mode: Required. Disk's independence mode type.
     Possible values include: 'persistent', 'independent_persistent',
     'independent_nonpersistent'
    :type independence_mode: str or
     ~azure.mgmt.vmwarecloudsimple.models.DiskIndependenceMode
    :param total_size: Required. Disk's total size
    :type total_size: int
    :param virtual_disk_id: Disk's id
    :type virtual_disk_id: str
    :ivar virtual_disk_name: Disk's display name
    :vartype virtual_disk_name: str
    """

    _validation = {
        'controller_id': {'required': True},
        'independence_mode': {'required': True},
        'total_size': {'required': True},
        'virtual_disk_name': {'readonly': True},
    }

    _attribute_map = {
        'controller_id': {'key': 'controllerId', 'type': 'str'},
        'independence_mode': {'key': 'independenceMode', 'type': 'DiskIndependenceMode'},
        'total_size': {'key': 'totalSize', 'type': 'int'},
        'virtual_disk_id': {'key': 'virtualDiskId', 'type': 'str'},
        'virtual_disk_name': {'key': 'virtualDiskName', 'type': 'str'},
    }

    def __init__(self, *, controller_id: str, independence_mode, total_size: int, virtual_disk_id: str=None, **kwargs) -> None:
        super(VirtualDisk, self).__init__(**kwargs)
        self.controller_id = controller_id
        self.independence_mode = independence_mode
        self.total_size = total_size
        self.virtual_disk_id = virtual_disk_id
        self.virtual_disk_name = None