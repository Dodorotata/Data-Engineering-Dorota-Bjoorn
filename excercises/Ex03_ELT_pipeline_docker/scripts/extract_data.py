# %%
import requests, json, time

def extract_users(number_users: int, users_directory: str):
    """fetch user data from an API, save it as separate JSON files in a specified directory, and provide feedback about the extraction process"""
    for _ in range(number_users):
        # Send a GET request to the API and parse the response as JSON by calling the json() method on the response from .get()
        data = requests.get("https://random-data-api.com/api/v2/users").json()

        # Create a JSON file based on key 'id' and write the fetched data into the created file
        with open(users_directory / f"{data['id']}.json", "w") as file:
            json.dump(data, file)

        print(f"Extracting user with id {data['id']}")
        time.sleep(2)

if __name__ == "__main__":
    extract_users(3)

# %%
