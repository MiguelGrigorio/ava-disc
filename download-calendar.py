import twill 
from twill.commands import *
import os

go("https://ava3.cefor.ifes.edu.br")
showforms()

fv("1", "username", "20222ENEL0100")
fv("1", "password", "S6C8iotSRz.")

showforms()

submit()
print("Login realizado com sucesso!")
go("https://ava3.cefor.ifes.edu.br/calendar/export.php?")
showforms()

# Seleciona todos os eventos
fv("2", "events[exportevents]", "all")

# Seleciona a semana atual
fv("2", "period[timeperiod]", "weeknow")

# Aperta o botão de exportar
submit('export', '2')
print("Exportação realizada com sucesso!")

# Salva o arquivo
save_html("calendar.ics")