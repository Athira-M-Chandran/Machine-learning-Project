from collections import namedtuple

DataIntegrationConfig = namedtuple('DataIngestionConfig','[dataset_download_url','tgz_download_dir',"raw_data_div",'congested_train_dir','ingested_test_dir'])

DataValidationConfig = namedtuple("DataValidationConfig", ['schema_file_path'])

DataTransformationConfig = namedtuple("DataTransformationConfig", ['add_bedroom_per_room','transformed_train_dir','transformed_test_dir','preprocessed_object_file_path'])

ModelTrainerConfig = namedtuple('ModelTrainerConfig',['ModelTrainerConfig', 'trained_model_file_path', 'base_accuracy'])

ModelEvaluationConfig = namedtuple('ModelEvaluationConfig', ['model_evaluation_file_path','timestamp'])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])