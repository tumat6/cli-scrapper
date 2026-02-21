import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='A simple CLI tool to fetch data from a URL.')
    parser.add_argument('url', type=str, help='The URL to fetch data from')
    args = parser.parse_args()
    return args.url

