import random
import SqLite

class Anny():
    # Коэффициент при x
    k = random.uniform(-5, 5)

    # Свободный член уравнения прямой
    c = random.uniform(-5, 5)
    j=0
    # Вывод данных начальной прямой
    print('Начальная прямая: ', k, '* X + ', c)

    # Набор точек X:Y
   # input_x = SqLite.Data.getxinputs(0)
    #input_y = SqLite.Data.getyinputs(0)
    #print(input_y)
    # Скорость обучения
    rate = 0.000001


    # Высчитать y
    def proceed(self, x):
        return x * Anny.k + Anny.c


    # Тренировка сети
    def train(self, input_x, input_y, lenn):
        for i in range(7000):
            # Получить случайную X координату точки
            #j +=1
            #if j==len(SqLite.Data.getxinputs(0)):
                #j=0
            ran = random.randint(0, lenn)
            x = input_x[ran]
            #len(SqLite.Data.getxinputs(0))-1
            #print(x)
            # Получить соответствующую Y координату точки
            true_result = input_y[ran]
            #print('X',input_x[j],'Y',input_y[j])
            # Получить ответ сети
            out = Anny.proceed(0, x)
            # Считаем ошибку сети
            delta = true_result - out
            # Меняем вес при x в соответствии с дельта-правилом
            Anny.k += delta * Anny.rate * x

            # Меняем вес при постоянном входе в соответствии с дельта-правилом
            Anny.c += delta * Anny.rate
        list=[x,x * Anny.k + Anny.c]
        return list

# Вывод данных готовой прямой
print(Anny.train(0,SqLite.Data.getxinputs(0),SqLite.Data.getyinputs(0),len(SqLite.Data.getxinputs(0))-1))