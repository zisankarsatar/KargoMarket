import shutil
import os


def delete_path(p):
    try:            
        p = os.path.join(os.getcwd(), p)
        print("Path will be deleted {}".format(p))
        shutil.rmtree(p)
    except FileNotFoundError:
        return
    except NotADirectoryError:
        os.remove(p)

def run():
    print("Current Directory: ", os.getcwd())
    paths = [
        "account/migrations",
        "db.sqlite3",
    ]
    for p in paths:
        delete_path(p)
    