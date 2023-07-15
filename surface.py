import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


def PickFirstNode(nodes):
    max_dist = 999
    first_node = None
    first_node_index = 0
    for i in range(0, nodes.__len__()):
        if nodes[i][1] >= 0:
            continue
        if abs(nodes[i][0]) < max_dist:
            max_dist = abs(nodes[i][0])
            first_node = np.array([nodes[i][0], nodes[i][1]])
            first_node_index = i
    return [first_node, first_node_index]


def vector_angle(v_1, v_2):
    mod_v_1 = math.sqrt(v_1[0]**2+v_1[1]**2)
    mod_v_2 = math.sqrt(v_2[0]**2+v_2[1]**2)
    return math.acos((v_1[0]*v_2[0]+v_1[1]*v_2[1])/mod_v_1/mod_v_2)


def CcwSort(node2sort, first_node, first_node_index):
    sorted_node = []
    last_node = first_node
    last_sec_node = None
    visited = []
    for i in range(0, node2sort.__len__()):
        visited.append(False)
    visited[first_node_index] = True
    visited_cnt = 1
    while visited_cnt < node2sort.__len__():
        max_dist = 999
        nearest_node = []
        nearest_node_index = 0
        sorted_node.append(last_node)
        for i in range(0, node2sort.__len__()):
            if visited[i] is True:
                continue
            dx = node2sort[i][0]-last_node[0]
            dy = node2sort[i][1]-last_node[1]
            dist = math.sqrt(dx**2+dy**2)
            if dist < max_dist:
                if dist >= 0.04:
                    continue
                if last_node[0] == first_node[0] and last_node[1] == first_node[1] and dx < 0:
                    continue
                if last_sec_node is not None:
                    vec_1 = np.array(
                        [last_node[0]-last_sec_node[0], last_node[1]-last_sec_node[1]])
                    vec_2 = np.array(
                        [node2sort[i][0]-last_node[0], node2sort[i][1]-last_node[1]])
                    if vector_angle(vec_1, vec_2) > math.pi/4*3:
                        continue
                max_dist = dist
                nearest_node = node2sort[i]
                nearest_node_index = i
        visited[nearest_node_index] = True
        visited_cnt += 1
        if nearest_node.__len__() == 0:
            continue
        if last_node is not None:
            last_sec_node = last_node
            last_node = nearest_node
    # sorted_node.append(last_node)
    return sorted_node


def move_nodes(src, b):
    res = []
    for i in src:
        res.append(np.array(i)+b)
    return res


def rotate_cw_nodes(src, angle):
    res = []
    R = np.array([[math.cos(-angle), -math.sin(-angle)],
                 [math.sin(-angle), math.cos(-angle)]])
    for i in src:
        res.append(np.matmul(R, i))
    return res


def generate_curve_from_sample(sample_nodes, is_ccw, tap_len=20, tap_dist=2/100, tap_len_const=20):
    curve_generated = []
    temp_nodes = sample_nodes
    start_index = 1
    if is_ccw:
        start_index = sample_nodes.__len__()-1
    angle_accumulated = 0
    while angle_accumulated < math.pi/2:
        tangent = abs(temp_nodes[start_index][0]/temp_nodes[start_index][1])
        d_theta = math.atan(tangent)
        radius = math.sqrt(temp_nodes[start_index]
                           [0]**2+temp_nodes[start_index][1]**2)
        s = radius*d_theta
        if not is_ccw:
            curve_generated = move_nodes(curve_generated, np.array([-s, 0]))
        else:
            curve_generated = move_nodes(curve_generated, np.array([s, 0]))
        curve_generated.append(np.array([0, -radius]))
        if not is_ccw:
            temp_nodes = rotate_cw_nodes(temp_nodes, d_theta)
        else:
            temp_nodes = rotate_cw_nodes(temp_nodes, -d_theta)
        angle_accumulated += d_theta
        if is_ccw is False:
            start_index += 1
        else:
            start_index -= 1
    last_node = None
    tap_mode = False
    while True and tap_len > 0:
        if tap_mode:
            curve_generated.append(np.array([temp_nodes[start_index][0], temp_nodes[start_index][1] -
                                             tap_dist*(tap_len_const-tap_len)/tap_len_const]))
            tap_len -= 1
        else:
            if last_node is not None:
                dy = temp_nodes[start_index][1]-last_node[1]
                if is_ccw is False:
                    if dy > 0:
                        tap_mode = True
                else:
                    if dy > 0:
                        tap_mode = True
            curve_generated.append(
                np.array([temp_nodes[start_index][0], temp_nodes[start_index][1]]))
        last_node = temp_nodes[start_index]
        if is_ccw is False:
            start_index += 1
        else:
            start_index -= 1
    return curve_generated


def generate_curve(filename, v_centerize=np.array([0, 0.05]), theta=math.pi/2):
    fp = open(filename, "r")
    text = fp.read()
    fp.close()
    all_nodes = []
    for i in text.split('\n'):
        if i == "":
            continue
        x, y = i.split(' ')
        v_0 = np.array([(float(x)), (float(y))])
        R = np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]])
        v_1 = np.matmul(R, v_0)+v_centerize
        all_nodes.append(v_1)
    first_node = []
    first_node_index = 0
    [first_node, first_node_index] = PickFirstNode(all_nodes)
    node_sorted = CcwSort(all_nodes, first_node, first_node_index)
    curve_a = generate_curve_from_sample(node_sorted, False)
    curve_a = move_nodes(curve_a, np.array([-curve_a[0][0], 0]))
    curve_b = generate_curve_from_sample(node_sorted, True)
    curve_b = move_nodes(curve_b, np.array([-curve_b[0][0], 0]))
    curve = curve_a+curve_b
    X = []
    Y = []
    for i in curve:
        X.append(i[0])
        Y.append(i[1])

    # plt.clf()  # 清除图像
    # axises = plt.gca()
    # axises.spines["right"].set_color('none')
    # axises.spines["top"].set_color('none')
    # axises.spines['left'].set_position(('data', 0))
    # axises.spines['bottom'].set_position(('data', 0))
    # axises.set_aspect(1)
    # plt.xlim(-0.3, 0.3)
    # plt.ylim(-0.2, 0.2)
    # plt.scatter(X, Y, marker='+')
    # plt.show()
    return curve


def generate_surface(menu):
    X = []
    Y = []
    Z = []
    dir_list = os.listdir(menu)
    step = 0
    for f in dir_list:
        f_path = os.path.join(menu, f)
        curve = generate_curve(f_path, v_centerize=np.array([0, 0]))
        print(f_path)
        for n in curve:
            X.append(step+0.15)
            Y.append(n[0])
            Z.append(n[1])
        step += 0.005
    fig = plt.figure()  # 创建一个画布figure，然后在这个画布上加各种元素。
    ax = Axes3D(fig)  # 将画布作用于 Axes3D 对象上。
    ax.scatter(X, Y, Z, c='g', marker='*')

    ax.set_xlabel('X label')  # 画出坐标轴
    ax.set_ylabel('Y label')
    ax.set_zlabel('Z label')
    ax.set_xlim(0.1,0.3)
    ax.set_ylim(-0.1,0.1)
    ax.set_zlim(-0.1,0)
    ax.set_box_aspect([1,1,1])

    plt.show()


generate_surface("dataset_test")
