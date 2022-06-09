from .driver_fake_io import DriverFakeIo
from .driver_std_serial import DriverStdSerial
from .driver_platform import DriverPlatform
from .driver_psu_fake import DriverPsuFake
from .driver_reset_fake import DriverResetFake
from .driver_register_fake import DriverRegisterFake

PZA_DRIVERS_LIST=[
    DriverPlatform,
    DriverFakeIo,
    DriverStdSerial,
    DriverPsuFake,
    DriverResetFake,
    DriverRegisterFake
]
