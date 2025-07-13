# search.py
import webbrowser

def search():
    a= input("search:  ")
    

    if a:
        print(f"Searching Google for: {a}")
        webbrowser.open(f"https://www.google.com/search?q={a}")
    else:
        print("No search term provided.")
        

