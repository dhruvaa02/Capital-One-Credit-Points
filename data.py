"""
This file contains all the functionality for reading data from JSON formatted files in the
same directory. For now contains the function to read transactions and total the monthly
spendings. If this were to be scaled, would also contain the functionality to read
and update the rewards points system's rules as well.
"""
from json import load

def get_monthly_spendings(file: str) -> dict:
    """Reads transactions data from file in JSON format and returns the monthly spendings
    at each merchant.

        Args:
            - file: file path/name containing the month's transactions
 
        Returns:
            - totals: dictionary with merchants as keys and money spent in that month
            at that merchant {merchant: money spent}.

        >>> print(get_monthly_spendings("transactions.json"))
        {'sportcheck': 370, 'tim_hortons': 71, 'subway': 39}
        """

    with open(file) as json_file:
        transactions = load(json_file)

    totals = {}

    for purchase in transactions["transactions"].values():
        shop = purchase["merchant_code"]
        if shop not in totals:
            totals[shop] = purchase["amount_cents"] // 100 # convert to dollars and round down
        else:
            totals[shop] = totals[shop] + purchase["amount_cents"] // 100

    return totals