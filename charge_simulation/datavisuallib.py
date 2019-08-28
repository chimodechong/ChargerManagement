import matplotlib.pyplot as plt

def regulate(max_num, min_num, values):
    max_value = max(values)
    min_value = min(values)
    print("max value: " + str(max_value))
    print("min value: " + str(min_value))
    result = []
    for value in values:
        temp_value = round((max_num - min_num) * (value - min_value) / (max_value - min_value)) + min_num
        result.append(temp_value)
    #print(result)
    return result

def show_scatter(x_axis, y_axis, records):
    """
    this function is used to visualize and check the expasion of dataset
    records should be in form [{data_dict}] or iterator
    x_axis, y_axis should be among: [ici, icv, ibv, ibt, itt, freq, temp_th]
    """
    x_values = []
    y_values = []
    x_y = []
    individual_x_y = set()
    counts = dict()
    count_values = []

    print(len(records), " totally")

    for record in records:
        x_values.append(record[x_axis])
        y_values.append(record[y_axis])
        x_y.append((record[x_axis], record[y_axis]))
        individual_x_y.add((record[x_axis], record[y_axis]))
    for record in x_y:
        try:
            counts[record] += 1
        except:
            counts[record] = 1
    x_values = []
    y_values = []

    print("Got " + str(len(individual_x_y)) + " individual records")
    for x_y_pair in individual_x_y:
        x_values.append(x_y_pair[0])
        y_values.append(x_y_pair[1])
        count_values.append(counts[x_y_pair])

    # change darkness of color here
    count_values = regulate(20000, 5000, count_values)

    # this is to make sure plt renders the tintest color as it is
    x_values.append(max(x_values) + 1)
    y_values.append(max(y_values) + 1)
    count_values.append(0)

    plt.scatter(x_values, y_values, c=count_values, cmap=plt.cm.Blues, s=10)  # 传入两个列表，列表x_values的元素作为x坐标,列表y_values的元素作为y坐标，两个组合成一个点的坐标，所以一共有5个点
    plt.title("Scatter darker=more data", fontsize=24)  # 指定标题，并设置标题字体大小
    plt.xlabel(x_axis, fontsize=14)  # 指定X坐标轴的标签，并设置标签字体大小
    plt.ylabel(y_axis, fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小
    plt.tick_params(axis='both', labelsize=10)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
    plt.show()