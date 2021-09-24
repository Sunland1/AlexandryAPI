import json


def get_store():
    with open("./store.json", "r") as file:
        return json.load(file)


def save_store(new_store):
    with open("./store.json", "w") as file:
        json.dump(new_store , file)


def add_book(data):
    try:
        store = get_store()
        id_book = len(store)
        store[id_book] = data
        save_store(store)
        return 200

    except Exception as e:
        print(f"failed to add book : {e}")
        return 500


def modify_book(data, id_book):
    id_book = str(id_book)
    try:
        store = get_store()
        for key, info in data.items():
            if key == 'year':
                info = int(info)
            store[id_book][key] = info
        save_store(store)
        return store[id_book], 200
    except Exception as e:
        print(f"failed to modify book : {e}")
        return {}, 500


def delete_book(id_book):
    id_book = str(id_book)
    try:
        store = get_store()
        del store[id_book]
        save_store(store)
        return {}, 200
    except Exception as e:
        print(f"failed to modify book : {e}")
        return {}, 500


def get_book(id_book):
    id_book = str(id_book)
    try:
        store = get_store()
        return store[id_book], 200
    except Exception as e:
        print(f"failed to get book : {e}")
        return {}, 500


def get_book_all():
    try:
        store = get_store()
        return store, 200
    except Exception as e:
        print(f"failed to get books : {e}")
        return {}, 500

