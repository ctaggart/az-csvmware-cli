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


class CustomizationHostName(Model):
    """Host name model.

    :param name: Hostname
    :type name: str
    :param type: Type of host name. Possible values include: 'USER_DEFINED',
     'PREFIX_BASED', 'FIXED', 'VIRTUAL_MACHINE_NAME', 'CUSTOM_NAME'
    :type type: str or ~azure.mgmt.vmwarecloudsimple.models.enum
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CustomizationHostName, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
