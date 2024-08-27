import os
import urllib.request as request
import zipfile
from textsummarization.logging import logger
from textsummarization.utils.common import get_size
from textsummarization.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_dir):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_dir
            )
            logger.info(f"Downloaded file {self.config.local_dir} to {self.config.local_dir}")
        else:
            logger.info(f"File {self.config.local_dir} already exists of size {get_size(Path(self.config.local_dir))}")

    def extract_zip_file(self):
        """
        zip_file_path: Path to the zip file
        Extracts all files from the zip file to the unzip_path directory.
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)