import csv

def audit_ad_groups(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Group'] == 'Admin':
                print(f"User {row['User']} is part of Admin group")

if __name__ == '__main__':
    audit_ad_groups('sample_data/ad_group_members.csv')