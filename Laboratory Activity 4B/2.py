import csv

filename = r"C:\Users\lance\Documents\GitHub\IT0011\Laboratory Activity 4B\currency.csv"
def load_currency_rates(filename):
    currency_rates = {}
    with open(filename, mode="r", newline="", encoding="ISO-8859-1") as file:  
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            try:
                currency, currency_name, rate = row[0].strip(), row[1].strip(), float(row[2].strip())
                currency_rates[currency.upper()] = rate  
            except (ValueError, IndexError):
                print(f"Skipping invalid row: {row}")  
    return currency_rates

def convert_currency(amount, target_currency, rates):
    target_currency = target_currency.upper()  
    if target_currency in rates:
        converted_amount = amount * rates[target_currency]
        return converted_amount
    else:
        return None

def main():
    rates = load_currency_rates(filename)
    amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency do you want to have? ").upper()

    converted = convert_currency(amount, target_currency, rates)
    if converted is not None:
        print(f"\nDollar: {amount} USD")
        print(f"{target_currency}: {converted}")
    else:
        print("Currency not found in the exchange rates.")

if __name__ == "__main__":
    main()
