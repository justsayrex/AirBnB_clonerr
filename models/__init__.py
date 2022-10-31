"""This is the module for FileStorage autoinit."""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
