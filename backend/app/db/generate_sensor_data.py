from datetime import date, datetime, timedelta
import random

equipment_ids = [f'EQ-{str(i).zfill(5)}' for i in range(12486, 12496)]
fixed_measures = [i for i in range(0,23, 2)]
end_date = date.today()
start_date = end_date - timedelta(days=30)
filename = 'data_sensor.dat'

with open(filename, 'w') as file:
    while start_date <= end_date:
        for eqId in equipment_ids:
            for hour in fixed_measures:
                timestamp = datetime(year=start_date.year, month=start_date.month, day=start_date.day, hour=hour, minute=0, second=0)
                value = round(random.uniform(0.0, 90.0), 1)
                file.write(f'{eqId},{value},{timestamp.isoformat()}\n')

        start_date += timedelta(days=1)
