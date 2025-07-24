import pandas as pd

def report_failed_logins(csv_file):
    df = pd.read_csv(csv_file)
    failed = df[df['Status'] == 'Failed']
    print(failed[['User', 'Timestamp', 'SourceIP']])

if __name__ == '__main__':
    report_failed_logins('sample_data/login_audit_sample.csv')