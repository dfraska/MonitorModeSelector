from enum import IntEnum
import ctypes
from ctypes import windll, byref, Structure, Union, c_uint32, c_int, c_ulong,\
    c_long, c_ushort, c_bool, c_uint, c_uint64

SDC_APPLY = 0x80
QDC_ALL_PATHS = 0x1
QDC_DATABASE_CURRENT = 0x4

class LUID(Structure):
#         typedef struct _LUID {
#           DWORD LowPart;
#           LONG  HighPart;
#         } LUID, *PLUID;
    _fields_ = [
        ("LowPart", c_ulong),
        ("HighPart", c_long)]
 
class DISPLAYCONFIG_PATH_SOURCE_INFO_UNION_STRUCT(Structure):
#         struct {
#           UINT32 cloneGroupId  :16;
#           UINT32 sourceModeInfoIdx  :16;
#         } DUMMYSTRUCTNAME;
    _fields_ = [
        ("cloneGroupId", c_uint32, 16),
        ("sourceModeInfoIdx", c_uint32, 16)]
 
class DISPLAYCONFIG_PATH_SOURCE_INFO_UNION(Union):
#     union {
#       UINT32 modeInfoIdx;
#       struct {
#         UINT32 cloneGroupId  :16;
#         UINT32 sourceModeInfoIdx  :16;
#       } DUMMYSTRUCTNAME;
#     } DUMMYUNIONNAME;
    _fields_ = [
        ("modeInfoIdx", ctypes.c_uint32),
        ("DUMMYSTRUCTNAME", DISPLAYCONFIG_PATH_SOURCE_INFO_UNION_STRUCT)]
 
class DISPLAYCONFIG_PATH_SOURCE_INFO(Structure):
#     typedef struct DISPLAYCONFIG_PATH_SOURCE_INFO {
#       LUID   adapterId;
#       UINT32 id;
#       union {
#         UINT32 modeInfoIdx;
#         struct {
#           UINT32 cloneGroupId  :16;
#           UINT32 sourceModeInfoIdx  :16;
#         } DUMMYSTRUCTNAME;
#       } DUMMYUNIONNAME;
#       UINT32 statusFlags;
#     } DISPLAYCONFIG_PATH_SOURCE_INFO;
    _fields_ = [
        ("adapterId", LUID),
        ("id", c_uint32),
        ("DUMMYUNIONNAME", DISPLAYCONFIG_PATH_SOURCE_INFO_UNION),
        ("statusFlags", c_uint32)]

class DISPLAYCONFIG_PATH_TARGET_INFO_UNION_STRUCT(Structure):
#         struct {
#           UINT32 desktopModeInfoIdx  :16;
#           UINT32 targetModeInfoIdx  :16;
#         };
    _fields_ = [
        ("desktopModeInfoIdx", c_uint32, 16),
        ("targetModeInfoIdx", c_uint32, 16),
        ]
 
class DISPLAYCONFIG_PATH_TARGET_INFO_UNION(Union):
#     union {
#       UINT32 modeInfoIdx;
#       struct {
#         UINT32 desktopModeInfoIdx  :16;
#         UINT32 targetModeInfoIdx  :16;
#       };
#     };
    _fields_ = [
        ("modeInfoIdx", c_uint32),
        ("s", DISPLAYCONFIG_PATH_TARGET_INFO_UNION_STRUCT)
        ]
    pass
 
class DISPLAYCONFIG_PATH_TARGET_INFO(Structure):
#     typedef struct DISPLAYCONFIG_PATH_TARGET_INFO {
#       LUID                                  adapterId;
#       UINT32                                id;
#       union {
#         UINT32 modeInfoIdx;
#         struct {
#           UINT32 desktopModeInfoIdx  :16;
#           UINT32 targetModeInfoIdx  :16;
#         };
#       };
#       DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY outputTechnology;
#       DISPLAYCONFIG_ROTATION                rotation;
#       DISPLAYCONFIG_SCALING                 scaling;
#       DISPLAYCONFIG_RATIONAL                refreshRate;
#       DISPLAYCONFIG_SCANLINE_ORDERING       scanLineOrdering;
#       BOOL                                  targetAvailable;
#       UINT32                                statusFlags;
#     } DISPLAYCONFIG_PATH_TARGET_INFO;
    _fields_ = [
        ("adapterId", LUID),
        ("id", c_uint32),
        ("desktopModeInfoIdx", c_uint32, 16),
        ("targetModeInfoIdx", c_uint32, 16),
        ("output_technology", c_uint32),
        ("rotation", c_uint32),
        ("scaling", c_uint32),
        ("refreshRate", c_uint32),
        ("scanLineOrdering", c_uint32),
        ("targetAvailable", c_bool),
        ("statusFlags", c_uint32)]
 
