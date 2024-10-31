from typing import List, Dict
from django.core.paginator import Paginator
from ..repositories.folder_repository import FolderRepository
from ..models import Folder


class FolderService:
    def __init__(self):
        self.repository = FolderRepository()
