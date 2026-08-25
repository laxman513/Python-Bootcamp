import requests


def main():
    response = requests.get("https://www.example.com")

    print("Status code:", response.status_code)
    print("Requests version:", requests.__version__)


if __name__ == "__main__":
    main()