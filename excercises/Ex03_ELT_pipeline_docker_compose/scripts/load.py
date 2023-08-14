import time, requests

class Load:
    # define folsers where pictures of avatars will be saved
    def __init__(self, data_warehouse_path) -> None:
        self.avatar_path = data_warehouse_path / "avatars"
        self.data_warehouse_path = data_warehouse_path

    def load_avatars(self, urls, ids):
        # get avatar url for each id/url pair
        for avatar_url, id in zip(urls, ids):
            response = requests.get(avatar_url)

            # create a png file and save content from url as image
            with open(self.avatar_path / f"{id}.png" , "wb") as file: # wb to write non text data such as image
                file.write(response.content)

            time.sleep(2)
    
    # make df into csv file
    def load_csv_dashboard(self, df):
        df.to_csv(self.data_warehouse_path/"users.csv")
