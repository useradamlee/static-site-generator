import sys
from copystatic import copystatic
from generatepage import generate_pages_recursive

def main():
    if not sys.argv[0]:
        basepath = '/'
    else:
        basepath = sys.argv[0]
    copystatic("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
