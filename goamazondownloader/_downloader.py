import sys; sys.path.insert(0, "/home/adriano/goamazondownloader")
import os
from goamazondownloader import (requests as req, tqdm)
from xml.etree import ElementTree as ET
from goamazondownloader.constants import *
from goamazondownloader._exceptions import *
from goamazondownloader._exceptions import *


class Downloader:
    def __init__(self, **kwargs):
        self.year = kwargs.get('year', None)
        self.month = kwargs.get('month', None)
        self.day = kwargs.get('day', None)
        self.directory = kwargs.get('directory', None)
        self.remote_url = kwargs.get('remote_url', None)
        self.filename = kwargs.get('filename', None)
        self.token = None

    def initializer(self) -> None:
        pass

    def set_remote_url(self) -> None:
        pass

    def set_filename(self) -> None:
        pass

    def has_remote_url(self):
        return self.remote_url is not None

    def has_directory(self) -> bool:
        return self.directory is not None

    def has_date(self) -> bool:
        return self.year is not None and self.month is not None and \
               self.day is not None

    def is_logged(self) -> bool:
        return self.token is not None

    def format_date(self) -> None:
        self.year = str(self.year).zfill(4) \
            if self.year is not None else None
        self.month = str(self.month).zfill(2) \
            if self.month is not None else None
        self.day = str(self.day).zfill(2) \
            if self.day is not None else None

    def set_directory(self, instrument: str) -> None:
        try:
            if not self.has_date():
                raise DateRequiredError
            self.directory = INSTRUMENT_LOCAL_PATH.substitute(
                instrument=instrument,
                year=self.year,
                month=self.month,
                day=self.day)
        except DateRequiredError as err:
            print(err)

    def make_directory(self) -> None:
        try:
            if not self.has_directory():
                raise DirectoryRequiredError
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        except DirectoryRequiredError as err:
            print(err)

    def login(self, username: str) -> None:
        try:
            url_login = ARM_LOGIN_URL.substitute(username=username)
            res = req.get(url_login)
            tree = ET.fromstring(res.text.encode('utf-8'))

            if tree.find('status').text == 'valid':
                self.token = "uid=%s&st=%s" % (tree.find('id').text,
                                               tree.find('st').text)
                print('Logged as %s' % (tree.find('email').text))
            else:
                raise LoginUnsuccessfulError()
        except LoginUnsuccessfulError as err:
            print(err)

    def download(self) -> None:
        try:
            if not self.is_logged():
                raise LoginRequiredError()
            if not self.has_remote_url():
                raise RemoteUrlRequiredError
            if os.path.exists(self.filename):
                raise FileAlreadyExistError
            if not os.path.exists(self.directory):
                self.make_directory()

            res = req.get(self.remote_url, stream=True)
            total_size = int(res.headers['content-length'])
            with open(self.filename, 'wb') as file:
                for data in tqdm(iterable=res.iter_content(chunk_size=CHUNCK
                                                           ),
                                 total=total_size / CHUNCK, unit='KB'):
                    file.write(data)
            print('File %s downloaded!' % self.filename)
        except LoginRequiredError as err:
            print(err)
        except FileAlreadyExistError as err:
            print(err)
        except RemoteUrlRequiredError as err:
            print(err)


