import json


def extract_sales_by_receipt_and_create_file(source_file_path, target_receipt_id, output_file_path):
    try:
        with open(source_file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return

    # Find the accountFiscId for the given receiptId
    account_fisc_id = None
    if 'sales' in data and isinstance(data['sales'], list):
        for sale in data['sales']:
            if 'receiptId' in sale and sale['receiptId'] == target_receipt_id:
                account_fisc_id = sale.get('accountFiscId')
                break

    if account_fisc_id is None:
        print(f"No accountFiscId found for receiptId {target_receipt_id}")
        return

    # Extract sales entries for the found accountFiscId
    matching_sales_entries = [sale for sale in data['sales'] if sale.get(
        'accountFiscId') == account_fisc_id]

    # Write the matching sales entries to a new JSON file
    if matching_sales_entries:
        try:
            with open(output_file_path, 'w') as output_file:
                json.dump(matching_sales_entries, output_file, indent=4)
            print(f"Data has been written to {output_file_path}")
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print(f"No sales entries found for accountFiscId {account_fisc_id}")


# Example usage
source_file_path = 'data.json'
target_receipt_id = 'R845677.9027'
output_file_path = 'output_data.json'

extract_sales_by_receipt_and_create_file(
    source_file_path, target_receipt_id, output_file_path)
