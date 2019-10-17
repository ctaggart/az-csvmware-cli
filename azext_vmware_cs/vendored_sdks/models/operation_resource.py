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


class OperationResource(Model):
    """Operation status response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar end_time: End time of the operation
    :vartype end_time: datetime
    :param error: Error Message if operation failed
    :type error: ~azure.mgmt.vmwarecloudsimple.models.OperationError
    :ivar id: Operation Id
    :vartype id: str
    :ivar name: Operation ID
    :vartype name: str
    :ivar start_time: Start time of the operation
    :vartype start_time: datetime
    :ivar status: Operation status
    :vartype status: str
    """

    _validation = {
        'end_time': {'readonly': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'start_time': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'OperationError'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationResource, self).__init__(**kwargs)
        self.end_time = None
        self.error = kwargs.get('error', None)
        self.id = None
        self.name = None
        self.start_time = None
        self.status = None
