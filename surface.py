import matplotlib.pyplot as plt
import numpy as np
import math
fp = open("dataset_test/splice_SPRING2001+0.txt", "r")
text = fp.read()
fp.close()
X = []
Y = []
for i in text.split('\n'):
    if i == "":
        continue
    x, y = i.split(' ')
    v_centerize=np.array([0,0.05])
    v_0=np.array([(float(x)),(float(y))])
    theta=math.pi/2
    R=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
    v_1=np.matmul(R,v_0)+v_centerize
    X.append(v_1[0])
    Y.append(v_1[1])
axises = plt.gca()
axises.spines["right"].set_color('none')
axises.spines["top"].set_color('none')
axises.spines['left'].set_position(('data', 0))
axises.spines['bottom'].set_position(('data', 0))
axises.set_aspect(1)
plt.xlim(-0.12, 0.12)
plt.ylim(-0.07, 0.18)
plt.scatter(X, Y)
first_node=[]
first_node_index=0
def PickFirstNode():
    global first_node,first_node_index
    max_dist=999
    for i in range(0,X.__len__()):
        if Y[i]>=0:
            continue
        if abs(X[i])<max_dist:
            max_dist=abs(X[i])
            first_node=np.array([X[i],Y[i]])
            first_node_index=i

node_sorted=[] #vectors
            
def CcwSort():
    global node_sorted
    last_node=first_node
    visited=[]
    for i in range(0,X.__len__()):
        visited.append(False)
    visited[first_node_index]=True
    visited_cnt=1
    while visited_cnt<X.__len__():
        max_dist=999
        nearest_node=[]
        nearest_node_index=0
        node_sorted.append(last_node)
        for i in range(0,X.__len__()):
            if visited[i] is True:
                continue
            dx=X[i]-last_node[0]
            dy=Y[i]-last_node[1]
            dist=math.sqrt(dx**2+dy**2)
            if dist<max_dist:
                max_dist=dist
                if last_node[0]==first_node[0] and last_node[1]==first_node[1] and dx<0:
                    continue
                nearest_node=[X[i],Y[i]]
                nearest_node_index=i
        visited[nearest_node_index]=True
        visited_cnt+=1
        last_node=nearest_node
    node_sorted.append(last_node)
    
PickFirstNode()
CcwSort()
plt.scatter([first_node[0]],[first_node[1]],marker='v')
for i in node_sorted:
    plt.ion()  #打开交互模式
    axises = plt.gca()
    axises.spines["right"].set_color('none')
    axises.spines["top"].set_color('none')
    axises.spines['left'].set_position(('data', 0))
    axises.spines['bottom'].set_position(('data', 0))
    axises.set_aspect(1)
    plt.xlim(-0.12, 0.12)
    plt.ylim(-0.07, 0.18)
    plt.scatter([i[0]],[i[1]],marker='+')
    plt.show()
    plt.pause(0.001)
    # plt.clf()  #清除图像

def move_nodes(src,b):
    res=[]
    for i in src:
        res.append(np.array(i)+b)
    return res

def rotate_cw_nodes(src,angle):
    res=[]
    R=np.array([[math.cos(-angle),-math.sin(-angle)],[math.sin(-angle),math.cos(-angle)]])
    for i in src:
        res.append(np.matmul(R,i))
    return res
        
curve=[]
def generate_curve(dir):
    global curve
    temp_nodes=node_sorted
    start_index=1
    if dir=='ccw':
        start_index=node_sorted.__len__()-1
    angle_accumulated=0
    while angle_accumulated<math.pi/2:
        tangent=abs(temp_nodes[start_index][0]/temp_nodes[start_index][1])
        d_theta=math.atan(tangent)
        radius=math.sqrt(temp_nodes[start_index][0]**2+temp_nodes[start_index][1]**2)
        s=radius*d_theta
        if dir=='cw':
            curve=move_nodes(curve,np.array([-s,0]))
        else:
            curve=move_nodes(curve,np.array([s,0]))
        curve.append(np.array([0,-radius]))
        if dir=='cw':
            temp_nodes=rotate_cw_nodes(temp_nodes,d_theta)
        else:
            temp_nodes=rotate_cw_nodes(temp_nodes,-d_theta)
        angle_accumulated+=d_theta
        if dir=='cw':
            start_index+=1
        else:
            start_index-=1
        
        # 演示功能
        plt.ion()  #打开交互模式
        plt.clf()  #清除图像
        axises = plt.gca()
        axises.spines["right"].set_color('none')
        axises.spines["top"].set_color('none')
        axises.spines['left'].set_position(('data', 0))
        axises.spines['bottom'].set_position(('data', 0))
        axises.set_aspect(1)
        plt.xlim(-0.3, 0.3)
        plt.ylim(-0.2, 0.2)
        # plt.scatter([i[0]],[i[1]],marker='+')
        for k in curve:
           plt.scatter([k[0]],[k[1]],marker='+')
        for k in temp_nodes:
            plt.scatter([k[0]],[k[1]],marker='.')
        plt.show()
        plt.pause(0.01)

generate_curve('cw')
curve=move_nodes(curve,np.array([-curve[0][0],0]))
generate_curve('ccw')
plt.pause(120)
    