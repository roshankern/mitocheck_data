import pathlib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

import sys
sys.path.append("../utils")
from load_utils import compile_mitocheck_batch_data, split_data
from normalization_utils import get_normalization_scaler, get_normalized_mitocheck_data

# get normalization scaler from negative control features (normalization population)
negative_control_data_path = pathlib.Path("../1.idr_streams/extracted_features/negative_control_data")
normalization_scaler = get_normalization_scaler(negative_control_data_path)

# make results dir if it does not already exist
results_dir = pathlib.Path("normalized_data/")
results_dir.mkdir(parents=True, exist_ok=True)

# normalize training data
data_path = pathlib.Path("../2.format_training_data/results/training_data.csv.gz")
data = pd.read_csv(data_path, compression = "gzip", index_col=0)
normalized_data = get_normalized_mitocheck_data(data, normalization_scaler)
# save normalized training data
save_path = pathlib.Path(f"{results_dir}/{data_path.name}")
normalized_data.to_csv(save_path, compression="gzip")

# normalize negative control data
data_path = pathlib.Path("../1.idr_streams/extracted_features/negative_control_data")
data = compile_mitocheck_batch_data(data_path)
normalized_data = get_normalized_mitocheck_data(data, normalization_scaler)
# save normalized negative control data
save_path = pathlib.Path(f"{results_dir}/{data_path.name}.csv.gz")
normalized_data.to_csv(save_path, compression="gzip", index=False)

# normalize positive control data
data_path = pathlib.Path("../1.idr_streams/extracted_features/positive_control_data")
data = compile_mitocheck_batch_data(data_path)
normalized_data = get_normalized_mitocheck_data(data, normalization_scaler)
# save normalized positive control data
save_path = pathlib.Path(f"{results_dir}/{data_path.name}.csv.gz")
normalized_data.to_csv(save_path, compression="gzip", index=False)