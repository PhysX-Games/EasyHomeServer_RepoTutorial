import os
import numpy as np
import pandas as pd


def create_output_folder():
	os.makedirs("output", exist_ok=True)
	np.save("output/np_array.npy", np.random.rand(10, 10))
	pd.DataFrame(np.random.rand(10, 10)).to_csv("output/pd_dataframe.csv")


def print_data_from_output_folder():
	print(np.load("output/np_array.npy"))
	print(pd.read_csv("output/pd_dataframe.csv"))


if __name__ == '__main__':
	print('-'*50, 'Versions', '-'*50)
	print(f"Numpy version: {np.__version__}")
	print(f"Pandas version: {pd.__version__}")
	print('-'*50, 'Create output folder', '-'*50)
	create_output_folder()
	print_data_from_output_folder()
	print('-'*150)
