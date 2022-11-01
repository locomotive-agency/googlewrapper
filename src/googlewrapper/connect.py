"""API Wrapper for Google Authentication"""

from __future__ import annotations

import argparse
from pathlib import Path

from oauth2client import client, tools, file
import httplib2
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pygsheets


class Connection:
    """
    Google Connection Resource Objects Wrapper Class
    REMEMBER your 'client_secret.json' file in your PATH

    Creates a folder in the CWD (if it doesn't exist),
    Authenticate via oAuth2.0,
    Returns a resource object to be used in the other wrapper classes

    __Current methods used for authenication__
    .gsc() -> Google Search Console
    .ga() -> Google Analytics
    .cal() -> Google Calendar
    .sheets() -> Google Sheets
    .gbq()** -> Google Big Query
    .gmail() -> Gmail

    ** requires a separate service account authentication file **
    """

    def __init__(self) -> None:
        self.__dir_check()

    def __dir_check(self) -> None:
        # if there isn't a crednetials folder, create one
        if not Path("./credentials/").is_dir():
            Path("./credentials/").mkdir()

    def _authenticate(self, scope: list, service_account_key: str, service_account_subject: str):
         return service_account.Credentials.from_service_account_file(service_account_key,
                                                                 scopes=scope,
                                                                 subject=service_account_subject)

    def gsc(self, service_account_key, service_account_subject):
        """Google Search Console Connection Method"""
        scope_list = ["https://www.googleapis.com/auth/webmasters.readonly"]
        return build(
            "searchconsole", "v1", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
        )

    def ga(self, service_account_key, service_account_subject):
        """Google Analytics Connection Method"""
        scope_list = ["https://www.googleapis.com/auth/analytics.readonly"]
        return build(
            "analyticsreporting", "v4", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
        )

    def cal(self, service_account_key, service_account_subject):
        """Google Calendar Connection Method"""
        scope_list = ["https://www.googleapis.com/auth/calendar"]
        return build(
            "calendar", "v3", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
        )

    def pygsheets(self):
        "Pygsheets Connection Method"
        return pygsheets.authorize(local=True, credentials_directory="./credentials/")

    def sheets(self, service_account_key, service_account_subject):
        """Google Sheets Connection Method"""
        scope_list = [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        return build(
            "sheets", "v4", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
        )

    def gbq(self, service_account_key, service_account_subject):
        """
        Google Big Query Connection Method
        Requires a different .json file to connect
        """
        return service_account.Credentials.from_service_account_file(service_account_key, service_account_subject)

    def gmail(self, service_account_key, service_account_subject):
        """GMAIL Connection Method"""
        scope_list = ["https://mail.google.com/"]
        return build("gmail", "v1", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
    )

    def drive(self, service_account_key, service_account_subject):
        """Google Drive Connection Method"""
        scope_list = ["https://www.googleapis.com/auth/drive.readonly"]
        return build("drive", "v3", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
    )

    def docs(self, service_account_key, service_account_subject):
        """Google Docs Connection Method"""
        scope_list = ["https://www.googleapis.com/auth/drive.readonly"]
        return build("docs", "v1", credentials=self._authenticate(scope_list, service_account_key, service_account_subject)
    )
