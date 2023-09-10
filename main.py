# Function to split an email address into username and domain
def split_email(email):
    username, domain = email.split('@')
    return username, domain

# Input the number of students
n = int(input("Enter the number of students: "))

# Initialize an empty list to store email IDs
email_ids = []

# Input email IDs for n students and store them in a tuple
for i in range(n):
    email = input(f"Enter the email ID for student {i + 1}: ")
    email_ids.append(email)

# Convert the list of email IDs into a tuple
email_tuple = tuple(email_ids)

# Create two new tuples: one for usernames and one for domains
usernames = tuple(username for username, _ in map(split_email, email_ids))
domains = tuple(domain for _, domain in map(split_email, email_ids))

# Display all three tuples
print("Email IDs:", email_tuple)
print("Usernames:", usernames)
print("Domains:", domains)
