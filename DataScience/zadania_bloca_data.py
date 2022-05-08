import matplotlib.pyplot as plt, pandas as pd, numpy as np
from scipy.optimize import curve_fit
from scipy import integrate as intg
from matplotlib.gridspec import GridSpec
import statistics
from sympy import*

data = pd.read_excel('E:\PythonProjects\DataProject\data.xlsx')

xData = data.iloc[:, 0]
yData = data.iloc[:, 1]

x0 = sum(xData*yData)
s = sum(xData**2*yData)-x0

y2 = statistics.mean(xData)

def zadaniablocadata(x,a,x0,s):
    return a*np.exp(-((x-x0)**2/(s**2)))

popt,pcov = curve_fit(zadaniablocadata,xData,yData,p0 = (1,x0,s))
a,x0,s = popt

# Интеграл по данным yData,xData
answer_integral = intg.trapz(yData,xData)

print('-'*72)
print('Интеграл от функции (yData):\n','%.2f'% answer_integral)

# Аргументы для построения графика производной по данным xData,yData
dx = np.diff(xData)
dy = np.diff(yData)
dy_dx = dy/dx

print('-'*72)
print('Производная от функции, значения которой определены в столбце у:\n', dy)
print('-'*72)

# Для равного количества элементов
newxData = xData[:-1]

x_min = xData[0]
y_max = yData[0]
for i in range(len(yData)):
    if y_max < yData[i]:
        if x_min <= xData[i]:
            y_max = yData[i]
            x_min = xData[i]

print('Точка максимума функции по данным из xData, yData,x: %.1f, y: %.1f'% (x_min,y_max))

fig = plt.figure(figsize= (9,9))
GS = GridSpec(4,1,figure=fig)
plt.subplots_adjust(wspace=0, hspace=0.9)

plot1 = plt.subplot(GS[0,0])
plot1.scatter(xData, yData,s=10, label ='Data points', color='red')
plot1.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Даные из файла data.xlsx')
plt.legend()
plt.xlim([-1, 1])

plot2 = plt.subplot(GS[1,0])
plot2.plot(xData, zadaniablocadata(xData, *popt), label='Approximation line', color='blue' )
plot2.scatter(xData, yData, s=10, label='Data points', color='red')
plot2.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Точки и линия апроксимации файла data.xlsx')
plt.legend()
plt.xlim([-1, 1])

plot3 = plt.subplot(GS[3,0])
plot3.scatter(0, 0,s=50, label ='Minimum point', color='black')
plot3.scatter(0, y_max,s=50, label ='Maximum of func', color='#8A2BE2')
plot3.plot(xData,zadaniablocadata(xData,*popt),label ='Main func line of data points', color = 'blue' )

plot3.plot(newxData,dy_dx,label ='Derivative line of data points of main func', color='green') # Производная без аппроксимации

plot3.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Функция и производная')
plt.legend(loc = 4)
plt.xlim([-1, 1])

plot4 = plt.subplot(GS[2,0])
plot4.set_axis_off()
tabledata = [['A','%.2f'% a],
             ['\u03BC','%.2f'% x0],
             ['\u03C3\u00B2','%.2f'% s],
             ['Mean(xData)','%.2f'% y2],
             ['integrate(yData)','%.2f'% answer_integral]]

column_labels=["Parametrs", "Value"]
plot4.table(cellText=tabledata,cellLoc='center',colLabels=column_labels,colColours=['#E0EEEE']*2,loc='center')
plot4.set_title('Параметры аппроксимирующей функции',y=1.15)

plt.show()