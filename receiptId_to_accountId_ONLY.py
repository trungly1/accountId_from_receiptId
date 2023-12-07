import json


def get_account_fisc_id_by_receipt_id(file_path, target_receipt_id):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None

    # Check if 'sales' key is in data and it is a list
    if 'sales' in data and isinstance(data['sales'], list):
        for sale in data['sales']:
            # Check if 'receiptId' is in the sale and matches the target_receipt_id
            if 'receiptId' in sale and sale['receiptId'] == target_receipt_id:
                # Return the 'accountFiscId' if found
                return sale.get('accountFiscId')

    return None  # Return None if the receiptId was not found or 'sales' is not a list


# Example usage
file_path = 'data.json'
receipt_id = 'R845677.9027'
account_fisc_id = get_account_fisc_id_by_receipt_id(file_path, receipt_id)

if account_fisc_id:
    print(f"The accountFiscId for receiptId {receipt_id} is {account_fisc_id}")
else:
    print(f"No accountFiscId found for receiptId {receipt_id}")
