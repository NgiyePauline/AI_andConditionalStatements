Accuracy = 0.85
if 0.0 <= Accuracy <= 0.5:
#Accuracy >= 0.0 or Accuracy <= 0.5:
    result = 'poor model perfomance'
elif 0.51 <= Accuracy <= 0.75:
#Accuracy >= 0.51 or Accuracy <= 0.75:
    result = 'Average perfomance'
elif 0.76 <= Accuracy <= 0.90:
#Accuracy >= 0.76 or Accuracy <= 0.90:
    result ='Good model perfomance'
elif 0.91 <= Accuracy <= 1.0:
    result = 'Excellent model perfomance'
    print(Accuracy)
else:
    result = 'Invalid accuracy score'


print(result)


if result == 'model perfomance: Good':
    print('Nice work')
else:
    print('Not quite! Are your result strings formatted correctly?')