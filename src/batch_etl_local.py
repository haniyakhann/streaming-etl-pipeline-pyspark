import json
import csv
from datetime import datetime
from pathlib import Path

def main():
    input_file = Path("data/raw/events1.json")
    output_file = Path("output/curated/events_curated.csv")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with input_file.open() as f:
        for line in f:
            event = json.loads(line)
            if not event.get("event_type"):
                continue
            event["ingest_ts"] = datetime.utcnow().isoformat()
            rows.append(event)

    if rows:
        with output_file.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

    print("ETL complete → output/curated/events_curated.csv")

if __name__ == "__main__":
    main()
