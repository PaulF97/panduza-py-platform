from .driver_platform import DriverPlatform
from .driver_io_fake import DriverIoFake
from .driver_psu_fake import DriverPsuFake
from .driver_file_fake import DriverFileFake
from .driver_reset_fake import DriverResetFake
from .driver_register_fake import DriverRegisterFake

PZA_DRIVERS_LIST=[
    DriverPlatform,
    DriverIoFake,
    DriverPsuFake,
    DriverFileFake,
    DriverResetFake,
    DriverRegisterFake
]
