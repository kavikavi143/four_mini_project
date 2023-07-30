import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True, f"{url} is online and accessible."
        else:
            return False, f"{url} is online, but returned status code: {response.status_code}"
    except requests.RequestException:
        return False, f"{url} is offline or inaccessible."

def main():
    print("Website Connectivity Checker")
    num_websites = int(input("Enter the number of websites to check: "))

    websites = []
    for i in range(num_websites):
        website_url = input(f"Enter website URL {i + 1}: ")
        websites.append(website_url)

    for url in websites:
        is_online, message = check_website_status(url)
        print(message)

if __name__ == "__main__":
    main()
