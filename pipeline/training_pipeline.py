from src.common_functions import read_yaml
from src.data_ingestion import DataIngestion
from config.paths_config import *
from src.data_processing import DataProcessing
from src.model_training import ModelTraining


if __name__ == "__main__":
    config = read_yaml(file_path=CONFIG_PATH)

    gcs_params = {
        "project_id": config['project_id'],
        "bucket_name": config['gcs_config']['bucket_name'],
        "file_name": config['gcs_config']['file_name'],
    }
    data_ingestion = DataIngestion(gcs_params=gcs_params, output_dir=RAW_DATA_DIR)
    data_ingestion.run()

    data_processor = DataProcessing(file_path=RAW_DATA)
    data_processor.run()

    trainer = ModelTraining()
    trainer.run()