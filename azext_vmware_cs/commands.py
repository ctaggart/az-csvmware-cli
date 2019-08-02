# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_vmware_cs._client_factory import cf_vmware_cs


def load_command_table(self, _):

    # TODO: Add command type here
    # vmware_cs_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_vmware_cs)


    with self.command_group('vmware_cs') as g:
        g.custom_command('create', 'create_vmware_cs')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_vmware_cs')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_vmware_cs')


    with self.command_group('vmware_cs', is_preview=True):
        pass
