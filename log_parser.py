import pandas as pd
import re

def parse_nasa_log(file_path):
    pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+|-)')
    records = []

    with open(file_path, 'r', encoding='latin1') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                host, timestamp, request, status, size = match.groups()
                records.append({
                    "host": host,
                    "timestamp": timestamp,
                    "request": request,
                    "status": int(status),
                    "size": int(size) if size != '-' else 0
                })

    return pd.DataFrame(records)
