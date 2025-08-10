import sys
from copystatic import copystatic
from generatepage import generate_pages_recursive

def main():
    if not sys.argv[1]:
        basepath = '/'
    else:
        basepath = sys.argv[1]
    copystatic("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
