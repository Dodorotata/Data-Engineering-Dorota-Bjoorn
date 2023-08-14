#%%
import json
import pandas as pd 


class _DatalakeProvider:
    """Provides raw data in an easy interface"""
    def __init__(self, users_directory) -> None:
        self.all_users = []                                 # empty list to store all data from .json files
        for filepath in users_directory.iterdir():          # iterated through all .json files in users directory
            with open(filepath, 'r') as file:               # open each file in readmode
                user_data = json.load(file)                 # load JSON data into variable user_data
            self.all_users.append(user_data)                # append user_data to all_users list
            
    @property
    def raw_df(self):
        return pd.DataFrame(self.all_users)                 # makes all_users list into a raw_df with all data

#%%    
class Transforms:
    """Different transforms for different downstreams use cases"""
    # raw df --> base_df with selection of columns
    def __init__(self, users_directory):
        columns_keep = ["id", "first_name", "last_name", "username", "email", "phone_number", "address", "date_of_birth", "avatar"]

        self.base_df = _DatalakeProvider(users_directory).raw_df[columns_keep] # extracts columns from columns_keep from raw_df into new df
    
    # base_df --> final_df with id, full_name, date_of_birth, city, latitude, longtude
    @property
    def map_dashboard_df(self):
        # creates 3 dfs with differenct content
        df = self.base_df[["id", "first_name", "last_name", "date_of_birth"]] # --> final df
        cities = self.base_df["address"].apply(lambda row: row["city"])
        coordinates = self.base_df["address"].apply(lambda row: row["coordinates"])

        # creates 2 series vased on coordinates
        longitudes = coordinates.apply(lambda row: row["lng"]) 
        latitudes = coordinates.apply(lambda row: row["lat"])

        # adds 3 columns to df
        for name, column in zip(["city", "latitude", "longitude"],[cities, latitudes, longitudes]): # --> final df
            df.insert(loc = df.shape[1], column = name, value = column)

        # exchanges first_name and last_name columns for a full name column
        full_name =  df["first_name"] + " " + df["last_name"]
        df.insert(2, "name", full_name)                                                             # --> final df
        df = df.drop(columns = ["first_name", "last_name"])

        return df

    # base_df --> avatar_df with id and url to picutre of avatar
    def avatar_df(self):
        return self.base_df[["id","avatar"]]