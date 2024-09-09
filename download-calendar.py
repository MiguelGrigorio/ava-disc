import twill 
from twill.commands import *
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

go("https://ava3.cefor.ifes.edu.br")


fv("1", "username", login)
fv("1", "password", password)

submit()
print("Login realizado com sucesso!")

go("https://ava3.cefor.ifes.edu.br/calendar/export.php?")

fv("2", "events[exportevents]", "all")
fv("2", "period[timeperiod]", "weeknow")

submit('export', '2')

save_html("calendar.ics")
print("Exportação realizada com sucesso!")