import pandas as pd

def export_to_excel(csv_file, excel_file):
    df = pd.read_csv(csv_file)
    df.to_excel(excel_file, index=False)
    print(f"Exported report to {excel_file}")

if __name__ == '__main__':
    export_to_excel('sample_data/login_audit_sample.csv', 'failed_logins_report.xlsx')