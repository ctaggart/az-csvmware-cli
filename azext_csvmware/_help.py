# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
"""
This file contains the help strings (summaries and examples) for all commands and command groups.
"""

from knack.help_files import helps  # pylint: disable=unused-import

helps['csvmware'] = """
    type: group
    short-summary: Manage Azure VMware Solution by CloudSimple.
"""

helps['csvmware vm'] = """
    type: group
    short-summary: Manage VMware virtual machines.
"""

helps['csvmware vm create'] = """
    type: command
    short-summary: Create a VMware virtual machine.

    parameters:
        - name: --nic
          short-summary: Add or modify NICs.
          long-summary: |
            By default, the nics will be added according to the vSphere VM template.
            You can add more nics, or modify some properties of a nic specified in the VM template.
            Multiple nics can be specified by using more than one `--nic` argument.
            If a nic name already exists in the VM template, that nic would be modified according to the user input.
            If a nic name does not exist in the VM template, a new nic would be created and a new name will be assigned to it.
            Usage:   --nic name=MyNicName virtual-network=MyNetwork adapter=MyAdapter power-on-boot=True/False

        - name: --disk
          short-summary: Add or modify disks.
          long-summary: |
            By default, the disks will be added according to the vSphere VM template.
            You can add more disks, or modify some properties of a disk specified in the VM template.
            Multiple disks can be specified by using more than one `--disk` argument.
            If a disk name already exists in the VM template, that disk would be modified according to the user input.
            If a disk name does not exist in the VM template, a new disk would be created and a new name will be assigned to it.
            Usage:   --disk name=MyDiskName controller=SCSIControllerID mode=IndependenceMode size=DiskSizeInKB

    examples:
        - name: Creating a VM with default parameters from the vm template.
          text: >
            az csvmware vm create -n MyVm -g MyResourceGroup -p MyPrivateCloud -r MyResourcePool --template MyVmTemplate

        - name: Creating a VM and adding an extra nic to the VM with virtual network MyVirtualNetwork, adapter VMXNET3, that power ups on boot.
                The name entered in the nic is for identification purposes only, to see if such a nic name exists in the vm template, else a nic is created and a new name is assigned.
                Lets say the vm template contains a nic with name "Network adapter 1".
          text: >
            az csvmware vm create -n MyVm -g MyResourceGroup -p MyPrivateCloud -r MyResourcePool --template MyVmTemplate --nic name=NicNameWouldBeAssigned virtual-network=MyVirtualNetwork adapter=VMXNET3 power-on-boot=True

        - name: Customizing specific properties of a VM. Changing the number of cores to 2 and adapter of "Network adapter 1" nic to E1000E, from that specified in the template. All other properties would be defaulted from the template.
          text: >
            az csvmware vm create -n MyVm -g MyResourceGroup -p MyPrivateCloud -r MyResourcePool --template MyVmTemplate --cores 2 --nic name="Network adapter 1" adapter=E1000E

        - name: Customizing specific properties of a VM. Changing the adapter of "Network adapter 1" nic to E1000E, from that specified in the template, and also adding another nic with virtual network MyVirtualNetwork, adapter VMXNET3, that power ups on boot.
          text: >
            az csvmware vm create -n MyVm -g MyResourceGroup -p MyPrivateCloud -r MyResourcePool --template MyVmTemplate --nic name="Network adapter 1" adapter=E1000E --nic name=NicNameWouldBeAssigned virtual-network=MyVirtualNetwork adapter=VMXNET3 power-on-boot=True

        - name: Creating a VM and adding an extra disk to the VM with SCSI controller 0, persistent mode, and 41943040 KB size.
                The name entered in the disk is for identification purposes only, to see if such a disk name exists in the vm template, else a disk is created and a new name is assigned.
                Lets say the vm template contains a disk with name "Hard disk 1".
          text: >
            az csvmware vm create -n MyVm -g MyResourceGroup -p MyPrivateCloud -r MyResourcePool --template MyVmTemplate --disk name=DiskNameWouldBeAssigned controller=1000 mode=persistent size=41943040

        - name: Customizing specific properties of a VM. Changing the size of "Hard disk 1" disk to 21943040 KB, from that specified in the template, and also adding another disk with SCSI controller 0, persistent mode, and 41943040 KB size.
          text: >
            az csvmware vm create -n MyVm -g MyResourceGroup -p MyPrivateCloud -r MyResourcePool --template MyVmTemplate --disk name="Hard disk 1" size=21943040 --disk name=DiskNameWouldBeAssigned controller=1000 mode=persistent size=41943040
"""

