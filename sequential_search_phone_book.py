def sequential_search_phonebook(phonebook, name):
    for i in range(len(phonebook)):
        if phonebook[i][0] == name:
            return phonebook[i][1]
    return "Nomor telepon tidak ditemukan."

phonebook = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]
name = "Jane Smith"

phone_number = sequential_search_phonebook(phonebook, name)
if phone_number != "Nomor telepon tidak ditemukan.":
    print(f"Nomor telepon Jane Smith adalah: {phone_number}")
else:
    print(phone_number)
