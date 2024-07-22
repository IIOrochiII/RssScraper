import scrape

if __name__ == "__main__":
    name = input("Enter the name of channel like this(https://www.youtube.com/@{name})\n")
    print(scrape.getrss(name))