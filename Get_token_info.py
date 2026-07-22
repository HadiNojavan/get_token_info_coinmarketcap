import requests


def get_token_info(id):
    try:
        url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info"

        headers = {"X-CMC_PRO_API_KEY": "dd6bf95258d34316b61f83d9f369b985"}
        param={"id":id}
        response = requests.get(url, headers=headers,params=param)

        data = response.json()["data"]["1"]


        description = data.get("description", "")
        price = description.split("last known price of Bitcoin is ")[1].split(" USD")[0] if "last known price" in description else "N/A"
        supply = description.split("current supply of ")[1].split(".")[0] if "current supply" in description else "N/A"


        print(f"Name: {data['name']} ({data['symbol']})")
        print(f"Whitepaper: {data['urls']['technical_doc'][0] if data['urls']['technical_doc'] else 'N/A'}")
        print(f"GitHub: {data['urls']['source_code'][0] if data['urls']['source_code'] else 'N/A'}")
        print(f"Top Tags: {', '.join(data['tag-names'][:5])}")


        print(f"Price: ${price} USD")
        print(f"Circulating Supply: {supply} BTC")
        print(f"Launch Date: {data['date_launched']}")

        print("Blockchain Explorers:")
        for url in data['urls']['explorer']:
            print(f"   - {url}")

    except Exception as e:
        print(e)

if __name__=="__main__":
    get_token_info(id=1)
