# accountId_from_receiptId

## Overview

1. Use `receiptId_to_accountId_ONLY` to extract the accountId from a receiptId string only.

2. Use `script.py` to extract the accountId from a receiptId string and write the associated sales object to a single file called output_data.json.  This will output the Sale array with enclosing []. This output will comform to the json response format of `GET /f/finance/:businessLocationId/sale?accountId=A83147.4`. See `output_script(Sample).json` to see an example.  

3. Use `app.py` to extract the accountId from a receiptId string and write the associated sales object to a single file called output_data. Within this script, the [] will be omitted from the output file as if you copy pasted the sales array from data.json manually. See `output_app(Sample).json` to see an example.

## How to use

1. Make sure that you have python3 or python installed.
2. Replace the data.json (input_file) with your data.
3. Open the .py file you wish to use.
4. Replace the `target_receipt_id` with the desired receipt.
5. Change the input and output filename and path when appropriate.
6. Run the script by opening a terminal and calling the script you wish to use (e.g. `python3 app.py`).
