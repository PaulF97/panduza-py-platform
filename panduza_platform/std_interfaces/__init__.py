from .driver_fake_io import DriverFakeIo
from .driver_std_serial import DriverStdSerial
from .driver_platform import DriverPlatform
from .driver_psu_fake import DriverPsuFake

PZA_DRIVERS_LIST=[
    DriverPlatform,
    DriverFakeIo,
    DriverStdSerial,
    DriverPsuFake
]
