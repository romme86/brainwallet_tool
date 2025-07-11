import hashlib
from bit import Key

word_to_check = "1234567890"
private_key = hashlib.sha256(word_to_check.encode('utf-8')).hexdigest()
k = Key.from_hex(private_key)
txs = k.get_transactions()
if len(txs) > 0:
    print(">>>FOUND activity on brainwallet:", word_to_check)
    print("Address:", k.address)
else:
    print("try again, you will have more luck.")
