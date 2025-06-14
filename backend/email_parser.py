import pandas as pd
import re

def parse_email(email):
    local, domain = email.split('@')
    name_parts = re.split(r'[._]', local)
    first = name_parts[0].capitalize()
    last = name_parts[1].capitalize() if len(name_parts) > 1 else ''
    full_name = f"{first} {last}".strip()
    return {
        "first_name": first,
        "full_name": full_name,
        "domain": domain
    }

def read_emails(filepath):
    df = pd.read_csv(filepath)
    result = []
    for email in df['email']:
        parsed = parse_email(email)
        parsed["email"] = email
        result.append(parsed)
    return result
