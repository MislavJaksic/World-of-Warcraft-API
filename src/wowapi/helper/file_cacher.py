from pathlib import Path
import pickle
import logging


class FileCacher(object):
    def __init__(self, dir_path: Path):
        self.dir_path = dir_path

    def __str__(self):
        string = "FileCacher["
        string += str(self.dir_path.resolve())
        string += "]"
        return string

    def object_to_file(self, object, filename):
        logging.info(f"Stored in cache. Id: {filename}")
        with open(self.get_file_path(filename), 'wb') as file:
            pickle.dump(object, file, pickle.HIGHEST_PROTOCOL)

    def from_file(self, filename):
        logging.info(f"Cache hit. Id: {filename}")
        with open(self.get_file_path(filename), 'rb') as file:
            return pickle.load(file)

    def is_file_exists(self, filename):
        return self.get_file_path(filename).exists()

    def get_file_path(self, filename):
        filename_path = self.dir_path / filename
        return filename_path.resolve()
