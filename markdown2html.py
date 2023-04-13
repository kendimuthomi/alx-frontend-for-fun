#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
'''


import os
import sys
import re


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write("Missing " + markdown_file + "\n")
        sys.exit(1)

    with open(markdown_file, "r") as f:
        markdown_text = f.read()

    heading_pattern = re.compile(r'^(#+) (.+)$', re.MULTILINE)

    html_text = re.sub(heading_pattern, lambda match: "<h" + str(len(match.group(1))) + ">" + match.group(2) + "</h" + str(len(match.group(1))) + ">", markdown_text)

    list_pattern = r'^- (.+)$'

    html_text = re.sub(list_pattern, r'<ul>\n<li>\1</li>\n</ul>', html_text, flags=re.MULTILINE)

    with open(output_file, "w") as f:
        f.write(html_text)
    exit(0)
