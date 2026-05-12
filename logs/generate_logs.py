import pandas as pd
import random

ips = [
    "185.23.45.1",
    "192.168.1.5",
    "103.45.67.8",
    "172.16.0.10",
    "91.200.12.5"
]

countries = [
    "India",
    "Russia",
    "China",
    "USA",
    "North Korea"
]

logs = []

for i in range(10):

    log = {
        "ip": random.choice(ips),

        "failed_logins": random.randint(0, 25),

        "data_transfer": round(random.uniform(0.1, 10.0), 2),

        "country": random.choice(countries)
    }

    logs.append(log)

df = pd.DataFrame(logs)

df.to_csv("logs/security_logs.csv", index=False)

print("10 security logs generated successfully.")