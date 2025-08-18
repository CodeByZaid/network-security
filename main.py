import sys
from networksecurity.logging.logger import logging
def initiate_data_ingestion(self):
    try:
        df = self.export_collection_as_dataframe()
        df = self.export_data_to_feature_store(df)
        train_file_path, test_file_path = self.split_data_as_train_test(df)
        artifact = DataIngestionArtifact(
            train_file_path=train_file_path,
            test_file_path=test_file_path
        )
        return artifact
    except Exception as e:
        raise NetworkSecurityException(e, sys)   
    
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__=='__main__':
   
    trainingpipelineconfig=TrainingPipelineConfig()
    dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
    data_ingestion=DataIngestion(dataingestionconfig)
    logging.info("Initiate the data ingestion")
    dataingestionartifact=data_ingestion.initiate_data_ingestion()
    logging.info("Data Initiation Completed")
    print(dataingestionartifact)
    
    
    
    
    