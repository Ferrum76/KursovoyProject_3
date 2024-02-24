from utils.utils import get_last_five_data, get_data_from_json, filter_data, show_balance


def app():
    transactions = get_data_from_json("operations.json")
    ft = filter_data(transactions)
    for_show =get_last_five_data(ft)
    for i in for_show:
        print(show_balance(i), "\n")


if __name__ == "__main__":
    app()