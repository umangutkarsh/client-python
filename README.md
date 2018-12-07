# kubevirt-py
This is KubeVirt API an add-on for Kubernetes.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: v0.12.0-alpha.0-10-ge817c4f6
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/kubevirt/kubevirt](https://github.com/kubevirt/kubevirt)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/kubevirt/client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kubevirt/client-python.git`)

Then import the package:
```python
import kubevirt 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kubevirt
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubevirt.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubevirt.configuration.api_key_prefix['authorization'] = 'Bearer'
# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Health endpoint
    api_instance.check_health()
except ApiException as e:
    print("Exception when calling DefaultApi->check_health: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**check_health**](docs/DefaultApi.md#check_health) | **GET** /apis/kubevirt.io/v1alpha2/healthz | Health endpoint
*DefaultApi* | [**console**](docs/DefaultApi.md#console) | **GET** /apis/subresources.kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name}/console | Open a websocket connection to a serial console on the specified VirtualMachineInstance.
*DefaultApi* | [**create_namespaced_virtual_machine**](docs/DefaultApi.md#create_namespaced_virtual_machine) | **POST** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines | Create a VirtualMachine object.
*DefaultApi* | [**create_namespaced_virtual_machine_instance**](docs/DefaultApi.md#create_namespaced_virtual_machine_instance) | **POST** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances | Create a VirtualMachineInstance object.
*DefaultApi* | [**create_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#create_namespaced_virtual_machine_instance_migration) | **POST** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations | Create a VirtualMachineInstanceMigration object.
*DefaultApi* | [**create_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#create_namespaced_virtual_machine_instance_preset) | **POST** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets | Create a VirtualMachineInstancePreset object.
*DefaultApi* | [**create_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#create_namespaced_virtual_machine_instance_replica_set) | **POST** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets | Create a VirtualMachineInstanceReplicaSet object.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines | Delete a collection of VirtualMachine objects.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine_instance**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine_instance) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances | Delete a collection of VirtualMachineInstance objects.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine_instance_migration) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations | Delete a collection of VirtualMachineInstanceMigration objects.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine_instance_preset) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets | Delete a collection of VirtualMachineInstancePreset objects.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine_instance_replica_set) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets | Delete a collection of VirtualMachineInstanceReplicaSet objects.
*DefaultApi* | [**delete_namespaced_virtual_machine**](docs/DefaultApi.md#delete_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines/{name} | Delete a VirtualMachine object.
*DefaultApi* | [**delete_namespaced_virtual_machine_instance**](docs/DefaultApi.md#delete_namespaced_virtual_machine_instance) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name} | Delete a VirtualMachineInstance object.
*DefaultApi* | [**delete_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#delete_namespaced_virtual_machine_instance_migration) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | Delete a VirtualMachineInstanceMigration object.
*DefaultApi* | [**delete_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#delete_namespaced_virtual_machine_instance_preset) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets/{name} | Delete a VirtualMachineInstancePreset object.
*DefaultApi* | [**delete_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#delete_namespaced_virtual_machine_instance_replica_set) | **DELETE** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | Delete a VirtualMachineInstanceReplicaSet object.
*DefaultApi* | [**get_api_group**](docs/DefaultApi.md#get_api_group) | **GET** /apis | Get a KubeVirt API GroupList
*DefaultApi* | [**get_api_group_0**](docs/DefaultApi.md#get_api_group_0) | **GET** /apis/kubevirt.io | Get a KubeVirt API group
*DefaultApi* | [**get_api_group_1**](docs/DefaultApi.md#get_api_group_1) | **GET** /apis/subresources.kubevirt.io | Get a KubeVirt API Group
*DefaultApi* | [**get_api_resources**](docs/DefaultApi.md#get_api_resources) | **GET** /apis/kubevirt.io/v1alpha2 | Get KubeVirt API Resources
*DefaultApi* | [**get_api_resources_0**](docs/DefaultApi.md#get_api_resources_0) | **GET** /apis/subresources.kubevirt.io/v1alpha2 | Get a KubeVirt API resources
*DefaultApi* | [**list_namespaced_virtual_machine**](docs/DefaultApi.md#list_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines | Get a list of VirtualMachine objects.
*DefaultApi* | [**list_namespaced_virtual_machine_instance**](docs/DefaultApi.md#list_namespaced_virtual_machine_instance) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances | Get a list of VirtualMachineInstance objects.
*DefaultApi* | [**list_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#list_namespaced_virtual_machine_instance_migration) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations | Get a list of VirtualMachineInstanceMigration objects.
*DefaultApi* | [**list_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#list_namespaced_virtual_machine_instance_preset) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets | Get a list of VirtualMachineInstancePreset objects.
*DefaultApi* | [**list_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#list_namespaced_virtual_machine_instance_replica_set) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets | Get a list of VirtualMachineInstanceReplicaSet objects.
*DefaultApi* | [**list_virtual_machine_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/virtualmachines | Get a list of all VirtualMachine objects.
*DefaultApi* | [**list_virtual_machine_instance_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_instance_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/virtualmachineinstances | Get a list of all VirtualMachineInstance objects.
*DefaultApi* | [**list_virtual_machine_instance_migration_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_instance_migration_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/virtualmachineinstancemigrations | Get a list of all VirtualMachineInstanceMigration objects.
*DefaultApi* | [**list_virtual_machine_instance_preset_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_instance_preset_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/virtualmachineinstancepresets | Get a list of all VirtualMachineInstancePreset objects.
*DefaultApi* | [**list_virtual_machine_instance_replica_set_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_instance_replica_set_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/virtualmachineinstancereplicasets | Get a list of all VirtualMachineInstanceReplicaSet objects.
*DefaultApi* | [**patch_namespaced_virtual_machine**](docs/DefaultApi.md#patch_namespaced_virtual_machine) | **PATCH** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines/{name} | Patch a VirtualMachine object.
*DefaultApi* | [**patch_namespaced_virtual_machine_instance**](docs/DefaultApi.md#patch_namespaced_virtual_machine_instance) | **PATCH** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name} | Patch a VirtualMachineInstance object.
*DefaultApi* | [**patch_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#patch_namespaced_virtual_machine_instance_migration) | **PATCH** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | Patch a VirtualMachineInstanceMigration object.
*DefaultApi* | [**patch_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#patch_namespaced_virtual_machine_instance_preset) | **PATCH** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets/{name} | Patch a VirtualMachineInstancePreset object.
*DefaultApi* | [**patch_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#patch_namespaced_virtual_machine_instance_replica_set) | **PATCH** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | Patch a VirtualMachineInstanceReplicaSet object.
*DefaultApi* | [**read_namespaced_virtual_machine**](docs/DefaultApi.md#read_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines/{name} | Get a VirtualMachine object.
*DefaultApi* | [**read_namespaced_virtual_machine_instance**](docs/DefaultApi.md#read_namespaced_virtual_machine_instance) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name} | Get a VirtualMachineInstance object.
*DefaultApi* | [**read_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#read_namespaced_virtual_machine_instance_migration) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | Get a VirtualMachineInstanceMigration object.
*DefaultApi* | [**read_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#read_namespaced_virtual_machine_instance_preset) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets/{name} | Get a VirtualMachineInstancePreset object.
*DefaultApi* | [**read_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#read_namespaced_virtual_machine_instance_replica_set) | **GET** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | Get a VirtualMachineInstanceReplicaSet object.
*DefaultApi* | [**replace_namespaced_virtual_machine**](docs/DefaultApi.md#replace_namespaced_virtual_machine) | **PUT** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines/{name} | Update a VirtualMachine object.
*DefaultApi* | [**replace_namespaced_virtual_machine_instance**](docs/DefaultApi.md#replace_namespaced_virtual_machine_instance) | **PUT** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name} | Update a VirtualMachineInstance object.
*DefaultApi* | [**replace_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#replace_namespaced_virtual_machine_instance_migration) | **PUT** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | Update a VirtualMachineInstanceMigration object.
*DefaultApi* | [**replace_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#replace_namespaced_virtual_machine_instance_preset) | **PUT** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancepresets/{name} | Update a VirtualMachineInstancePreset object.
*DefaultApi* | [**replace_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#replace_namespaced_virtual_machine_instance_replica_set) | **PUT** /apis/kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | Update a VirtualMachineInstanceReplicaSet object.
*DefaultApi* | [**restart**](docs/DefaultApi.md#restart) | **PUT** /apis/subresources.kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachines/{name}/restart | Restart a VirtualMachine object.
*DefaultApi* | [**test**](docs/DefaultApi.md#test) | **GET** /apis/subresources.kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name}/test | Test endpoint verifying apiserver connectivity.
*DefaultApi* | [**version**](docs/DefaultApi.md#version) | **GET** /apis/subresources.kubevirt.io/v1alpha2/version | 
*DefaultApi* | [**vnc**](docs/DefaultApi.md#vnc) | **GET** /apis/subresources.kubevirt.io/v1alpha2/namespaces/{namespace}/virtualmachineinstances/{name}/vnc | Open a websocket connection to connect to VNC on the specified VirtualMachineInstance.
*DefaultApi* | [**watch_namespaced_virtual_machine**](docs/DefaultApi.md#watch_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha2/watch/namespaces/{namespace}/virtualmachines | Watch a VirtualMachine object.
*DefaultApi* | [**watch_namespaced_virtual_machine_instance**](docs/DefaultApi.md#watch_namespaced_virtual_machine_instance) | **GET** /apis/kubevirt.io/v1alpha2/watch/namespaces/{namespace}/virtualmachineinstances | Watch a VirtualMachineInstance object.
*DefaultApi* | [**watch_namespaced_virtual_machine_instance_migration**](docs/DefaultApi.md#watch_namespaced_virtual_machine_instance_migration) | **GET** /apis/kubevirt.io/v1alpha2/watch/namespaces/{namespace}/virtualmachineinstancemigrations | Watch a VirtualMachineInstanceMigration object.
*DefaultApi* | [**watch_namespaced_virtual_machine_instance_preset**](docs/DefaultApi.md#watch_namespaced_virtual_machine_instance_preset) | **GET** /apis/kubevirt.io/v1alpha2/watch/namespaces/{namespace}/virtualmachineinstancepresets | Watch a VirtualMachineInstancePreset object.
*DefaultApi* | [**watch_namespaced_virtual_machine_instance_replica_set**](docs/DefaultApi.md#watch_namespaced_virtual_machine_instance_replica_set) | **GET** /apis/kubevirt.io/v1alpha2/watch/namespaces/{namespace}/virtualmachineinstancereplicasets | Watch a VirtualMachineInstanceReplicaSet object.
*DefaultApi* | [**watch_virtual_machine_instance_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_instance_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/watch/virtualmachineinstances | Watch a VirtualMachineInstanceList object.
*DefaultApi* | [**watch_virtual_machine_instance_migration_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_instance_migration_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/watch/virtualmachineinstancemigrations | Watch a VirtualMachineInstanceMigrationList object.
*DefaultApi* | [**watch_virtual_machine_instance_preset_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_instance_preset_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/watch/virtualmachineinstancepresets | Watch a VirtualMachineInstancePresetList object.
*DefaultApi* | [**watch_virtual_machine_instance_replica_set_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_instance_replica_set_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/watch/virtualmachineinstancereplicasets | Watch a VirtualMachineInstanceReplicaSetList object.
*DefaultApi* | [**watch_virtual_machine_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha2/watch/virtualmachines | Watch a VirtualMachineList object.


## Documentation For Models

 - [V1APIGroup](docs/V1APIGroup.md)
 - [V1APIGroupList](docs/V1APIGroupList.md)
 - [V1APIResource](docs/V1APIResource.md)
 - [V1APIResourceList](docs/V1APIResourceList.md)
 - [V1Affinity](docs/V1Affinity.md)
 - [V1CDRomTarget](docs/V1CDRomTarget.md)
 - [V1CPU](docs/V1CPU.md)
 - [V1Clock](docs/V1Clock.md)
 - [V1ClockOffsetUTC](docs/V1ClockOffsetUTC.md)
 - [V1CloudInitNoCloudSource](docs/V1CloudInitNoCloudSource.md)
 - [V1CniNetwork](docs/V1CniNetwork.md)
 - [V1ConfigMapVolumeSource](docs/V1ConfigMapVolumeSource.md)
 - [V1ContainerDiskSource](docs/V1ContainerDiskSource.md)
 - [V1DHCPOptions](docs/V1DHCPOptions.md)
 - [V1DataVolumeSource](docs/V1DataVolumeSource.md)
 - [V1DeleteOptions](docs/V1DeleteOptions.md)
 - [V1Devices](docs/V1Devices.md)
 - [V1Disk](docs/V1Disk.md)
 - [V1DiskTarget](docs/V1DiskTarget.md)
 - [V1DomainSpec](docs/V1DomainSpec.md)
 - [V1EmptyDiskSource](docs/V1EmptyDiskSource.md)
 - [V1EphemeralVolumeSource](docs/V1EphemeralVolumeSource.md)
 - [V1FeatureAPIC](docs/V1FeatureAPIC.md)
 - [V1FeatureHyperv](docs/V1FeatureHyperv.md)
 - [V1FeatureSpinlocks](docs/V1FeatureSpinlocks.md)
 - [V1FeatureState](docs/V1FeatureState.md)
 - [V1FeatureVendorID](docs/V1FeatureVendorID.md)
 - [V1Features](docs/V1Features.md)
 - [V1Firmware](docs/V1Firmware.md)
 - [V1FloppyTarget](docs/V1FloppyTarget.md)
 - [V1GroupVersionForDiscovery](docs/V1GroupVersionForDiscovery.md)
 - [V1HPETTimer](docs/V1HPETTimer.md)
 - [V1HTTPGetAction](docs/V1HTTPGetAction.md)
 - [V1HTTPHeader](docs/V1HTTPHeader.md)
 - [V1HostDisk](docs/V1HostDisk.md)
 - [V1Hugepages](docs/V1Hugepages.md)
 - [V1HypervTimer](docs/V1HypervTimer.md)
 - [V1I6300ESBWatchdog](docs/V1I6300ESBWatchdog.md)
 - [V1Initializer](docs/V1Initializer.md)
 - [V1Initializers](docs/V1Initializers.md)
 - [V1Interface](docs/V1Interface.md)
 - [V1KVMTimer](docs/V1KVMTimer.md)
 - [V1LabelSelector](docs/V1LabelSelector.md)
 - [V1LabelSelectorRequirement](docs/V1LabelSelectorRequirement.md)
 - [V1ListMeta](docs/V1ListMeta.md)
 - [V1LocalObjectReference](docs/V1LocalObjectReference.md)
 - [V1LunTarget](docs/V1LunTarget.md)
 - [V1Machine](docs/V1Machine.md)
 - [V1Memory](docs/V1Memory.md)
 - [V1Network](docs/V1Network.md)
 - [V1NodeAffinity](docs/V1NodeAffinity.md)
 - [V1NodeSelector](docs/V1NodeSelector.md)
 - [V1NodeSelectorRequirement](docs/V1NodeSelectorRequirement.md)
 - [V1NodeSelectorTerm](docs/V1NodeSelectorTerm.md)
 - [V1ObjectMeta](docs/V1ObjectMeta.md)
 - [V1OwnerReference](docs/V1OwnerReference.md)
 - [V1PITTimer](docs/V1PITTimer.md)
 - [V1PersistentVolumeClaimSpec](docs/V1PersistentVolumeClaimSpec.md)
 - [V1PersistentVolumeClaimVolumeSource](docs/V1PersistentVolumeClaimVolumeSource.md)
 - [V1PodAffinity](docs/V1PodAffinity.md)
 - [V1PodAffinityTerm](docs/V1PodAffinityTerm.md)
 - [V1PodAntiAffinity](docs/V1PodAntiAffinity.md)
 - [V1PodNetwork](docs/V1PodNetwork.md)
 - [V1Port](docs/V1Port.md)
 - [V1Preconditions](docs/V1Preconditions.md)
 - [V1PreferredSchedulingTerm](docs/V1PreferredSchedulingTerm.md)
 - [V1Probe](docs/V1Probe.md)
 - [V1RTCTimer](docs/V1RTCTimer.md)
 - [V1ResourceRequirements](docs/V1ResourceRequirements.md)
 - [V1SecretVolumeSource](docs/V1SecretVolumeSource.md)
 - [V1ServerAddressByClientCIDR](docs/V1ServerAddressByClientCIDR.md)
 - [V1ServiceAccountVolumeSource](docs/V1ServiceAccountVolumeSource.md)
 - [V1Status](docs/V1Status.md)
 - [V1StatusCause](docs/V1StatusCause.md)
 - [V1StatusDetails](docs/V1StatusDetails.md)
 - [V1TCPSocketAction](docs/V1TCPSocketAction.md)
 - [V1Timer](docs/V1Timer.md)
 - [V1Toleration](docs/V1Toleration.md)
 - [V1VirtualMachine](docs/V1VirtualMachine.md)
 - [V1VirtualMachineCondition](docs/V1VirtualMachineCondition.md)
 - [V1VirtualMachineInstance](docs/V1VirtualMachineInstance.md)
 - [V1VirtualMachineInstanceCondition](docs/V1VirtualMachineInstanceCondition.md)
 - [V1VirtualMachineInstanceList](docs/V1VirtualMachineInstanceList.md)
 - [V1VirtualMachineInstanceMigration](docs/V1VirtualMachineInstanceMigration.md)
 - [V1VirtualMachineInstanceMigrationList](docs/V1VirtualMachineInstanceMigrationList.md)
 - [V1VirtualMachineInstanceMigrationSpec](docs/V1VirtualMachineInstanceMigrationSpec.md)
 - [V1VirtualMachineInstanceMigrationState](docs/V1VirtualMachineInstanceMigrationState.md)
 - [V1VirtualMachineInstanceMigrationStatus](docs/V1VirtualMachineInstanceMigrationStatus.md)
 - [V1VirtualMachineInstanceNetworkInterface](docs/V1VirtualMachineInstanceNetworkInterface.md)
 - [V1VirtualMachineInstancePreset](docs/V1VirtualMachineInstancePreset.md)
 - [V1VirtualMachineInstancePresetList](docs/V1VirtualMachineInstancePresetList.md)
 - [V1VirtualMachineInstancePresetSpec](docs/V1VirtualMachineInstancePresetSpec.md)
 - [V1VirtualMachineInstanceReplicaSet](docs/V1VirtualMachineInstanceReplicaSet.md)
 - [V1VirtualMachineInstanceReplicaSetCondition](docs/V1VirtualMachineInstanceReplicaSetCondition.md)
 - [V1VirtualMachineInstanceReplicaSetList](docs/V1VirtualMachineInstanceReplicaSetList.md)
 - [V1VirtualMachineInstanceReplicaSetSpec](docs/V1VirtualMachineInstanceReplicaSetSpec.md)
 - [V1VirtualMachineInstanceReplicaSetStatus](docs/V1VirtualMachineInstanceReplicaSetStatus.md)
 - [V1VirtualMachineInstanceSpec](docs/V1VirtualMachineInstanceSpec.md)
 - [V1VirtualMachineInstanceStatus](docs/V1VirtualMachineInstanceStatus.md)
 - [V1VirtualMachineInstanceTemplateSpec](docs/V1VirtualMachineInstanceTemplateSpec.md)
 - [V1VirtualMachineList](docs/V1VirtualMachineList.md)
 - [V1VirtualMachineSpec](docs/V1VirtualMachineSpec.md)
 - [V1VirtualMachineStatus](docs/V1VirtualMachineStatus.md)
 - [V1Volume](docs/V1Volume.md)
 - [V1WatchEvent](docs/V1WatchEvent.md)
 - [V1Watchdog](docs/V1Watchdog.md)
 - [V1WeightedPodAffinityTerm](docs/V1WeightedPodAffinityTerm.md)
 - [V1alpha1DataVolume](docs/V1alpha1DataVolume.md)
 - [V1alpha1DataVolumeSource](docs/V1alpha1DataVolumeSource.md)
 - [V1alpha1DataVolumeSourceHTTP](docs/V1alpha1DataVolumeSourceHTTP.md)
 - [V1alpha1DataVolumeSourcePVC](docs/V1alpha1DataVolumeSourcePVC.md)
 - [V1alpha1DataVolumeSourceS3](docs/V1alpha1DataVolumeSourceS3.md)
 - [V1alpha1DataVolumeSpec](docs/V1alpha1DataVolumeSpec.md)
 - [V1alpha1DataVolumeStatus](docs/V1alpha1DataVolumeStatus.md)


## Documentation For Authorization


## BearerToken

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author

kubevirt-dev@googlegroups.com