class DISPLAYCONFIG_PATH_INFO(Structure):
#     typedef struct DISPLAYCONFIG_PATH_INFO {
#       DISPLAYCONFIG_PATH_SOURCE_INFO sourceInfo;
#       DISPLAYCONFIG_PATH_TARGET_INFO targetInfo;
#       UINT32                         flags;
#     } DISPLAYCONFIG_PATH_INFO;
    _fields_ = [
        ("sourceInfo", DISPLAYCONFIG_PATH_SOURCE_INFO),
        ("targetInfo", DISPLAYCONFIG_PATH_TARGET_INFO),
        ("flags", c_uint32)]

class DISPLAYCONFIG_RATIONAL(Structure):
#     typedef struct DISPLAYCONFIG_RATIONAL {
#       UINT32 Numerator;
#       UINT32 Denominator;
#     } DISPLAYCONFIG_RATIONAL;
    _fields_ = [
        ("Numerator", c_uint32),
        ("Denominator", c_uint32)]

class DISPLAYCONFIG_2DREGION(Structure):
#     typedef struct DISPLAYCONFIG_2DREGION {
#       UINT32 cx;
#       UINT32 cy;
#     } DISPLAYCONFIG_2DREGION;
    _fields_ = [
        ("cx", c_uint32),
        ("cy", c_uint32)]

class ADDITIONAL_SIGNAL_INFO(Structure):
#         struct {
#           UINT32 videoStandard  :16;
#           UINT32 vSyncFreqDivider  :6;
#           UINT32 reserved  :10;
#         } AdditionalSignalInfo;
    _fields_ = [
        ("videoStandard", c_uint32, 16),
        ("vSyncFreqDivider", c_uint32, 16),
        ("reserved", c_uint32, 10),]
    
class DISPLAYCONFIG_VIDEO_SIGNAL_INFO_UNION(Union):
#       union {
#         struct {
#           UINT32 videoStandard  :16;
#           UINT32 vSyncFreqDivider  :6;
#           UINT32 reserved  :10;
#         } AdditionalSignalInfo;

#         UINT32 videoStandard;
#       };
    _fields_ = [
        ("AdditionalSignalInfo", ADDITIONAL_SIGNAL_INFO),
        ("videoStandard", c_uint32)]

class DISPLAYCONFIG_VIDEO_SIGNAL_INFO(Structure):
#     typedef struct DISPLAYCONFIG_VIDEO_SIGNAL_INFO {
#       UINT64                          pixelRate;
#       DISPLAYCONFIG_RATIONAL          hSyncFreq;
#       DISPLAYCONFIG_RATIONAL          vSyncFreq;
#       DISPLAYCONFIG_2DREGION          activeSize;
#       DISPLAYCONFIG_2DREGION          totalSize;
#       union {
#         struct {
#           UINT32 videoStandard  :16;
#           UINT32 vSyncFreqDivider  :6;
#           UINT32 reserved  :10;
#         } AdditionalSignalInfo;
#         UINT32 videoStandard;
#       };
#       DISPLAYCONFIG_SCANLINE_ORDERING scanLineOrdering;
#     } DISPLAYCONFIG_VIDEO_SIGNAL_INFO;
    _fields_ = [
        ("pixelRate", c_uint64),
        ("hSyncFreq", DISPLAYCONFIG_RATIONAL),
        ("vSyncFreq", DISPLAYCONFIG_RATIONAL),
        ("activeSize", DISPLAYCONFIG_2DREGION),
        ("totalSize", DISPLAYCONFIG_2DREGION),
        ("u", DISPLAYCONFIG_VIDEO_SIGNAL_INFO_UNION),
        ("scanLineOrdering", c_uint32)]

