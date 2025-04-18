import pytz
import time
import logging
from datetime import datetime


def format_time_exec(initial):
    try:
        fin = time.time()
        duracion = int(fin - initial)
        dias = duracion // 86400
        horas = (duracion % 86400) // 3600
        minutos = (duracion % 3600) // 60
        segundos = duracion % 60
        return f"Tiempo de ejecución: {dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}"
    except Exception as e:
        logging.error(str(e), exc_info=True)
        print(e)

def time_converter(tz):
    def converter(*args):
        utc_dt = datetime.utcnow()
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(tz)
        return local_dt.timetuple()
    return converter

