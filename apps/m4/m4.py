import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment


def main():
    parser = argparse.ArgumentParser(description='M4')
    parser.add_argument('input', help='Path to the input html file')
    args = parser.parse_args()
    in_path = Path(args.input)

    text = in_path.read_text(encoding="utf-8", errors="ignore")

    soup = BeautifulSoup(text, "lxml")

    print("=== Iterating Over All Nodes ===")
    for node in soup:
        if isinstance(node, Tag):
            print(f"[TAG] <{node.name}> attrs={node.attrs}")
        elif isinstance(node, NavigableString):
            stripped = str(node).strip()
            if stripped:
                print(f"[STRING] \"{stripped}\"")
        elif isinstance(node, Comment):
            print(f"[COMMENT] <!--{node}-->")
        else:
            print(f"[OTHER] {node}")


if __name__ == "__main__":
    main()
