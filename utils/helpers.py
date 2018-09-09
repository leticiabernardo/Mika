from datetime import datetime
from pytz import timezone
import time
from unicodedata import normalize


def clean_word(string):
    ln = string.strip()
    #ln = normalize('NFKD', ln).encode('ASCII', 'ignore').decode('ASCII')

    ln = ln.upper()
    return ln


def get_date_human_post(date_req):
    south_africa = timezone('America/Sao_Paulo')
    sa_time = datetime.now(south_africa)

    date_today = sa_time.strftime('%Y-%m-%d')
    date_today_time = time.mktime(datetime.strptime(date_today, "%Y-%m-%d").timetuple())
    date_today_year = sa_time.strftime('%Y')

    date_req_date = time.strftime('%Y-%m-%d', time.strptime(date_req, '%a %b %d %H:%M:%S +0000 %Y'))
    date_req_hour = time.strftime('%H:%M', time.strptime(date_req, '%a %b %d %H:%M:%S +0000 %Y'))
    date_req_time = time.mktime(datetime.strptime(date_req_date, "%Y-%m-%d").timetuple())
    date_req_year = time.strftime('%Y', time.strptime(date_req, '%a %b %d %H:%M:%S +0000 %Y'))
    day = time.strftime('%d', time.strptime(date_req, '%a %b %d %H:%M:%S +0000 %Y'))
    month = time.strftime('%B', time.strptime(date_req, '%a %b %d %H:%M:%S +0000 %Y'))

    if date_today_time == date_req_time:
        return "Hoje às " + date_req_hour
    else:
        if (date_today_time - date_req_time) == 86400:
            return "Ontem às " + date_req_hour
        else:
            if ((date_today_time - date_req_time)/86400) <= 7:
                past_days = int((date_today_time - date_req_time)/86400)
                return "Há " + str(past_days) + " dias às " + date_req_hour

            elif date_today_year == date_req_year:
                return day + " de " + month + " às " + date_req_hour
            else:
                return day + " de " + month + " de " + date_req_year + " às " + date_req_hour

#date_req = "Sat Aug 25 16:45:54 +0000 2018"
#print (get_date_human_post(date_req))


