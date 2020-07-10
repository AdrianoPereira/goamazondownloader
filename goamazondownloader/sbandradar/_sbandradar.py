import sys; sys.path.insert(0, "/home/adriano/goamazondownloader")
"""S-Band radar data download"""

# Author: Adriano P. Almeida <adriano.almeida@inpe.br>
# License: MIT

from goamazondownloader import (Downloader, warnings, os)
from goamazondownloader.constants import (SIPAM_FILENAME)


class SBandRadar(Downloader):
    def __init__(self, **kwargs) -> None:
        super(SBandRadar, self).__init__(**kwargs)
        self.hour = kwargs.get('hour', None)
        self.minute = kwargs.get('minute', None)

        self.format_date()
        self.format_time()
        super(SBandRadar, self).set_directory(instrument='sbandradar')
        self.set_filename()

    def set_remote_url(self) -> None:
        if self.token is None:
            self.token = self.set_token_access()

    def has_time(self) -> bool:
        return self.hour is not None and self.minute is not None

    def format_time(self) -> None:
        self.hour = str(self.hour).zfill(2) \
            if self.hour is not None else None
        self.minute = str(self.minute).zfill(2) \
            if self.minute is not None else None

    def set_filename(self) -> None:
        if not self.has_date():
            warnings.warn('Date is not complete!', category=UserWarning)
            return
        if not self.has_time():
            warnings.warn('Time is not complete!', category=UserWarning)
            return
        if not self.has_directory():
            self.set_directory()

        self.format_date()
        self.format_time()

        self.filename = os.path.join(self.directory, SIPAM_FILENAME.\
                                     substitute(year=self.year,
                                                month=self.month,
                                                day=self.day,
                                                hour=self.hour,
                                                minute=self.minute,
                                                sep='_'))


if __name__ == "__main__":
    obj = SBandRadar(year=2014, month=2, day=18, hour=15, minute=0)
    # print(obj.directory)
    # print(obj.filename)
    # obj.login("adriano.almeida@inpe.bra")
    obj.download()


