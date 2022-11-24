import matplotlib.pyplot as plt

def Grafica(var1,var2):
    fig = plt.figure()
    plt.barh(var1,var2,color = 'purple')
    plt.show()
