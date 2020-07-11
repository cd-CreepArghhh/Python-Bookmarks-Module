def main():
    args = sys.argv
    if len(args) < 2:
        usage()
        return
    command = args[1]
    if command == "help":
        usage()
    elif command == "list":
        list_bookmarks()
    elif command == "add":
        add_bookmark(" ".join(args[2:]))
    elif command == "remove":
        remove_bookmark(" ".join(args[2:]))
    elif command == "search":
        search_for(" ".join(args[2:]))
    elif command == "replace":
        replace_bookmark(" ".join(args[2:]))
    elif command == "uninstall":
        uninstall()


def get_lib_path():
    for pathItem in sys.path:
        if pathItem.endswith(r"\lib"):
            return pathItem


def usage():
    print("""Usage:
    python -m bookmarks <command> [options]

Commands:
    help: displays this help message and exits
    list: lists all your bookmarks
    add <bookmark>: adds <bookmark>
    remove <bookmark>: removes <bookmark>
    search <bookmark>: searches for <bookmark>
    replace <bookmark>: replaces <bookmark>
    clear: removes all bookmarks
    uninstall: uninstalls this module
""")


def list_bookmarks():
    from time import sleep
    f = open("Bookmarks.txt", "r")
    try:
        bookmark_str = list("Your bookmarks are:")
        for x in bookmark_str:
            print(x, end="", flush=True)
            sleep(0.05)
        print("\n")
        sleep(1)
        for text in f.readlines():
            t = list(text.strip())
            for x in t:
                print(x, end="", flush=True)
                sleep(0.05)
            print()
            sleep(0.5)
        input("\n\nEnter to exit")
    finally:
        f.close()


def add_bookmark(bookmark):
    f = open("Bookmarks.txt", "a")
    f.write(bookmark + "\n")
    f.close()
    print(f"Added '{bookmark}'")


def remove_bookmark(bookmark):
    print("If you have too many bookmarks, this may take a while. DO NOT terminate the process as that may delete many of your bookmarks.")
    f = open("Bookmarks.txt", "r")
    txt = f.readlines()
    f.close()
    if (bookmark + "\n") in txt:
        txt.remove(bookmark + "\n")
    else:
        print(f"You haven't bookmarked '{bookmark}'")
        return

    f = open("Bookmarks.txt", "w")

    try:
        for n in txt:
            f.write(n)
    finally:
        f.close()
        print(f"Removed '{bookmark}'")


def search_for(text):
    f = open("Bookmarks.txt", "r")
    for bookmark in f.readlines():
        if text in bookmark.strip():
            print(bookmark.strip())


def clear_bookmarks():
    f = open("Bookmarks.txt", "r")
    for text in f.readlines():
        remove_bookmark(text.strip())


def replace_bookmark(old_bookmark):
    new_bookmark = input(f"Replace '{old_bookmark}' with: ")
    print()
    remove_bookmark(old_bookmark)
    print()
    add_bookmark(new_bookmark)


def uninstall():
    print("Uninstalling...")
    print("Note: uninstalling will not clear your bookmarks.")
    os.remove(get_lib_path() + "\\site-packages\\bookmarks.py")
    os.remove(get_lib_path() + "\\site-packages\\__pycache__\\bookmarks.cpython-38.pyc")


if __name__ == '__main__':
    import sys
    import os
    main()
