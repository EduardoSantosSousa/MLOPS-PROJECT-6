import os 

#-----------------------------------------------
#Project root path
#-----------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))

#------------------------------------------------
#File and directory configuration
#------------------------------------------------

# Path to general configuration file
CONFIG_PATH = os.path.join(PROJECT_ROOT, 'config', 'config.yml')

# Directories and data files
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'raw')
RAW_DATA = os.path.join(RAW_DATA_DIR, 'data.csv')

PROCESSED_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'processed')

X_TRAIN_PATH = os.path.join(PROCESSED_DIR, 'X_train.pkl')
X_TEST_PATH = os.path.join(PROCESSED_DIR, 'X_test.pkl')
Y_TRAIN_PATH = os.path.join(PROCESSED_DIR, 'y_train.pkl')
Y_TEST_PATH = os.path.join(PROCESSED_DIR, 'y_test.pkl')

MODEL_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'model')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')
CONFUSION_MATRIX_PATH = os.path.join(MODEL_DIR, 'confusion_matrix.png')
