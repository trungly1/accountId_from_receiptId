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

    # Write the matching sales entry to a new JSON file
    if matching_sales_entries:
        try:
            # Assuming there is only one matching sales entry
            matching_sales_entry = matching_sales_entries[0] if matching_sales_entries else None
            if matching_sales_entry:
                # Check for specific fields before writing to file
                if (matching_sales_entry.get('accountFiscId') == "A845677.9166" and
                        matching_sales_entry.get('receiptId') == target_receipt_id):
                    with open(output_file_path, 'w') as output_file:
                        json.dump(matching_sales_entry, output_file, indent=4)
                    print(f"Data has been written to {output_file_path}")
                else:
                    print(
                        f"No matching entry with specified accountFiscId and receiptId.")
            else:
                print(
                    f"No sales entry found for accountFiscId {account_fisc_id}")
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print(f"No sales entries found for accountFiscId {account_fisc_id}")


# Example usage
source_file_path = 'data.json'
target_receipt_id = 'R845677.9027'  # Updated to match your provided receipt ID
output_file_path = 'app_output.json'

extract_sales_by_receipt_and_create_file(
    source_file_path, target_receipt_id, output_file_path)
