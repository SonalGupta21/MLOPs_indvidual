from dataclasses import dataclass
from pathlib import Path

#Defining the data class which basically tells you where and how the data could be fetched
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path