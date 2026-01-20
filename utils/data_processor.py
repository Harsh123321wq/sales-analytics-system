from datetime import datetime

# ---------- PART 1 ----------
def parse_transactions(raw_lines):
    transactions = []

    for line in raw_lines:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) != 8:
            continue

        tid, date, pid, pname, qty, price, cid, region = parts

        try:
            pname = pname.replace(',', '')
            qty = int(qty)
            price = float(price.replace(',', ''))
        except:
            continue

        transactions.append({
            'TransactionID': tid,
            'Date': date,
            'ProductID': pid,
            'ProductName': pname,
            'Quantity': qty,
            'UnitPrice': price,
            'CustomerID': cid,
            'Region': region
        })

    return transactions


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid = []
    invalid = 0

    for t in transactions:
        try:
            if (t['Quantity'] <= 0 or
                t['UnitPrice'] <= 0 or
                not t['TransactionID'].startswith('T') or
                not t['ProductID'].startswith('P') or
                not t['CustomerID'].startswith('C')):
                invalid += 1
                continue

            amount = t['Quantity'] * t['UnitPrice']
            if region and t['Region'] != region:
                continue
            if min_amount and amount < min_amount:
                continue
            if max_amount and amount > max_amount:
                continue

            valid.append(t)
        except:
            invalid += 1

    summary = {
        'total_input': len(transactions),
        'invalid': invalid,
        'final_count': len(valid)
    }

    return valid, invalid, summary

# ---------- PART 2 ----------
def calculate_total_revenue(transactions):
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)


def region_wise_sales(transactions):
    regions = {}
    total = calculate_total_revenue(transactions)

    for t in transactions:
        r = t['Region']
        amt = t['Quantity'] * t['UnitPrice']
        if r not in regions:
            regions[r] = {'total_sales': 0, 'transaction_count': 0}
        regions[r]['total_sales'] += amt
        regions[r]['transaction_count'] += 1

    for r in regions:
        regions[r]['percentage'] = round((regions[r]['total_sales'] / total) * 100, 2)

    return dict(sorted(regions.items(), key=lambda x: x[1]['total_sales'], reverse=True))


def top_selling_products(transactions, n=5):
    products = {}
    for t in transactions:
        name = t['ProductName']
        if name not in products:
            products[name] = [0, 0]
        products[name][0] += t['Quantity']
        products[name][1] += t['Quantity'] * t['UnitPrice']

    result = [(k, v[0], v[1]) for k, v in products.items()]
    result.sort(key=lambda x: x[1], reverse=True)
    return result[:n]


def customer_analysis(transactions):
    customers = {}
    for t in transactions:
        cid = t['CustomerID']
        amt = t['Quantity'] * t['UnitPrice']
        if cid not in customers:
            customers[cid] = {'total_spent': 0, 'count': 0}
        customers[cid]['total_spent'] += amt
        customers[cid]['count'] += 1

    for cid in customers:
        customers[cid]['avg_order_value'] = round(
            customers[cid]['total_spent'] / customers[cid]['count'], 2
        )

    return dict(sorted(customers.items(), key=lambda x: x[1]['total_spent'], reverse=True))


def daily_sales_trend(transactions):
    daily = {}
    for t in transactions:
        d = t['Date']
        if d not in daily:
            daily[d] = {'revenue': 0, 'count': 0, 'customers': set()}
        daily[d]['revenue'] += t['Quantity'] * t['UnitPrice']
        daily[d]['count'] += 1
        daily[d]['customers'].add(t['CustomerID'])

    for d in daily:
        daily[d]['unique_customers'] = len(daily[d]['customers'])
        del daily[d]['customers']

    return dict(sorted(daily.items()))


def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)
    peak = max(daily.items(), key=lambda x: x[1]['revenue'])
    return peak[0], peak[1]['revenue'], peak[1]['count']


def low_performing_products(transactions, threshold=10):
    products = {}
    for t in transactions:
        name = t['ProductName']
        if name not in products:
            products[name] = [0, 0]
        products[name][0] += t['Quantity']
        products[name][1] += t['Quantity'] * t['UnitPrice']

    result = [(k, v[0], v[1]) for k, v in products.items() if v[0] < threshold]
    result.sort(key=lambda x: x[1])
    return result

# ---------- PART 4 ----------
def generate_sales_report(transactions, enriched, output_file='output/sales_report.txt'):
    total_rev = calculate_total_revenue(transactions)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*40 + "\n")
        f.write("SALES ANALYTICS REPORT\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write("="*40 + "\n\n")
        f.write(f"Total Revenue: ₹{total_rev:,.2f}\n")
        f.write(f"Total Transactions: {len(transactions)}\n")

