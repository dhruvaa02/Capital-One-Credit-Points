from monthly import get_monthly_spendings
from maximizer import reduced_bf

if __name__ == "__main__":
    monthly = get_monthly_spendings("transactions.json")
    points = reduced_bf(monthly)
    print(points)