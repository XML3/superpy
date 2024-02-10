import uuid

#Functions:

#Generates a unique product ID
def generate_product_id():
    return str(uuid.uuid4())

#Generates a unique purchase ID
def generate_purchase_id():
    return str(uuid.uuid4())

#Generates a unique sale ID
def generate_sold_id():
    return str(uuid.uuid4())

#Test for sold_id/  Is it duplicating or is it Unique ID?
def test_generate_sold_id(num_ids=1000):
    generate_ids = set()
    for _ in range(num_ids):
        sold_id = generate_sold_id()
        if sold_id in generate_ids:
            print("Duplicate ID found:", sold_id)
            return False
        generate_ids.add(sold_id)
        print("all IDs are unique!")
        return True

if __name__ == "__main__":
    test_generate_sold_id()