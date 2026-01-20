import requests

def fetch_all_products():
    try:
        response = requests.get("https://dummyjson.com/products?limit=100", timeout=10)
        data = response.json()
        return data.get('products', [])
    except:
        return []


def create_product_mapping(api_products):
    mapping = {}
    for p in api_products:
        mapping[p['id']] = {
            'category': p.get('category'),
            'brand': p.get('brand'),
            'rating': p.get('rating')
        }
    return mapping


def enrich_sales_data(transactions, product_mapping):
    enriched = []

    for t in transactions:
        t_copy = t.copy()
        t_copy['API_Category'] = None
        t_copy['API_Brand'] = None
        t_copy['API_Rating'] = None
        t_copy['API_Match'] = False

        try:
            pid = int(''.join(filter(str.isdigit, t['ProductID'])))
            if pid in product_mapping:
                t_copy['API_Category'] = product_mapping[pid]['category']
                t_copy['API_Brand'] = product_mapping[pid]['brand']
                t_copy['API_Rating'] = product_mapping[pid]['rating']
                t_copy['API_Match'] = True
        except:
            pass

        enriched.append(t_copy)

    save_enriched_data(enriched)
    return enriched


def save_enriched_data(data, filename='data/enriched_sales_data.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region|API_Category|API_Brand|API_Rating|API_Match\n")
        for t in data:
            f.write(
                f"{t['TransactionID']}|{t['Date']}|{t['ProductID']}|{t['ProductName']}|"
                f"{t['Quantity']}|{t['UnitPrice']}|{t['CustomerID']}|{t['Region']}|"
                f"{t['API_Category']}|{t['API_Brand']}|{t['API_Rating']}|{t['API_Match']}\n"
            )

