import kaggle.api
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_file("cclark/product-item-data", "sample-data.csv")