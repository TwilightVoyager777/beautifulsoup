from bs4 import BeautifulSoup, SoupStrainer
import argparse, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Task 3')
    parser.add_argument('input', help='Path to the input html file')
    args = parser.parse_args()
    in_path = Path(args.input)

    text = in_path.read_text(encoding='utf-8',errors='ignore')
    def keep_all_filter(*args, **kwargs):
        return True
    soup = BeautifulSoup(text, "lxml", parse_only=SoupStrainer(keep_all_filter))

    count = 0
    for a in soup.find_all(True):
        print(a.name)
        count += 1
    print(f"[INFO] total tags: {count}", file=sys.stderr)

if __name__ == '__main__':
    main()