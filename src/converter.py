"""
@author Aumit Leon
Convert Markdown documents to HTML
Uses the mistune library markdown parser: https://github.com/lepture/mistune (Copyright (c) 2014, Hsiaoming Yang)
License information for use of mistune library: https://github.com/lepture/mistune/blob/master/LICENSE
"""

import re
import argparse
import mistune
from bs4 import BeautifulSoup as bs


def main():
    # Collect arguments
    parser = argparse.ArgumentParser(description="Convert Markdown File to HTML file")
    parser.add_argument(
        "--input", "-i", type=str, required=True, help="input markdown file"
    )
    parser.add_argument(
        "--output", "-o", type=str, default="converted.html", help="output HTML file"
    )

    args = parser.parse_args()

    html_doc = open(args.output, "w", encoding="utf-8")
    generated_html = (
        "<!DOCTYPE html>"
        + "<!--Converted via md-to-html-->"
        + "<html><head></head><body>"
    )

    with open(args.input, encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
            generated_html += mistune.markdown(line)

    generated_html += "</body></html>"

    # make BeautifulSoup
    soup = bs(generated_html, "html.parser")
    # prettify the html
    prettyHTML = soup.prettify()
    # write to the html doc
    html_doc.write(prettyHTML)


if __name__ == "__main__":
    main()
