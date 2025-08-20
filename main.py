import sys
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

# Import configs
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig
# Import components
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
# Import artifacts
from networksecurity.entity.artifact_entity import DataIngestionArtifact

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        # Data Ingestion
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        # Data Validation
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
