#Найти суммарную стоимость билетов по каждому классу
# обслуживания (поле Pclass).
#1. Survived — обозначает, выжил данный пассажир или нет (0 для умерших, 1 для выживших);
#2. Pclass — класс пассажира (1 — высший, 2 — средний, 3 — низший);
#3. Name — имя;
#4. Sex — пол;
#5. Age — возраст;
#6. SibSp — количество братьев, сестер, сводных братьев, сводных сестер, супругов на борту
#титаника;
#7. Parch — количество родителей, детей (в том числе приемных) на борту титаника;
#8. Ticket — номер билета;
#9. Fare — плата за проезд;
#10. Cabin — каюта;
#11. Embarked — порт посадки (C — Шербур; Q — Квинстаун; S — Саутгемптон).
import csv

with open('data.csv','r') as file:
  v = 0
  s = 0
  e = 0
  for line in file:
      data = line.split(',')
      if data[2] == '1':
          v += float(data[10])
      elif data[2] == '2':
          s += float(data[10])
      elif data[2] == '3':
          e += float(data[10])
print("Сумма полученная от продажи билетов \"высшего(VIP)\" класса - ", round(v,2))
print("Сумма полученная от продажи билетов \"среднего(стандартного)\" класса - ", round(s,2))
print("Сумма полученная от продажи билетов \"низший(эконом)\" класса - ", round(e,2))


