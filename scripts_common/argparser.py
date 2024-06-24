import argparse

def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description='Open a web browser with specific options and periodically open new tabs.')
    parser.add_argument('url', help='URL to open in the browser')
    # parser.add_argument('tabs_number', type=int, help='URL to open in the browser')

    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode')
    parser.add_argument('--host', action='store_true', help='Open tab as a host of the conference')

    parser.add_argument('--url_statistics', help='The URL of the server to send data to.')
    parser.add_argument('--client_id', help='Unique client identifier.')
    
    parser.add_argument('--interval', type=int, default=1, help='Interval between data sends in seconds.')
    parser.add_argument('--tab_id', type=int, default=1, help='Id for user')

    return parser.parse_args()