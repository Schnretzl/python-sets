# 2. Set Operations in Data Analysis

# Task 1: Duplicate Entries Cleanup
def remove_dupicates(customer_id_list):
    return set(customer_id_list)

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
print(remove_dupicates(customer_ids))