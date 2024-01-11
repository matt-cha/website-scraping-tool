import requests
import csv

def scrape_inventory_api():
    url = "https://www.coastlinecdjr.com/new-inventory/index.htm"  # Replace with the actual API endpoint URL

    # Headers from the Network tab in dev tools
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.coastlinecdjr.com/new-inventory/index.htm",
        # Add any other required headers
    }

    # You may need to include any necessary parameters in the payload
    payload = {
        "start": "0",
        "rows": "10",  # Adjust the number of rows as needed
        # Add any other required parameters
    }

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers, params=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and process the information you need from the 'getInventory' object
        inventory_data = data.get('getInventory', [])

        # Example: Print the VIN and price for each vehicle
        for item in inventory_data:
            vin = item.get('vin', 'N/A')
            price = item.get('price', {}).get('basePrice', 'N/A')

            print("VIN:", vin)
            print("Price:", price)
            print("-" * 30)

        # Save the data to a CSV file
        save_to_csv(inventory_data)

    else:
        print("Failed to retrieve data. Status code:", response.status_code)

def save_to_csv(data):
    # Specify the file path for the CSV file
    csv_file_path = "inventory_data.csv"

    # Specify the field names/columns for the CSV file
    field_names = ["VIN", "Price"]  # Add more fields as needed

    # Write the data to the CSV file
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    scrape_inventory_api()
import requests
import csv

def scrape_inventory_api():
    url = "https://www.coastlinecdjr.com/inventory/getInventory.htm"  # Replace with the actual API endpoint URL

    # Headers from the Network tab in dev tools
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.coastlinecdjr.com/new-inventory/index.htm",
        # Add any other required headers
    }

    # You may need to include any necessary parameters in the payload
    payload = {
        "start": "0",
        "rows": "10",  # Adjust the number of rows as needed
        # Add any other required parameters
    }

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers, params=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and process the information you need from the 'getInventory' object
        inventory_data = data.get('getInventory', [])

        # Example: Print the VIN and price for each vehicle
        for item in inventory_data:
            vin = item.get('vin', 'N/A')
            price = item.get('price', {}).get('basePrice', 'N/A')

            print("VIN:", vin)
            print("Price:", price)
            print("-" * 30)

        # Save the data to a CSV file
        save_to_csv(inventory_data)

    else:
        print("Failed to retrieve data. Status code:", response.status_code)

def save_to_csv(data):
    # Specify the file path for the CSV file
    csv_file_path = "inventory_data.csv"

    # Specify the field names/columns for the CSV file
    field_names = ["VIN", "Price"]  # Add more fields as needed

    # Write the data to the CSV file
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    scrape_inventory_api()
