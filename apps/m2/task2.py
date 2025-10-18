import argparse

from bs4 import BeautifulSoup, SoupStrainer
import argparse, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Task 2')
    parser.add_argument('input', help='Path to the input html file')
    args = parser.parse_args()
    in_path = Path(args.input)

    text = in_path.read_text(encoding='utf-8',errors='ignore')
    strainer = SoupStrainer("a")
    soup = BeautifulSoup(text, "lxml", parse_only=strainer)

    count = 0
    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            print(href)
            count += 1
    print(f"[INFO] links: {count}", file=sys.stderr)

if __name__ == '__main__':
    main()