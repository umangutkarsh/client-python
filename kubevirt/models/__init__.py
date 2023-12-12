# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .k8s_io_api_core_v1_affinity import K8sIoApiCoreV1Affinity
from .k8s_io_api_core_v1_downward_api_volume_file import K8sIoApiCoreV1DownwardAPIVolumeFile
from .k8s_io_api_core_v1_exec_action import K8sIoApiCoreV1ExecAction
from .k8s_io_api_core_v1_http_get_action import K8sIoApiCoreV1HTTPGetAction
from .k8s_io_api_core_v1_http_header import K8sIoApiCoreV1HTTPHeader
from .k8s_io_api_core_v1_local_object_reference import K8sIoApiCoreV1LocalObjectReference
from .k8s_io_api_core_v1_node_affinity import K8sIoApiCoreV1NodeAffinity
from .k8s_io_api_core_v1_node_selector import K8sIoApiCoreV1NodeSelector
from .k8s_io_api_core_v1_node_selector_requirement import K8sIoApiCoreV1NodeSelectorRequirement
from .k8s_io_api_core_v1_node_selector_term import K8sIoApiCoreV1NodeSelectorTerm
from .k8s_io_api_core_v1_object_field_selector import K8sIoApiCoreV1ObjectFieldSelector
from .k8s_io_api_core_v1_persistent_volume_claim_spec import K8sIoApiCoreV1PersistentVolumeClaimSpec
from .k8s_io_api_core_v1_persistent_volume_claim_volume_source import K8sIoApiCoreV1PersistentVolumeClaimVolumeSource
from .k8s_io_api_core_v1_pod_affinity import K8sIoApiCoreV1PodAffinity
from .k8s_io_api_core_v1_pod_affinity_term import K8sIoApiCoreV1PodAffinityTerm
from .k8s_io_api_core_v1_pod_anti_affinity import K8sIoApiCoreV1PodAntiAffinity
from .k8s_io_api_core_v1_pod_dns_config import K8sIoApiCoreV1PodDNSConfig
from .k8s_io_api_core_v1_pod_dns_config_option import K8sIoApiCoreV1PodDNSConfigOption
from .k8s_io_api_core_v1_preferred_scheduling_term import K8sIoApiCoreV1PreferredSchedulingTerm
from .k8s_io_api_core_v1_resource_claim import K8sIoApiCoreV1ResourceClaim
from .k8s_io_api_core_v1_resource_field_selector import K8sIoApiCoreV1ResourceFieldSelector
from .k8s_io_api_core_v1_resource_requirements import K8sIoApiCoreV1ResourceRequirements
from .k8s_io_api_core_v1_tcp_socket_action import K8sIoApiCoreV1TCPSocketAction
from .k8s_io_api_core_v1_toleration import K8sIoApiCoreV1Toleration
from .k8s_io_api_core_v1_topology_spread_constraint import K8sIoApiCoreV1TopologySpreadConstraint
from .k8s_io_api_core_v1_typed_local_object_reference import K8sIoApiCoreV1TypedLocalObjectReference
from .k8s_io_api_core_v1_typed_object_reference import K8sIoApiCoreV1TypedObjectReference
from .k8s_io_api_core_v1_weighted_pod_affinity_term import K8sIoApiCoreV1WeightedPodAffinityTerm
from .k8s_io_apimachinery_pkg_api_resource_quantity import K8sIoApimachineryPkgApiResourceQuantity
from .k8s_io_apimachinery_pkg_apis_meta_v1_api_group import K8sIoApimachineryPkgApisMetaV1APIGroup
from .k8s_io_apimachinery_pkg_apis_meta_v1_api_group_list import K8sIoApimachineryPkgApisMetaV1APIGroupList
from .k8s_io_apimachinery_pkg_apis_meta_v1_api_resource import K8sIoApimachineryPkgApisMetaV1APIResource
from .k8s_io_apimachinery_pkg_apis_meta_v1_api_resource_list import K8sIoApimachineryPkgApisMetaV1APIResourceList
from .k8s_io_apimachinery_pkg_apis_meta_v1_delete_options import K8sIoApimachineryPkgApisMetaV1DeleteOptions
from .k8s_io_apimachinery_pkg_apis_meta_v1_duration import K8sIoApimachineryPkgApisMetaV1Duration
from .k8s_io_apimachinery_pkg_apis_meta_v1_fields_v1 import K8sIoApimachineryPkgApisMetaV1FieldsV1
from .k8s_io_apimachinery_pkg_apis_meta_v1_group_version_for_discovery import K8sIoApimachineryPkgApisMetaV1GroupVersionForDiscovery
from .k8s_io_apimachinery_pkg_apis_meta_v1_label_selector import K8sIoApimachineryPkgApisMetaV1LabelSelector
from .k8s_io_apimachinery_pkg_apis_meta_v1_label_selector_requirement import K8sIoApimachineryPkgApisMetaV1LabelSelectorRequirement
from .k8s_io_apimachinery_pkg_apis_meta_v1_list_meta import K8sIoApimachineryPkgApisMetaV1ListMeta
from .k8s_io_apimachinery_pkg_apis_meta_v1_managed_fields_entry import K8sIoApimachineryPkgApisMetaV1ManagedFieldsEntry
from .k8s_io_apimachinery_pkg_apis_meta_v1_object_meta import K8sIoApimachineryPkgApisMetaV1ObjectMeta
from .k8s_io_apimachinery_pkg_apis_meta_v1_owner_reference import K8sIoApimachineryPkgApisMetaV1OwnerReference
from .k8s_io_apimachinery_pkg_apis_meta_v1_patch import K8sIoApimachineryPkgApisMetaV1Patch
from .k8s_io_apimachinery_pkg_apis_meta_v1_preconditions import K8sIoApimachineryPkgApisMetaV1Preconditions
from .k8s_io_apimachinery_pkg_apis_meta_v1_root_paths import K8sIoApimachineryPkgApisMetaV1RootPaths
from .k8s_io_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr import K8sIoApimachineryPkgApisMetaV1ServerAddressByClientCIDR
from .k8s_io_apimachinery_pkg_apis_meta_v1_status import K8sIoApimachineryPkgApisMetaV1Status
from .k8s_io_apimachinery_pkg_apis_meta_v1_status_cause import K8sIoApimachineryPkgApisMetaV1StatusCause
from .k8s_io_apimachinery_pkg_apis_meta_v1_status_details import K8sIoApimachineryPkgApisMetaV1StatusDetails
from .k8s_io_apimachinery_pkg_apis_meta_v1_time import K8sIoApimachineryPkgApisMetaV1Time
from .k8s_io_apimachinery_pkg_apis_meta_v1_watch_event import K8sIoApimachineryPkgApisMetaV1WatchEvent
from .k8s_io_apimachinery_pkg_runtime_raw_extension import K8sIoApimachineryPkgRuntimeRawExtension
from .k8s_io_apimachinery_pkg_util_intstr_int_or_string import K8sIoApimachineryPkgUtilIntstrIntOrString
from .v1_acpi import V1ACPI
from .v1_access_credential import V1AccessCredential
from .v1_access_credential_secret_source import V1AccessCredentialSecretSource
from .v1_add_volume_options import V1AddVolumeOptions
from .v1_arch_configuration import V1ArchConfiguration
from .v1_arch_specific_configuration import V1ArchSpecificConfiguration
from .v1_bios import V1BIOS
from .v1_block_size import V1BlockSize
from .v1_bootloader import V1Bootloader
from .v1_cd_rom_target import V1CDRomTarget
from .v1_cpu import V1CPU
from .v1_cpu_feature import V1CPUFeature
from .v1_cpu_topology import V1CPUTopology
from .v1_cert_config import V1CertConfig
from .v1_chassis import V1Chassis
from .v1_client_passthrough_devices import V1ClientPassthroughDevices
from .v1_clock import V1Clock
from .v1_clock_offset import V1ClockOffset
from .v1_clock_offset_utc import V1ClockOffsetUTC
from .v1_cloud_init_config_drive_source import V1CloudInitConfigDriveSource
from .v1_cloud_init_no_cloud_source import V1CloudInitNoCloudSource
from .v1_component_config import V1ComponentConfig
from .v1_config_drive_ssh_public_key_access_credential_propagation import V1ConfigDriveSSHPublicKeyAccessCredentialPropagation
from .v1_config_map_volume_source import V1ConfigMapVolumeSource
from .v1_container_disk_info import V1ContainerDiskInfo
from .v1_container_disk_source import V1ContainerDiskSource
from .v1_custom_block_size import V1CustomBlockSize
from .v1_custom_profile import V1CustomProfile
from .v1_customize_components import V1CustomizeComponents
from .v1_customize_components_patch import V1CustomizeComponentsPatch
from .v1_dhcp_options import V1DHCPOptions
from .v1_dhcp_private_options import V1DHCPPrivateOptions
from .v1_data_volume_source import V1DataVolumeSource
from .v1_data_volume_template_dummy_status import V1DataVolumeTemplateDummyStatus
from .v1_data_volume_template_spec import V1DataVolumeTemplateSpec
from .v1_developer_configuration import V1DeveloperConfiguration
from .v1_devices import V1Devices
from .v1_disable_free_page_reporting import V1DisableFreePageReporting
from .v1_disable_serial_console_log import V1DisableSerialConsoleLog
from .v1_disk import V1Disk
from .v1_disk_target import V1DiskTarget
from .v1_disk_verification import V1DiskVerification
from .v1_domain_memory_dump_info import V1DomainMemoryDumpInfo
from .v1_domain_spec import V1DomainSpec
from .v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from .v1_downward_metrics import V1DownwardMetrics
from .v1_downward_metrics_volume_source import V1DownwardMetricsVolumeSource
from .v1_efi import V1EFI
from .v1_empty_disk_source import V1EmptyDiskSource
from .v1_ephemeral_volume_source import V1EphemeralVolumeSource
from .v1_feature_apic import V1FeatureAPIC
from .v1_feature_hyperv import V1FeatureHyperv
from .v1_feature_kvm import V1FeatureKVM
from .v1_feature_spinlocks import V1FeatureSpinlocks
from .v1_feature_state import V1FeatureState
from .v1_feature_vendor_id import V1FeatureVendorID
from .v1_features import V1Features
from .v1_filesystem import V1Filesystem
from .v1_filesystem_virtiofs import V1FilesystemVirtiofs
from .v1_firmware import V1Firmware
from .v1_flags import V1Flags
from .v1_freeze_unfreeze_timeout import V1FreezeUnfreezeTimeout
from .v1_gpu import V1GPU
from .v1_generation_status import V1GenerationStatus
from .v1_guest_agent_command_info import V1GuestAgentCommandInfo
from .v1_guest_agent_ping import V1GuestAgentPing
from .v1_hpet_timer import V1HPETTimer
from .v1_host_device import V1HostDevice
from .v1_host_disk import V1HostDisk
from .v1_hotplug_volume_source import V1HotplugVolumeSource
from .v1_hotplug_volume_status import V1HotplugVolumeStatus
from .v1_hugepages import V1Hugepages
from .v1_hyperv_timer import V1HypervTimer
from .v1_i6300_esb_watchdog import V1I6300ESBWatchdog
from .v1_initrd_info import V1InitrdInfo
from .v1_input import V1Input
from .v1_instancetype_matcher import V1InstancetypeMatcher
from .v1_interface import V1Interface
from .v1_interface_binding_plugin import V1InterfaceBindingPlugin
from .v1_interface_bridge import V1InterfaceBridge
from .v1_interface_macvtap import V1InterfaceMacvtap
from .v1_interface_masquerade import V1InterfaceMasquerade
from .v1_interface_passt import V1InterfacePasst
from .v1_interface_sriov import V1InterfaceSRIOV
from .v1_interface_slirp import V1InterfaceSlirp
from .v1_ksm_configuration import V1KSMConfiguration
from .v1_kvm_timer import V1KVMTimer
from .v1_kernel_boot import V1KernelBoot
from .v1_kernel_boot_container import V1KernelBootContainer
from .v1_kernel_boot_status import V1KernelBootStatus
from .v1_kernel_info import V1KernelInfo
from .v1_kube_virt import V1KubeVirt
from .v1_kube_virt_certificate_rotate_strategy import V1KubeVirtCertificateRotateStrategy
from .v1_kube_virt_condition import V1KubeVirtCondition
from .v1_kube_virt_configuration import V1KubeVirtConfiguration
from .v1_kube_virt_list import V1KubeVirtList
from .v1_kube_virt_self_sign_configuration import V1KubeVirtSelfSignConfiguration
from .v1_kube_virt_spec import V1KubeVirtSpec
from .v1_kube_virt_status import V1KubeVirtStatus
from .v1_kube_virt_workload_update_strategy import V1KubeVirtWorkloadUpdateStrategy
from .v1_launch_security import V1LaunchSecurity
from .v1_live_update_affinity import V1LiveUpdateAffinity
from .v1_live_update_cpu import V1LiveUpdateCPU
from .v1_live_update_configuration import V1LiveUpdateConfiguration
from .v1_live_update_features import V1LiveUpdateFeatures
from .v1_live_update_memory import V1LiveUpdateMemory
from .v1_log_verbosity import V1LogVerbosity
from .v1_lun_target import V1LunTarget
from .v1_machine import V1Machine
from .v1_mediated_devices_configuration import V1MediatedDevicesConfiguration
from .v1_mediated_host_device import V1MediatedHostDevice
from .v1_memory import V1Memory
from .v1_memory_dump_volume_source import V1MemoryDumpVolumeSource
from .v1_memory_status import V1MemoryStatus
from .v1_migrate_options import V1MigrateOptions
from .v1_migration_configuration import V1MigrationConfiguration
from .v1_multus_network import V1MultusNetwork
from .v1_numa import V1NUMA
from .v1_numa_guest_mapping_passthrough import V1NUMAGuestMappingPassthrough
from .v1_network import V1Network
from .v1_network_configuration import V1NetworkConfiguration
from .v1_no_cloud_ssh_public_key_access_credential_propagation import V1NoCloudSSHPublicKeyAccessCredentialPropagation
from .v1_node_mediated_device_types_config import V1NodeMediatedDeviceTypesConfig
from .v1_node_placement import V1NodePlacement
from .v1_pit_timer import V1PITTimer
from .v1_pause_options import V1PauseOptions
from .v1_pci_host_device import V1PciHostDevice
from .v1_permitted_host_devices import V1PermittedHostDevices
from .v1_persistent_volume_claim_info import V1PersistentVolumeClaimInfo
from .v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from .v1_plugin_binding import V1PluginBinding
from .v1_pod_network import V1PodNetwork
from .v1_port import V1Port
from .v1_preference_matcher import V1PreferenceMatcher
from .v1_probe import V1Probe
from .v1_qemu_guest_agent_ssh_public_key_access_credential_propagation import V1QemuGuestAgentSSHPublicKeyAccessCredentialPropagation
from .v1_qemu_guest_agent_user_password_access_credential_propagation import V1QemuGuestAgentUserPasswordAccessCredentialPropagation
from .v1_rest_client_configuration import V1RESTClientConfiguration
from .v1_rtc_timer import V1RTCTimer
from .v1_rate_limiter import V1RateLimiter
from .v1_realtime import V1Realtime
from .v1_reloadable_component_configuration import V1ReloadableComponentConfiguration
from .v1_remove_volume_options import V1RemoveVolumeOptions
from .v1_resource_requirements import V1ResourceRequirements
from .v1_restart_options import V1RestartOptions
from .v1_rng import V1Rng
from .v1_sev import V1SEV
from .v1_sev_attestation import V1SEVAttestation
from .v1_sev_measurement_info import V1SEVMeasurementInfo
from .v1_sev_platform_info import V1SEVPlatformInfo
from .v1_sev_policy import V1SEVPolicy
from .v1_sev_secret_options import V1SEVSecretOptions
from .v1_sev_session_options import V1SEVSessionOptions
from .v1_sm_bios_configuration import V1SMBiosConfiguration
from .v1_ssh_public_key_access_credential import V1SSHPublicKeyAccessCredential
from .v1_ssh_public_key_access_credential_propagation_method import V1SSHPublicKeyAccessCredentialPropagationMethod
from .v1_ssh_public_key_access_credential_source import V1SSHPublicKeyAccessCredentialSource
from .v1_seccomp_configuration import V1SeccompConfiguration
from .v1_secret_volume_source import V1SecretVolumeSource
from .v1_service_account_volume_source import V1ServiceAccountVolumeSource
from .v1_sound_device import V1SoundDevice
from .v1_start_options import V1StartOptions
from .v1_stop_options import V1StopOptions
from .v1_support_container_resources import V1SupportContainerResources
from .v1_sy_nic_timer import V1SyNICTimer
from .v1_sysprep_source import V1SysprepSource
from .v1_tls_configuration import V1TLSConfiguration
from .v1_tpm_device import V1TPMDevice
from .v1_timer import V1Timer
from .v1_token_bucket_rate_limiter import V1TokenBucketRateLimiter
from .v1_topology_hints import V1TopologyHints
from .v1_usb_host_device import V1USBHostDevice
from .v1_usb_selector import V1USBSelector
from .v1_unpause_options import V1UnpauseOptions
from .v1_user_password_access_credential import V1UserPasswordAccessCredential
from .v1_user_password_access_credential_propagation_method import V1UserPasswordAccessCredentialPropagationMethod
from .v1_user_password_access_credential_source import V1UserPasswordAccessCredentialSource
from .v1_vgpu_display_options import V1VGPUDisplayOptions
from .v1_vgpu_options import V1VGPUOptions
from .v1_virtual_machine import V1VirtualMachine
from .v1_virtual_machine_condition import V1VirtualMachineCondition
from .v1_virtual_machine_instance import V1VirtualMachineInstance
from .v1_virtual_machine_instance_condition import V1VirtualMachineInstanceCondition
from .v1_virtual_machine_instance_file_system import V1VirtualMachineInstanceFileSystem
from .v1_virtual_machine_instance_file_system_info import V1VirtualMachineInstanceFileSystemInfo
from .v1_virtual_machine_instance_file_system_list import V1VirtualMachineInstanceFileSystemList
from .v1_virtual_machine_instance_guest_agent_info import V1VirtualMachineInstanceGuestAgentInfo
from .v1_virtual_machine_instance_guest_os_info import V1VirtualMachineInstanceGuestOSInfo
from .v1_virtual_machine_instance_guest_os_user import V1VirtualMachineInstanceGuestOSUser
from .v1_virtual_machine_instance_guest_os_user_list import V1VirtualMachineInstanceGuestOSUserList
from .v1_virtual_machine_instance_list import V1VirtualMachineInstanceList
from .v1_virtual_machine_instance_migration import V1VirtualMachineInstanceMigration
from .v1_virtual_machine_instance_migration_condition import V1VirtualMachineInstanceMigrationCondition
from .v1_virtual_machine_instance_migration_list import V1VirtualMachineInstanceMigrationList
from .v1_virtual_machine_instance_migration_phase_transition_timestamp import V1VirtualMachineInstanceMigrationPhaseTransitionTimestamp
from .v1_virtual_machine_instance_migration_spec import V1VirtualMachineInstanceMigrationSpec
from .v1_virtual_machine_instance_migration_state import V1VirtualMachineInstanceMigrationState
from .v1_virtual_machine_instance_migration_status import V1VirtualMachineInstanceMigrationStatus
from .v1_virtual_machine_instance_network_interface import V1VirtualMachineInstanceNetworkInterface
from .v1_virtual_machine_instance_phase_transition_timestamp import V1VirtualMachineInstancePhaseTransitionTimestamp
from .v1_virtual_machine_instance_preset import V1VirtualMachineInstancePreset
from .v1_virtual_machine_instance_preset_list import V1VirtualMachineInstancePresetList
from .v1_virtual_machine_instance_preset_spec import V1VirtualMachineInstancePresetSpec
from .v1_virtual_machine_instance_profile import V1VirtualMachineInstanceProfile
from .v1_virtual_machine_instance_replica_set import V1VirtualMachineInstanceReplicaSet
from .v1_virtual_machine_instance_replica_set_condition import V1VirtualMachineInstanceReplicaSetCondition
from .v1_virtual_machine_instance_replica_set_list import V1VirtualMachineInstanceReplicaSetList
from .v1_virtual_machine_instance_replica_set_spec import V1VirtualMachineInstanceReplicaSetSpec
from .v1_virtual_machine_instance_replica_set_status import V1VirtualMachineInstanceReplicaSetStatus
from .v1_virtual_machine_instance_spec import V1VirtualMachineInstanceSpec
from .v1_virtual_machine_instance_status import V1VirtualMachineInstanceStatus
from .v1_virtual_machine_instance_template_spec import V1VirtualMachineInstanceTemplateSpec
from .v1_virtual_machine_list import V1VirtualMachineList
from .v1_virtual_machine_memory_dump_request import V1VirtualMachineMemoryDumpRequest
from .v1_virtual_machine_options import V1VirtualMachineOptions
from .v1_virtual_machine_spec import V1VirtualMachineSpec
from .v1_virtual_machine_start_failure import V1VirtualMachineStartFailure
from .v1_virtual_machine_state_change_request import V1VirtualMachineStateChangeRequest
from .v1_virtual_machine_status import V1VirtualMachineStatus
from .v1_virtual_machine_volume_request import V1VirtualMachineVolumeRequest
from .v1_volume import V1Volume
from .v1_volume_snapshot_status import V1VolumeSnapshotStatus
from .v1_volume_status import V1VolumeStatus
from .v1_watchdog import V1Watchdog
from .v1alpha1_condition import V1alpha1Condition
from .v1alpha1_error import V1alpha1Error
from .v1alpha1_migration_policy import V1alpha1MigrationPolicy
from .v1alpha1_migration_policy_list import V1alpha1MigrationPolicyList
from .v1alpha1_migration_policy_spec import V1alpha1MigrationPolicySpec
from .v1alpha1_migration_policy_status import V1alpha1MigrationPolicyStatus
from .v1alpha1_persistent_volume_claim import V1alpha1PersistentVolumeClaim
from .v1alpha1_selectors import V1alpha1Selectors
from .v1alpha1_snapshot_volumes_lists import V1alpha1SnapshotVolumesLists
from .v1alpha1_source_spec import V1alpha1SourceSpec
from .v1alpha1_virtual_machine import V1alpha1VirtualMachine
from .v1alpha1_virtual_machine_clone import V1alpha1VirtualMachineClone
from .v1alpha1_virtual_machine_clone_list import V1alpha1VirtualMachineCloneList
from .v1alpha1_virtual_machine_clone_spec import V1alpha1VirtualMachineCloneSpec
from .v1alpha1_virtual_machine_clone_status import V1alpha1VirtualMachineCloneStatus
from .v1alpha1_virtual_machine_clone_template_filters import V1alpha1VirtualMachineCloneTemplateFilters
from .v1alpha1_virtual_machine_export import V1alpha1VirtualMachineExport
from .v1alpha1_virtual_machine_export_link import V1alpha1VirtualMachineExportLink
from .v1alpha1_virtual_machine_export_links import V1alpha1VirtualMachineExportLinks
from .v1alpha1_virtual_machine_export_list import V1alpha1VirtualMachineExportList
from .v1alpha1_virtual_machine_export_manifest import V1alpha1VirtualMachineExportManifest
from .v1alpha1_virtual_machine_export_spec import V1alpha1VirtualMachineExportSpec
from .v1alpha1_virtual_machine_export_status import V1alpha1VirtualMachineExportStatus
from .v1alpha1_virtual_machine_export_volume import V1alpha1VirtualMachineExportVolume
from .v1alpha1_virtual_machine_export_volume_format import V1alpha1VirtualMachineExportVolumeFormat
from .v1alpha1_virtual_machine_pool import V1alpha1VirtualMachinePool
from .v1alpha1_virtual_machine_pool_condition import V1alpha1VirtualMachinePoolCondition
from .v1alpha1_virtual_machine_pool_list import V1alpha1VirtualMachinePoolList
from .v1alpha1_virtual_machine_pool_spec import V1alpha1VirtualMachinePoolSpec
from .v1alpha1_virtual_machine_pool_status import V1alpha1VirtualMachinePoolStatus
from .v1alpha1_virtual_machine_restore import V1alpha1VirtualMachineRestore
from .v1alpha1_virtual_machine_restore_list import V1alpha1VirtualMachineRestoreList
from .v1alpha1_virtual_machine_restore_spec import V1alpha1VirtualMachineRestoreSpec
from .v1alpha1_virtual_machine_restore_status import V1alpha1VirtualMachineRestoreStatus
from .v1alpha1_virtual_machine_snapshot import V1alpha1VirtualMachineSnapshot
from .v1alpha1_virtual_machine_snapshot_content import V1alpha1VirtualMachineSnapshotContent
from .v1alpha1_virtual_machine_snapshot_content_list import V1alpha1VirtualMachineSnapshotContentList
from .v1alpha1_virtual_machine_snapshot_content_spec import V1alpha1VirtualMachineSnapshotContentSpec
from .v1alpha1_virtual_machine_snapshot_content_status import V1alpha1VirtualMachineSnapshotContentStatus
from .v1alpha1_virtual_machine_snapshot_list import V1alpha1VirtualMachineSnapshotList
from .v1alpha1_virtual_machine_snapshot_spec import V1alpha1VirtualMachineSnapshotSpec
from .v1alpha1_virtual_machine_snapshot_status import V1alpha1VirtualMachineSnapshotStatus
from .v1alpha1_virtual_machine_template_spec import V1alpha1VirtualMachineTemplateSpec
from .v1alpha1_volume_backup import V1alpha1VolumeBackup
from .v1alpha1_volume_restore import V1alpha1VolumeRestore
from .v1alpha1_volume_snapshot_status import V1alpha1VolumeSnapshotStatus
from .v1beta1_cpu_instancetype import V1beta1CPUInstancetype
from .v1beta1_cpu_preference_requirement import V1beta1CPUPreferenceRequirement
from .v1beta1_cpu_preferences import V1beta1CPUPreferences
from .v1beta1_clock_preferences import V1beta1ClockPreferences
from .v1beta1_data_volume_blank_image import V1beta1DataVolumeBlankImage
from .v1beta1_data_volume_checkpoint import V1beta1DataVolumeCheckpoint
from .v1beta1_data_volume_source import V1beta1DataVolumeSource
from .v1beta1_data_volume_source_gcs import V1beta1DataVolumeSourceGCS
from .v1beta1_data_volume_source_http import V1beta1DataVolumeSourceHTTP
from .v1beta1_data_volume_source_image_io import V1beta1DataVolumeSourceImageIO
from .v1beta1_data_volume_source_pvc import V1beta1DataVolumeSourcePVC
from .v1beta1_data_volume_source_ref import V1beta1DataVolumeSourceRef
from .v1beta1_data_volume_source_registry import V1beta1DataVolumeSourceRegistry
from .v1beta1_data_volume_source_s3 import V1beta1DataVolumeSourceS3
from .v1beta1_data_volume_source_snapshot import V1beta1DataVolumeSourceSnapshot
from .v1beta1_data_volume_source_upload import V1beta1DataVolumeSourceUpload
from .v1beta1_data_volume_source_vddk import V1beta1DataVolumeSourceVDDK
from .v1beta1_data_volume_spec import V1beta1DataVolumeSpec
from .v1beta1_device_preferences import V1beta1DevicePreferences
from .v1beta1_feature_preferences import V1beta1FeaturePreferences
from .v1beta1_firmware_preferences import V1beta1FirmwarePreferences
from .v1beta1_machine_preferences import V1beta1MachinePreferences
from .v1beta1_memory_instancetype import V1beta1MemoryInstancetype
from .v1beta1_memory_preference_requirement import V1beta1MemoryPreferenceRequirement
from .v1beta1_preference_requirements import V1beta1PreferenceRequirements
from .v1beta1_storage_spec import V1beta1StorageSpec
from .v1beta1_virtual_machine_cluster_instancetype import V1beta1VirtualMachineClusterInstancetype
from .v1beta1_virtual_machine_cluster_instancetype_list import V1beta1VirtualMachineClusterInstancetypeList
from .v1beta1_virtual_machine_cluster_preference import V1beta1VirtualMachineClusterPreference
from .v1beta1_virtual_machine_cluster_preference_list import V1beta1VirtualMachineClusterPreferenceList
from .v1beta1_virtual_machine_instancetype import V1beta1VirtualMachineInstancetype
from .v1beta1_virtual_machine_instancetype_list import V1beta1VirtualMachineInstancetypeList
from .v1beta1_virtual_machine_instancetype_spec import V1beta1VirtualMachineInstancetypeSpec
from .v1beta1_virtual_machine_preference import V1beta1VirtualMachinePreference
from .v1beta1_virtual_machine_preference_list import V1beta1VirtualMachinePreferenceList
from .v1beta1_virtual_machine_preference_spec import V1beta1VirtualMachinePreferenceSpec
from .v1beta1_volume_preferences import V1beta1VolumePreferences
from .v1_interface_bridge import V1InterfaceBridge
from .v1_interface_slirp import V1InterfaceSlirp
