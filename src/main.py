# import pandas as pd

# df = pd.read_csv(r"data/Sleep_health_and_lifestyle_dataset.csv")

# print(df.head())


import random
import sys
from dvclive import Live

with Live(save_dvc_exp=True) as live:
    epochs = int(sys.argv[1])
    live.log_param("epochs", epochs)
    for epoch in range(epochs):
        live.log_metric("train/accuracy", epoch + random.random())
        live.log_metric("train/loss", epochs - epoch - random.random())
        live.log_metric("val/accuracy",epoch + random.random() )
        live.log_metric("val/loss", epochs - epoch - random.random())
        live.next_step()

