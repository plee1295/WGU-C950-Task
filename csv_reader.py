import csv
from hash_table import HashMap

# Read CSV files
with open('./data/input_data.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')

    hash_map = HashMap()  # Create an instance of HashMap class
    first_delivery = []  # first truck delivery
    second_delivery = [] # second truck delivery
    final_delivery = [] # final truck delivery

    # Insert values from csv file into key/value pairs of the hash table -> O(n)
    for row in read_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        value = [id, address_location, address, city, state, zip, delivery, size, 
            note, delivery_start, delivery_status]

        # Conditional statements to determine which truck a package should be located and 
        # put these packages into a nested list for quick indexing

        # Correct incorrect package details
        if '84104' in value[5] and '10:30' not in value[6]:
            final_delivery.append(value)

        # First truck's first delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_delivery.append(value)

        # Second truck's delivery
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            second_delivery.append(value)
        
        # Check remaining packages
        if value not in first_delivery and value not in second_delivery and value not in final_delivery:
            second_delivery.append(value) if len(second_delivery) < len(final_delivery) else final_delivery.append(value)

        # Insert value into the hash table
        hash_map.insert(id, value)

    # Get packages on the first delivery -> O(1)
    def get_first_delivery():
        return first_delivery

    # Get packages on the second delivery -> O(1)
    def get_second_delivery():
        return second_delivery

    # Get packages on the final delivery -> O(1)
    def get_final_delivery():
        return final_delivery

    # Get full list of packages -> O(1)
    def get_hash_map():
        return hash_map