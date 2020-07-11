import sys; sys.path.insert(0, "/home/adriano/goamazondownloader")
"""Very Low Frequency sensor data download"""

# Author: Adriano P. Almeida <adriano.almeida@inpe.br>
# License: MIT

from goamazondownloader import (Downloader, os, requests as req)
from goamazondownloader.constants import (STARNET_REMOTE_URL, STARNET_FILENAME)
from goamazondownloader._exceptions import *


class VLFSensor(Downloader):
    def __init__(self, **kwargs) -> None:
        super(VLFSensor, self).__init__(**kwargs)
        self.initializer()

    def initializer(self) -> None:
        try:
            if not self.has_date():
                raise DateRequiredError
            self.format_date()
            super(VLFSensor, self).set_directory(instrument='vlfsensor')
            self.set_filename()
        except DateRequiredError as err:
            print(err)

    def set_remote_url(self) -> None:
        try:
            if not self.is_logged():
                raise LoginRequiredError
            if not self.has_date():
                raise DateRequiredError
            file_url = STARNET_REMOTE_URL.substitute(year=self.year,
                                                     month=self.month,
                                                     day=self.day,
                                                     token_access=self.token)
            res = req.get(file_url)
            if res.status_code != 200:
                raise UrlFileNotFoundError
            self.remote_url = file_url
        except LoginRequiredError as err:
            print(err)
        except DateRequiredError as err:
            print(err)
        except UrlFileNotFoundError as err:
            print(err)

    def set_filename(self) -> None:
        try:
            if not self.has_date():
                raise DateRequiredError
            if not self.has_directory():
                self.set_directory()

            self.format_date()
            self.filename = os.path.join(self.directory, STARNET_FILENAME.\
                                         substitute(year=self.year,
                                                    month=self.month,
                                                    day=self.day,
                                                    sep='_'))
        except DateRequiredError as err:
            print(err)


if __name__ == "__main__":
    obj = VLFSensor(year=2014, month=2, day=18)
    obj.login("username")
    obj.set_remote_url()
    obj.download()