class DISPLAYCONFIG_TARGET_MODE(Structure):
#     typedef struct DISPLAYCONFIG_TARGET_MODE {
#       DISPLAYCONFIG_VIDEO_SIGNAL_INFO targetVideoSignalInfo;
#     } DISPLAYCONFIG_TARGET_MODE;
    _fields_ = [("targetVideoSignalInfo", DISPLAYCONFIG_VIDEO_SIGNAL_INFO)]

class POINTL(Structure):
#     typedef struct _POINTL {
#       LONG x;
#       LONG y;
#     } POINTL, *PPOINTL;
    _fields_ = [
        ("x", c_long),
        ("y", c_long)]

class DISPLAYCONFIG_SOURCE_MODE(Structure):
#     typedef struct DISPLAYCONFIG_SOURCE_MODE {
#       UINT32                    width;
#       UINT32                    height;
#       DISPLAYCONFIG_PIXELFORMAT pixelFormat;
#       POINTL                    position;
#     } DISPLAYCONFIG_SOURCE_MODE;
    _fields_ = [
        ("width", c_uint32),
        ("height", c_uint32),
        ("pixelFormat", c_uint32),
        ("position", POINTL)]

class RECTL(Structure):
#     typedef struct _RECTL {
#       LONG left;
#       LONG top;
#       LONG right;
#       LONG bottom;
#     } RECTL, *PRECTL;
    _fields_ = [
        ("left", c_long),
        ("top", c_long),
        ("right", c_long),
        ("bottom", c_long),]

class DISPLAYCONFIG_DESKTOP_IMAGE_INFO(Structure):
#     typedef struct DISPLAYCONFIG_DESKTOP_IMAGE_INFO {
#       POINTL PathSourceSize;
#       RECTL  DesktopImageRegion;
#       RECTL  DesktopImageClip;
#     } DISPLAYCONFIG_DESKTOP_IMAGE_INFO;
    _fields_ = [
        ("PathSourceSize", POINTL),
        ("DesktopImageRegion", RECTL),
        ("DesktopImageClip", RECTL),]

class DISPLAYCONFIG_MODE_INFO_UNION(Union):
    _fields_ = [
        ("targetMode", DISPLAYCONFIG_TARGET_MODE),
        ("sourceMode", DISPLAYCONFIG_SOURCE_MODE),
        ("desktopImageInfo", DISPLAYCONFIG_DESKTOP_IMAGE_INFO),]
 
class DISPLAYCONFIG_MODE_INFO(Structure):
#     typedef struct DISPLAYCONFIG_MODE_INFO {
#       DISPLAYCONFIG_MODE_INFO_TYPE infoType;
#       UINT32                       id;
#       LUID                         adapterId;
#       union {
#         DISPLAYCONFIG_TARGET_MODE        targetMode;
#         DISPLAYCONFIG_SOURCE_MODE        sourceMode;
#         DISPLAYCONFIG_DESKTOP_IMAGE_INFO desktopImageInfo;
#       };
#     } DISPLAYCONFIG_MODE_INFO;
    _fields_ = [
        ("infoType", c_uint32),
        ("id", c_uint32),
        ("adapterId", LUID),
        ("u", DISPLAYCONFIG_MODE_INFO_UNION)]

class Mode(IntEnum):
    Extend = 0x4,
    Duplicate = 0x2,
    Internal = 0x8,
    External = 0x1,

# https://stackoverflow.com/questions/6590939/how-to-set-display-settings-to-extend-mode-in-windows-7-using-c
# https://msdn.microsoft.com/en-us/library/windows/hardware/ff569533(v=vs.85).aspx
def set_mode(mode):
    windll.user32.SetDisplayConfig(
        0, None, 0, None, mode | SDC_APPLY)

def get_mode():
    path_array_size = c_uint32()
    mode_array_size = c_uint32()
     
    windll.user32.GetDisplayConfigBufferSizes(
        QDC_ALL_PATHS, byref(path_array_size), byref(mode_array_size))
    
    paths = (DISPLAYCONFIG_PATH_INFO * path_array_size.value)()
    modes = (DISPLAYCONFIG_MODE_INFO * mode_array_size.value)()
    
    current_topology = c_uint32()
    
    windll.user32.QueryDisplayConfig(
        QDC_DATABASE_CURRENT, byref(path_array_size), paths,
        byref(mode_array_size), modes, byref(current_topology))
    
    return Mode(current_topology.value)