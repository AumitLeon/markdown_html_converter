"""
Collect arguments for converter script.
@author Aumit Leon
"""
import converter
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown File to HTML file')
    parser.add_argument('--input', '-i', type=str, required=True, help="input markdown file")
    parser.add_argument('--output', '-o', type=str, default="converted.html", help="output HTML file")

    args = parser.parse_args()

    converter.main(args)

if __name__ == '__main__':
    main()


