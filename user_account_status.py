import pandas as pd

def inactive_users_report(csv_file):
    df = pd.read_csv(csv_file)
    inactive = df[df['Status'] == 'Disabled']
    print(inactive[['User', 'LastLogin', 'Status']])

if __name__ == '__main__':
    inactive_users_report('sample_data/user_status.csv')