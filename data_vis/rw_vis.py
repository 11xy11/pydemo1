from matplotlib import pyplot as plt
from radomwalk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_num=list(range(rw.num_points))
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    # 隐藏坐标轴
    ax = plt.axes()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.scatter(rw.x_values, rw.y_values, c=point_num,
                cmap=plt.cm.Blues,
                edgecolor='none', s=15)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none',
                s=100)

    plt.show()
    label=input("Make another photo(y/n):")
    if label=='n':
        break;