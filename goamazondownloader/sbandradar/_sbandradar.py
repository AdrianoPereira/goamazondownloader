import sys; sys.path.insert(0, "/home/adriano/goamazondownloader")
"""S-Band radar data download"""

# Author: Adriano P. Almeida <adriano.almeida@inpe.br>
# License: MIT

from goamazondownloader import (Downloader, os, requests as req, BeautifulSoup,
                                ElementTree as ET)
from goamazondownloader.constants import (SIPAM_FILENAME, SIPAM_FRAME_URL,
                                          ARM_URL_BASE, ARM_LOGIN_URL)
from goamazondownloader._exceptions import *


class SBandRadar(Downloader):
    def __init__(self, **kwargs) -> None:
        super(SBandRadar, self).__init__(**kwargs)
        self.hour = kwargs.get('hour', None)
        self.minute = kwargs.get('minute', None)
        self.initializer()

    def initializer(self) -> None:
        try:
            if not self.has_date():
                raise DateRequiredError
            if not self.has_time():
                raise TimeRequiredError
            self.format_date()
            self.format_time()
            super(SBandRadar, self).set_directory(instrument='sbandradar')
            self.set_filename()
        except DateRequiredError as err:
            print(err)
        except TimeRequiredError as err:
            print(err)

    def set_remote_url(self) -> None:
        try:
            if not self.is_logged():
                raise LoginRequiredError
            if not self.has_date():
                raise DateRequiredError
            if not self.has_time():
                raise TimeRequiredError
            frame_url = SIPAM_FRAME_URL.substitute(year=self.year,
                                                   month=self.month,
                                                   day=self.day,
                                                   token_access=self.token)
            res = req.get(frame_url)
            soup = BeautifulSoup(res.content, "html.parser")
            tags = soup.find_all('pre')[0].find_all('a')
            urls = list()
            for i, tag in enumerate(tags):
                if i % 2 != 0:
                    file_url = os.path.join(ARM_URL_BASE, tag.attrs['href'][1:])
                    print(file_url)
                    urls.append(file_url)
            if not urls:
                raise ListFilesNotFoundError

            substring = "_cappi_%s%s%s_%s%s" % (self.year, self.month, self.day,
                                                self.hour, self.minute)
            file_url = list(filter(lambda url: substring in url, urls))
            print(file_url)
            if not file_url:
                raise UrlFileNotFoundError
            self.remote_url = file_url[0]

        except LoginRequiredError as err:
            print(err)
        except DateRequiredError as err:
            print(err)
        except TimeRequiredError as err:
            print(err)
        except ListFilesNotFoundError as err:
            print(err)
        except UrlFileNotFoundError as err:
            print(err)

    def has_time(self) -> bool:
        return self.hour is not None and self.minute is not None

    def format_time(self) -> None:
        self.hour = str(self.hour).zfill(2) \
            if self.hour is not None else None
        self.minute = str(self.minute).zfill(2) \
            if self.minute is not None else None

    def set_filename(self) -> None:
        try:
            if not self.has_date():
                raise DateRequiredError
            if not self.has_time():
                raise TimeRequiredError
            if not self.has_directory():
                self.set_directory()
        except DateRequiredError as err:
            print(err)
        except TimeRequiredError as err:
            print(err)

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
    obj = SBandRadar(year=2014, month=2, day=18, hour=15, minute=15)
    obj.login("username")
    obj.set_remote_url()
    obj.download()


