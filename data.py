from json import load

def get_monthly_spendings(file: str) -> dict:
    with open(file) as json_file:
        transactions = load(json_file)

    totals = {}

    for purchase in transactions["transactions"].values():
        shop = purchase["merchant_code"]
        if shop not in totals:
            totals[shop] = purchase["amount_cents"] // 100
        else:
            totals[shop] = totals[shop] + purchase["amount_cents"] // 100

    return totals