helps['csvmware vm list'] = """
    type: command
    short-summary: List details of VMware virtual machines in the current subscription. If resource group is specified, only the details of virtual machines in that resource group would be listed.
    examples:
        - name: List details of VMware VMs in the current subscription.
          text: >
            az csvmware vm list

        - name: List details of VMware VMs in a particular resource group.
          text: >
            az csvmware vm list -g MyResourceGroup

"""

helps['csvmware vm delete'] = """
    type: command
    short-summary: Delete a VMware virtual machine.
    examples:
        - name: Delete a VMware VM.
          text: >
            az csvmware vm delete -n MyVm -g MyResourceGroup
"""

helps['csvmware vm show'] = """
    type: command
    short-summary: Get the details of a VMware virtual machine.
    examples:
        - name: Get the details of a VMware VM.
          text: >
            az csvmware vm show -n MyVm -g MyResourceGroup
"""

helps['csvmware vm start'] = """
    type: command
    short-summary: Start a VMware virtual machine.
    examples:
        - name: Start a VMware VM.
          text: >
            az csvmware vm start -n MyVm -g MyResourceGroup
"""

helps['csvmware vm stop'] = """
    type: command
    short-summary: Stop/Reboot/Suspend a VMware virtual machine.
    examples:
        - name: Power off a VMware VM.
          text: >
            az csvmware vm stop -n MyVm -g MyResourceGroup --mode poweroff

        - name: Restart a VMware VM.
          text: >
            az csvmware vm stop -n MyVm -g MyResourceGroup --mode reboot
"""

helps['csvmware vm update'] = """
    type: command
    short-summary: Update the tags field of a VMware virtual machine.
    examples:
        - name: Add or update a tag.
          text: >
            az csvmware vm update -n MyVm -g MyResourceGroup --set tags.tagName=tagValue

        - name: Remove a tag.
          text: >
            az csvmware vm update -n MyVm -g MyResourceGroup --remove tags.tagName
"""

helps['csvmware vm nic'] = """
    type: group
    short-summary: Manage VMware virtual machine's Network Interface Cards.
"""

helps['csvmware vm nic add'] = """
    type: command
    short-summary: Add NIC to a VMware virtual machine.
    examples:
        - name: Add a NIC with default parameters in a VM.
          text: >
            az csvmware vm nic add --vm-name MyVm -g MyResourceGroup --virtual-network MyVirtualNetwork

        - name: Add a NIC with E1000E adapter that powers on boot in a VM.
          text: >
            az csvmware vm nic add --vm-name MyVm -g MyResourceGroup --virtual-network MyVirtualNetwork --adapter E1000E --power-on-boot true
"""

helps['csvmware vm nic list'] = """
    type: command
    short-summary: List details of NICs available on a VMware virtual machine.
    examples:
        - name: List details of NICs in a VM.
          text: >
            az csvmware vm nic list --vm-name MyVm -g MyResourceGroup
"""

helps['csvmware vm nic show'] = """
    type: command
    short-summary: Get the details of a VMware virtual machine's NIC.
    examples:
        - name: Get the details of a NIC in a VM.
          text: >
            az csvmware vm nic show --vm-name MyVm -g MyResourceGroup -n "My NIC Name"
"""

helps['csvmware vm nic delete'] = """
    type: command
    short-summary: Delete NICs from a VM.
    examples:
        - name: Delete two NICs from a VM.
          text: >
            az csvmware vm nic delete --vm-name MyVm -g MyResourceGroup --nics "My NIC Name 1" "My NIC Name 2"
"""

