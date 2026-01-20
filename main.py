from utils.file_handler import read_sales_data
from utils.data_processor import *
from utils.api_handler import *

def main():
    try:
        print("SALES ANALYTICS SYSTEM")

        raw = read_sales_data("data/sales_data.txt")
        transactions = parse_transactions(raw)

        valid, invalid, _ = validate_and_filter(transactions)

        api_products = fetch_all_products()
        mapping = create_product_mapping(api_products)

        enriched = enrich_sales_data(valid, mapping)

        generate_sales_report(valid, enriched)

        print("Process completed successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

