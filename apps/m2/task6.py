import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def main():
    parser = argparse.ArgumentParser(description='Task 6')
    parser.add_argument('input', help='Path to the input html file')
    args = parser.parse_args()
    in_path = Path(args.input)

    text = in_path.read_text(encoding='utf-8',errors='ignore')

    b_to_blockquote = SoupReplacer("b", "blockquote")
    print(BeautifulSoup(text, "lxml", replacer=b_to_blockquote).prettify())

if __name__ == '__main__':
    main()