helps['csvmware vm disk'] = """
    type: group
    short-summary: Manage VMware virtual machine's disks.
"""

helps['csvmware vm disk add'] = """
    type: command
    short-summary: Add disk to a VMware virtual machine.
    examples:
        - name: Add a disk with default parameters in a VM.
          text: >
            az csvmware vm disk add --vm-name MyVm -g MyResourceGroup

        - name: Add a disk with SATA controller 0 and 64 GB memory in a VM.
          text: >
            az csvmware vm disk add --vm-name MyVm -g MyResourceGroup --controller 15000 --size 67108864
"""

helps['csvmware vm disk list'] = """
    type: command
    short-summary: List details of disks available on a VMware virtual machine.
    examples:
        - name: List details of disks in a VM.
          text: >
            az csvmware vm disk list --vm-name MyVm -g MyResourceGroup
"""

helps['csvmware vm disk show'] = """
    type: command
    short-summary: Get the details of a VMware virtual machine's disk.
    examples:
        - name: Get the details of a disk in a VM.
          text: >
            az csvmware vm disk show --vm-name MyVm -g MyResourceGroup -n "My Disk Name"
"""

helps['csvmware vm disk delete'] = """
    type: command
    short-summary: Delete disks from a VM.
    examples:
        - name: Delete two disks from a VM.
          text: >
            az csvmware vm disk delete --vm-name MyVm -g MyResourceGroup --disks "My Disk Name 1" "My Disk Name 2"
"""

helps['csvmware vm-template'] = """
    type: group
    short-summary: Manage VMware virtual machine templates.
"""

helps['csvmware vm-template list'] = """
    type: command
    short-summary: List details of VMware virtual machines templates in a private cloud.
    examples:
        - name: List details of VM templates.
          text: >
            az csvmware vm-template list -p MyPrivateCloud -r MyResourcePool --location eastus
"""

helps['csvmware vm-template show'] = """
    type: command
    short-summary: Get the details of a VMware virtual machines template in a private cloud.
    examples:
        - name: Get the details of a VM template.
          text: >
            az csvmware vm-template show  -n MyVmTemplate -p MyPrivateCloud --location eastus
"""

helps['csvmware virtual-network'] = """
    type: group
    short-summary: Manage virtual networks.
"""

helps['csvmware virtual-network list'] = """
    type: command
    short-summary: List details of available virtual networks in a private cloud.
    examples:
        - name: List details of virtual networks.
          text: >
            az csvmware virtual-network list -p MyPrivateCloud -r MyResourcePool --location eastus
"""

helps['csvmware virtual-network show'] = """
    type: command
    short-summary: Get the details of a virtual network in a private cloud.
    examples:
        - name: Get the details of a virtual network.
          text: >
            az csvmware virtual-network show -n MyVirtualNetwork -p MyPrivateCloud --location eastus
"""

helps['csvmware private-cloud'] = """
    type: group
    short-summary: Manage VMware private clouds.
"""

helps['csvmware private-cloud list'] = """
    type: command
    short-summary: List details of private clouds in a region.
    examples:
        - name: List details of private clouds in East US.
          text: >
            az csvmware private-cloud list --location eastus
"""

helps['csvmware private-cloud show'] = """
    type: command
    short-summary: Get the details of a private cloud in a region.
    examples:
        - name: Get the details of a private cloud which is in East US.
          text: >
            az csvmware private-cloud show -n MyPrivateCloud --location eastus
"""

helps['csvmware resource-pool'] = """
    type: group
    short-summary: Manage VMware resource pools.
"""

helps['csvmware resource-pool list'] = """
    type: command
    short-summary: List details of resource pools in a private cloud.
    examples:
        - name: List details of resource pools.
          text: >
            az csvmware resource-pool list -p MyPrivateCloud --location eastus
"""

helps['csvmware resource-pool show'] = """
    type: command
    short-summary: Get the details of a resource pool in a private cloud.
    examples:
        - name: Get the details of a resource pool.
          text: >
            az csvmware resource-pool show -n MyResourcePool -p MyPrivateCloud --location eastus
"""
