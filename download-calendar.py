import twill 
from twill.commands import *
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

go("https://ava3.cefor.ifes.edu.br")

fv("1", "username", username)
fv("1", "password", password)

submit()
print("Login realizado com sucesso!")


go("https://ava3.cefor.ifes.edu.br/calendar/export.php?")

fv("2", "events[exportevents]", "all")
fv("2", "period[timeperiod]", "weeknow")

submit('export', '2')
save_html("calendar.ics")
print("Exportação realizada com sucesso!")
