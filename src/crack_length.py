import pandas as pd
import numpy as np

data_path = r"..\data\canadian_pit_data\crack_head_coordinates.csv"


def coordinates_to_length(coordinates: pd.DataFrame)->pd.Series:
    "Compute accumulated length of crack according to coordinates given"
    coordinates_shifted = coordinates.shift(-1)
    coordinates_shifted.iloc[-1, :] = coordinates_shifted.iloc[-2, :]
    delta = coordinates_shifted - coordinates
    square = delta.applymap(lambda x: x**2)
    square_dist = square.sum(axis=1)
    dist_delta = square_dist.map(lambda x: np.sqrt(x))
    dist = dist_delta.cumsum()
    return dist


if __name__ == "__main__":
    data = pd.read_csv(data_path, sep=r"\t", header=None, engine='python')
    left_crack = data.iloc[:, 0:2]
    middle_crack = data.iloc[:, 2:4]
    right_crack = data.iloc[:, 4:6]
    dist_left = coordinates_to_length(left_crack)
    dist_middle = coordinates_to_length(middle_crack)
    dist_right = coordinates_to_length(right_crack)
    dist_df = pd.concat([dist_left, dist_middle, dist_right], axis=1)
    dist_df.to_csv(r"..\data\canadian_pit_data\crack_length.csv", columns=None, index=None, header=None, sep="\t")
