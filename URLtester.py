import requests
import argparse

def check_urls(file_path):
    """
    Reads URLs from a file, checks their status, and prints the results.
    
    :param file_path: Path to the file containing URLs.
    """
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except IOError as e:
        print(f"Error: Unable to read the file '{file_path}'. {e}")
        return

    for url in urls:
        url = url.strip()
        if not url:
            continue  # Skip empty lines

        full_url = f"http://{url}" if not url.startswith(("http://", "https://")) else url

        try:
            response = requests.get(full_url, allow_redirects=False, timeout=5)
            print(f"{full_url} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{full_url} - Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Check the status of URLs listed in a file.")
    parser.add_argument('file_path', help="Path to the file containing URLs.")
    args = parser.parse_args()

    check_urls(args.file_path)

if __name__ == "__main__":
    main()