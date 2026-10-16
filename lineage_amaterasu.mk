#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from device
$(call inherit-product, device/fcnt/amaterasu/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Device identifier. This must come after all inclusions.
PRODUCT_NAME := lineage_amaterasu
PRODUCT_DEVICE := amaterasu
PRODUCT_MANUFACTURER := FCNT
PRODUCT_BRAND := FCNT
PRODUCT_MODEL := F51A

PRODUCT_GMS_CLIENTID_BASE := android-fcnt

PRODUCT_BUILD_PROP_OVERRIDES += \
    DeviceName=F51A \
    BuildDesc="F51A-user 13 V71R051A F51A.20230213 release-keys" \
    BuildFingerprint=DOCOMO/F51A/F51A:12/V71R051A/F51A.20230213:user/release-keys
