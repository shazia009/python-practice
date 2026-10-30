# JSON JAVASCRIPT OBJECT NOTATION DATATYPE HY YEH EK
# load for read

import json
order = {"id": "A102", "customer": "Noor Foods", "total": 12800, "paid": False, "notes": None}
text=json.dumps(order)
print(text)

same_order=json.loads(text)
print(same_order["customer"]) 

 
