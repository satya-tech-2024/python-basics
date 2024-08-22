customer = {
    "name": "Satya",
    "age": 45,
    "IsValid": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("bDate")) #No key is present with this
customer["role"] = "It Consultant"

print(customer)