import matplotlib.pyplot as plt


def conv_curve(name):
    with open(str(name) + ".csv", 'r') as file:
        lines = file.readlines()
        file.close()
    lines = lines[2:]
    time = []
    y1 = []
    y2 = []
    for i in range(len(lines)):
        element = lines[i][0:-1]
        element = element.split(',')
        time.append(float(element[0]))
        y1.append(float(element[1]))
        y2.append(float(element[2]))
    return time, y1, y2


def plotting_curve(curve):
    time = curve[0]
    y1 = curve[1]
    y2 = curve[2]

    plt.plot(time, y1, label="Tension 1")
    plt.plot(time, y2, label="Tension 2")
    plt.xlabel('Temps')
    plt.ylabel('Tension')
    plt.title('Temps / Tension')
    plt.show()


def conv_four(name):
    with open(str(name) + ".csv", 'r') as file:
        lines = file.readlines()
        file.close()
    lines = lines[2:-1]
    freq = []
    y1 = []
    for i in range(len(lines)):
        element = lines[i][0:-1]
        element = element.split(',')
        freq.append(float(element[0]))
        if element[1] == '':
            y1.append(0)
        else:
            y1.append(float(element[1]))
    return freq, y1


def plotting_four(curve):
    freq = curve[0]
    y1 = curve[1]

    plt.plot(freq, y1)
    plt.ylabel('Tension')
    plt.xlabel('Fréquence')
    plt.title('Tension / Fréquence')
    plt.show()


#############################################
#            ALL IN ONE FUNCTIONS           #
#############################################


def csv_to_plot_tension(name):
    with open(str(name) + ".csv", 'r') as file:
        lines = file.readlines()
        file.close()
    lines = lines[2:-1]
    time = []
    y1 = []
    y2 = []
    for i in range(len(lines)):
        element = lines[i][0:-1]
        element = element.split(',')
        time.append(float(element[0]))
        y1.append(float(element[1]))
        y2.append(float(element[2]))
    plt.plot(time, y1, label="Tension 1")
    plt.plot(time, y2, label="Tension 2")
    plt.xlabel('Temps')
    plt.ylabel('Amplitude')
    plt.title('Temps / Amplitude')
    plt.show()


def csv_to_plot_four(name):
    with open(str(name) + ".csv", 'r') as file:
        lines = file.readlines()
        file.close()
    lines = lines[2:-1]
    freq = []
    y1 = []
    for i in range(len(lines)):
        element = lines[i][0:-1]
        element = element.split(',')
        freq.append(float(element[0]))
        if element[1] == '':
            y1.append(0)
        else:
            y1.append(float(element[1]))

    plt.plot(freq, y1)
    plt.ylabel('Amplitude')
    plt.xlabel('Fréquence')
    plt.title('Amplitude / Fréquence')
    plt.show()


def graph_computing(name):
    """
    Automatically plots the correct graphs depending on the input
    Usage: graph_computing("SpecRepTrian")
    """
    try:
        csv_to_plot_four(name)
    except FileNotFoundError:
        csv_to_plot_tension(name)


#############################################
#                CRAFTING                   #
#############################################

def average_computing(values):
    """
    :param values: list
    :return: float

    Returns the average value of a list as a float
    """
    return sum(values) / len(values)


def get_maximums(xList, yList):
    maximumsX = []
    maximumsY = []
    threshold = 3 * average_computing(yList)
    for i in range(len(yList)):
        if yList[i] >= threshold:
            maximumsX.append(xList[i])
            maximumsY.append(yList[i])
    return maximumsX, maximumsY


def refining(xList, yList):
    maximumsX = []
    maximumsY = []
    maxX = 0.0
    maxY = 0.0
    while xList:
        for i in range(len(yList)):
            if yList[i] >= maxY:
                return 0


# print(conv_four("SpecRepTrian")[1])
# print(average_computing(conv_four("SpecRepTrian")[1]))
lists = conv_four("SpecRepTrian")[0], conv_four("SpecRepTrian")[1]

results = get_maximums(lists[0], lists[1])
print(results)


"""
graph_computing("NomDuFichierEnRespectantLaCasseEtSans.csvALaFin")


"""
