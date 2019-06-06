"""
This file does the following:
1) Reads in the multiple CSV files into a single dataframe
2) Constructs a new dataframe that aggregates all trips' datapoints into a single row each
3) Have new features in the new dataframe (average, max, min, etc.) 
"""

import re
import os
import numpy as np
import pandas as pd
import glob
import dask.dataframe as dd

PROJ_DIR = os.path.abspath(os.curdir)
FEATURES_DATA_PATH = '/safety/features/*.csv'
LABELS_PATH = '/safety/labels/labels.csv'


def get_features_from_csv():
    """ Returns a dataframe sorted by bookingID and in ascending order for seconds """
    print("Reading CSV files into a dataframe ...")

    features = pd.concat([pd.read_csv(f) for f in glob.glob(
        PROJ_DIR + FEATURES_DATA_PATH)], ignore_index=True)
    features_sorted = features.sort_values(by=['bookingID', 'second'])

    print("Features fetched from CSV!\n")
    return features_sorted


def get_labels():
    labels = pd.read_csv(PROJ_DIR + LABELS_PATH)
    return labels


def create_new_df(dataset, labels):
    mean_df = dataset.groupby('bookingID').mean().reset_index()
    max_df = dataset.groupby('bookingID').max().reset_index()
    min_df = dataset.groupby('bookingID').min().reset_index()
    percentile30_df = dataset.groupby('bookingID').quantile(q=0.3).reset_index()
    percentile70_df = dataset.groupby('bookingID').quantile(q=0.7).reset_index()
    std_df = dataset.groupby('bookingID').std().reset_index()

    time_df = max_df[["bookingID", "second"]].rename(index=str, columns={"second": "time"})

    mean_df = mean_df.rename(index=str, columns={"Accuracy":"Accuracy_avg", 
                                             "Bearing":"Bearing_avg", 
                                             "acceleration_x":"acceleration_x_avg", 
                                             "acceleration_y":"acceleration_y_avg", 
                                             "acceleration_z":"acceleration_z_avg", 
                                             "gyro_x":"gyro_x_avg", 
                                             "gyro_y":"gyro_y_avg", 
                                             "gyro_z":"gyro_z_avg", 
                                             "Speed":"Speed_avg"
                                            })

    max_df = max_df.rename(index=str, columns={"Accuracy":"Accuracy_max", 
                                                "Bearing":"Bearing_max", 
                                                "acceleration_x":"acceleration_x_max", 
                                                "acceleration_y":"acceleration_y_max", 
                                                "acceleration_z":"acceleration_z_max", 
                                                "gyro_x":"gyro_x_max", 
                                                "gyro_y":"gyro_y_max", 
                                                "gyro_z":"gyro_z_max", 
                                                "Speed":"Speed_max"
                                                })

    min_df = min_df.rename(index=str, columns={"Accuracy":"Accuracy_min", 
                                                "Bearing":"Bearing_min", 
                                                "acceleration_x":"acceleration_x_min", 
                                                "acceleration_y":"acceleration_y_min", 
                                                "acceleration_z":"acceleration_z_min", 
                                                "gyro_x":"gyro_x_min", 
                                                "gyro_y":"gyro_y_min", 
                                                "gyro_z":"gyro_z_min", 
                                                "Speed":"Speed_min"
                                                })

    percentile30_df = percentile30_df.rename(index=str, columns={"Accuracy":"Accuracy_perc30", 
                                                                "Bearing":"Bearing_perc30", 
                                                                "acceleration_x":"acceleration_x_perc30", 
                                                                "acceleration_y":"acceleration_y_perc30", 
                                                                "acceleration_z":"acceleration_z_perc30", 
                                                                "gyro_x":"gyro_x_perc30", 
                                                                "gyro_y":"gyro_y_perc30", 
                                                                "gyro_z":"gyro_z_perc30", 
                                                                "Speed":"Speed_perc30"
                                                                })

    percentile70_df = percentile70_df.rename(index=str, columns={"Accuracy":"Accuracy_perc70", 
                                                                "Bearing":"Bearing_perc70", 
                                                                "acceleration_x":"acceleration_x_perc70", 
                                                                "acceleration_y":"acceleration_y_perc70", 
                                                                "acceleration_z":"acceleration_z_perc70", 
                                                                "gyro_x":"gyro_x_perc70", 
                                                                "gyro_y":"gyro_y_perc70", 
                                                                "gyro_z":"gyro_z_perc70", 
                                                                "Speed":"Speed_perc70"
                                                                })
                                                                
    std_df = std_df.rename(index=str, columns={"Accuracy":"Accuracy_std", 
                                            "Bearing":"Bearing_std", 
                                            "acceleration_x":"acceleration_x_std", 
                                            "acceleration_y":"acceleration_y_std", 
                                            "acceleration_z":"acceleration_z_std", 
                                            "gyro_x":"gyro_x_std", 
                                            "gyro_y":"gyro_y_std", 
                                            "gyro_z":"gyro_z_std", 
                                            "Speed":"Speed_std"
                                            })

    list_of_dataframes = [mean_df, max_df, min_df, percentile30_df, percentile70_df, std_df, time_df]
    safety_new_dataset = pd.concat(list_of_dataframes, axis=1)
    bookingID_df = max_df[['bookingID']]
    safety_new_dataset = safety_new_dataset.drop(columns=["second", "bookingID"])
    safety_new_dataset = pd.concat([bookingID_df, safety_new_dataset], axis=1)

    full_df = pd.merge(safety_new_dataset, labels, on="bookingID")
    full_df = full_df.drop_duplicates('bookingID', keep='last')
    print("Size of final dataframe: ", full_df.shape)

    return full_df



if __name__ == "__main__":
    # Get dataframes of features & labels
    dataset = get_features_from_csv()
    labels = get_labels()

    # Create new dataframe with new features
    full_df = create_new_df(dataset, labels)

    # Save new dataframe as a new CSV to disk
    full_df.to_csv('safety_dataset_new.csv', index=False)
    print("Dataset with new features saved as safety_dataset_new.csv!")
