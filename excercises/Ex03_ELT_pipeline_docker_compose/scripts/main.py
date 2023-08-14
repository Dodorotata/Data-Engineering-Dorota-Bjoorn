from setup import setup_folder_structure, paths_directory
from extract_data import extract_users
from transform import Transforms
from load import Load


if __name__ == "__main__":

    # create folders
    setup_folder_structure()

    # save user raw data in .json files
    extract_users(3, paths_directory["users"])

    # create df with ids and urls to picutres of avatars
    avatar_df = Transforms(paths_directory["users"]).avatar_df()

    # create df with id, full_name, date_of_birth, city, latitude, longtude
    map_df = Transforms(paths_directory["users"]).map_dashboard_df

    ids, urls = avatar_df["id"], avatar_df["avatar"]
    print(urls, ids)

    # instance of Load class in created with required path parametere
    loader = Load(paths_directory["data_warehouse"])

    # downloads avatar images from the specified URLs and saves them as PNG files
    loader.load_avatars(urls, ids)

    #  save map_df as a CSV file
    loader.load_csv_dashboard(map_df)