import requests 
import datetime


def print_headers(response):
    print("\nPrinting headers:\n")
    for header, value in response.headers.items():
        print(header, value)
    print()

def print_server_software(response):
    try:
        server = response.headers['server']
    except KeyError:
        server = 'unknown'
    print(f'\nServer: {server}\n')
    

def print_cookies(response):
    print("\nPrinting cookies:\n")
    
    for cookie in response.cookies:
        date = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Cookie Name: {cookie.name}")
        print(f"Expires: {date}")
        print("--------------------")
    print()


def main():
    url = input("\nEnter a URL (press enter for default): ")
    if not url:
        # url = 'http://python.org/'
        url = 'https://www.google.com'
        print(f"Default URL: {url}")
    with requests.get(url) as response:
        # print_headers(response)
        print_server_software(response)
        print_cookies(response)


if __name__ == '__main__':
    main()
        
        