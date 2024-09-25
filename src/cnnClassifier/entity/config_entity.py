from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    local_data_file2: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    DATASET: Path
    male_path: Path
    female_path: Path
    data: Path
    image_folder1: Path
    folder_name: Path