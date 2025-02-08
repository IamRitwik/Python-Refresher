import webbrowser

searchTerm = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("https://google.com/search?q=" + searchTerm)
