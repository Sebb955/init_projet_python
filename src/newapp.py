from datetime import datetime
from dateutil.relativedelta import relativedelta

def add_time(now, intervals):
    for interval, amount in intervals.items():
        if interval == 'years':
            now = now + relativedelta(years=amount)
        elif interval == 'months':
            now = now + relativedelta(months=amount)
        elif interval == 'weeks':
            now = now + relativedelta(weeks=amount)
        elif interval == 'days':
            now = now + relativedelta(days=amount)
        elif interval == 'hours':
            now = now + relativedelta(hours=amount)
        elif interval == 'minutes':
            now = now + relativedelta(minutes=amount)
        elif interval == 'seconds':
            now = now + relativedelta(seconds=amount)
        else:
            raise ValueError("Interval invalide")
    return now

# Obtention de la date et de l'heure actuelles
now = datetime.now()
print("Date et heure actuelles:", now)

# Ajout de différents intervalles de temps à la date et l'heure actuelles
intervals = {
    'months': 1,
    'weeks': 1,
    'hours': 10
}
now = add_time(now, intervals)

print("Date et heure mises à jour:", now)

