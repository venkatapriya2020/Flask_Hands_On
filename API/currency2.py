import requests


def main():
    base = input("First Currency:")
    other = input("Second Currency:")
    res = requests.get("http://data.fixer.io/api/latest?access_key=089650790f130aabee9475bc90832522",
                    params={"base":base,"symbols":other})
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful")
        
    data = res.json()
    print(data)
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")
    
    
if __name__ == "__main__":
    main()        
        