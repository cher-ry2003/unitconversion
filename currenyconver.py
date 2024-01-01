import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    params = {'apikey': api_key}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        rate = data['rates'].get(target_currency)
        if rate:
            return rate
        else:
            raise ValueError(f"Unsupported target currency: {target_currency}")
    else:
        raise Exception(f"Failed to fetch exchange rates: {data.get('error')}")


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


def currency_converter(api_key):
    print("Welcome to the Currency Converter!")
    
    while True:
        try:
            amount = float(input("Enter the amount in the source currency: "))
            source_currency = input("Enter the source currency code (e.g., USD): ").upper()
            target_currency = input("Enter the target currency code (e.g., EUR): ").upper()
            
            exchange_rate = get_exchange_rate(api_key, source_currency, target_currency)
            converted_amount = convert_currency(amount, exchange_rate)
            
            print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
            print(f"Exchange rate used: 1 {source_currency} = {exchange_rate:.4f} {target_currency}")
            
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    api_key = 'https://api.api-ninjas.com/v1/convertcurrency?have'
    currency_converter(api_key)
