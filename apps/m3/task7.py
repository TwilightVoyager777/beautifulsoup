import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

#python apps/m3/task7.py apps/baidu.html

def add_class_attr(tag):
    if tag.name == "p":
        tag.attrs["class"] = "test"


def main():
    parser = argparse.ArgumentParser(description="Task 7 using SoupReplacer API")
    parser.add_argument("input", help="Path to the input html file")
    parser.add_argument("-o", "--output", help="Path to the output html file")
    args = parser.parse_args()

    in_path = Path(args.input)
    text = in_path.read_text(encoding="utf-8")
    replacer = SoupReplacer(xformer=add_class_attr)
    soup = BeautifulSoup(text, "lxml", replacer=replacer)

    out_path = Path(args.output) if args.output else Path("output.html")
    out_path.write_text(soup.prettify(), encoding="utf-8")

    print(f"All <p> tags updated with class='test' and wrote to {out_path}")


if __name__ == "__main__":
    main()
