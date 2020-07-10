from string import Template
import os


CHUNCK = 1024
ARM_LOGIN_URL = Template(
    "https://www.archive.arm.gov/armlogin/doLogin.jsp?uid=$username&ui=iop"
)

SIPAM_LOCAL_PATH = Template(
    os.path.join(
        '/'.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-1]),
        'datasets/sipam/$year/$month/$day'
    )
)

INSTRUMENT_LOCAL_PATH = Template(
    os.path.join(
        '/'.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-1]),
        'datasets/$instrument/$year/$month/$day'
    )
)

SIPAM_FILENAME = Template('sbmn_cappi_$year$month$day$sep$hour$minute.nc')
SIPAM_FRAME_URL = Template(
    "https://iop.archive.arm.gov/arm-iop/2014/mao/goamazon/T1/schumacher-sband_radar/$year$month$day/?frame=listing&uid=$uid"
)