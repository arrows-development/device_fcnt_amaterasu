#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sm8250',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_vendor' if partition in ['odm', 'vendor'] else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qti.stats.pdlib',
        'com.qualcomm.qti.dpm.api@1.0',
        'libmmosal',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/hw/vendor.qti.hardware.vibrator.service.fcnt': blob_fixup()
        .replace_needed('android.hardware.vibrator-V1-ndk_platform.so',
                        'android.hardware.vibrator-V1-ndk.so')
        .replace_needed('vendor.qti.hardware.vibrator.impl.so',
                        'vendor.qti.hardware.vibrator.impl_fcnt.so'),
    'vendor/lib64/vendor.qti.hardware.vibrator.impl_fcnt.so': blob_fixup()
        .replace_needed('android.hardware.vibrator-V1-ndk_platform.so',
                        'android.hardware.vibrator-V1-ndk.so'),
    'vendor/etc/init/vendor.qti.hardware.vibrator.service.fcnt.rc': blob_fixup()
        .regex_replace(r'/vendor/bin/hw/vendor\.qti\.hardware\.vibrator\.service',
                       '/vendor/bin/hw/vendor.qti.hardware.vibrator.service.fcnt'),
    'vendor/etc/init/vendor.sensors.sscrpcd.rc': blob_fixup()
        .regex_replace('class early_hal', 'class core'),
    'vendor/lib64/liblgdnnsnpe.so': blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib64/libimagerwrapper.so': blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
	    .sig_replace('9A 0A 00 94', 'E0 03 00 AA'),
    'vendor/lib64/libdpps.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib64/libets_teeclient_v2.so': (
        blob_fixup()
            .remove_needed('libfpsph.so')
            .add_needed('libets_teeclient_v2_shim.so')
    ),
}  # fmt: skip

module = ExtractUtilsModule(
    'amaterasu',
    'fcnt',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
