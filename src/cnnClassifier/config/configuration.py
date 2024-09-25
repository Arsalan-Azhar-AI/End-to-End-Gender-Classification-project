from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from src.cnnClassifier.entity.config_entity import DataPreprocessingConfig
class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            local_data_file2=config.local_data_file2,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config.data_preprocessing

        create_directories([config.root_dir])
        create_directories([config.DATASET])
        create_directories([config.male_path])
        create_directories([config.female_path])

        data_preprocessing_config = DataPreprocessingConfig(
            root_dir=config.root_dir,
            DATASET=config.DATASET,
            male_path=config.male_path,
            female_path=config.female_path,
            data=config.data,
            image_folder1=config.image_folder1,
            folder_name=config.folder_name 
        )

        return data_preprocessing_config
      