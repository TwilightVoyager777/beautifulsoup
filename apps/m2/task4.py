from bs4 import BeautifulSoup, SoupStrainer
import argparse, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Task 4')
    parser.add_argument('input', help='Path to the input html file')
    args = parser.parse_args()
    in_path = Path(args.input)

    text = in_path.read_text(encoding='utf-8', errors='ignore')
    def pass_all_for_parse(*args, **kwargs):
        return True

    soup = BeautifulSoup(text, "lxml", parse_only=SoupStrainer(pass_all_for_parse()))

    tags_with_id = soup.find_all(attrs={"id": True})

    count = 0
    for tag in tags_with_id:
        print(f"<{tag.name}> id={tag.get('id')}")
        count += 1
    print(f"[INFO] tags with id: {count}", file=sys.stderr)


if __name__ == '__main__':
    main()