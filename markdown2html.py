#!/usr/bin/python3
"""Code to write markdown for html"""
import os
import sys
import markdown


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write("Missing " + markdown_file + "\n")
        sys.exit(1)
    exit(0)
