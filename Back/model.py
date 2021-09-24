import json

def getStore() : 
    with open("./store.json" , "r" ) as file :
        return json.load(file)


def saveStore(new_store) : 
    with open("./store.json" , "w") as file :
        json.dump(new_store , file)

def add_book(data):
    try :
        store = getStore()
        id_book = len(store) + 1 
        store[id_book] = data
        saveStore(store)
        return 200

    except Exception as e : 
        print(f"failed to add book : {e}")
        return 500

def get_Book(id_book) : 
    try :
        store = getStore()
        return 200 , store[id_book]
    except Exception as e : 
        print(f"failed to get book : {e}")
        return 500



def get_book_all() :
    try :
        store = getStore()
        return {
            "statusCode" : 200 ,
            "body" : store
        }
    except Exception as e : 
        print(f"failed to get books : {e}")
        return 500
