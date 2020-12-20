import requests

def main():
    currency=input("Currency:")
    res = requests.get("http://data.fixer.io/api/latest?access_key=089650790f130aabee9475bc90832522")
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful")
        
    data = res.json()
    rate = data["rates"][currency]
    print(f"1 USD is equal to {rate} {currency}")
    
if __name__ == "__main__":
    main()        
        