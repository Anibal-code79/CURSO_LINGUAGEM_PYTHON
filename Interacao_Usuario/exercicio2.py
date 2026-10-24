#código simples capaz de avaliar a hora de término de um período
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
mins = mins + dura 
hour = hour + mins  
mins = mins % 60
hour = hour % 24
print(hour, ":", mins, sep='')