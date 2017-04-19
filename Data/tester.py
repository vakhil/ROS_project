import cPickle
import math
import Features.a1 as a1
import Features.a2 as a2
import numpy as np
from sklearn.metrics import accuracy_score
with open('adaboost_classifier.pkl', 'rb') as fid:
    clf = cPickle.load(fid)


X= []
Y = []
j = 0
with open('room_test') as f:
	for line in f:
		
		points = [] ##It is a 2d array
		points_x_y = []
		if line[0] != 'H':
			X.append([])

			Y.append(0)
			parts = line.split('(')
			for i in range(1,len(parts)):
				value = parts[i].split(' , ')
				angle = value[0]
				angle = float(angle) 
				useless = value[1].split(' )')
				distance = float(useless[0])
				x = distance*math.cos(angle)
				y = distance*math.sin(angle)
				points.append([distance,angle])
				points_x_y.append([x,y])
			feat = a1.a1_9_10(points,len(points));
			feat_a_1 = ([a1.a1_1(points,len(points)),a1.a1_2(points,len(points)),a1.a1_3(points,len(points)),a1.a1_4(points,len(points)), a1.a1_5(points,len(points)),a1.a1_6(points,len(points)),a1.a1_7(points,len(points)), feat[0], feat[1], a1.a1_11(points,len(points)),a1.a1_12(points,len(points)),a1.a1_13(points,len(points)),a1.a1_14(points,len(points)),a1.a1_15(points,len(points)),a1.a1_16(points,len(points))])
			feat_a_2 = []
			feat_a_2.append(a2.a2_1(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_2(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_3(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_4(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_5(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_8(points_x_y,len(points_x_y)))
			net_feature = []
			net_feature.append(feat_a_1)
			net_feature.append(feat_a_2)


			for k in net_feature[0] :
				X[j].append(k)



			for i in range(0,4):
				X[j].append(net_feature[1][i]);

			
			for k in net_feature[1][4][0]:
				X[j].append(k)

			X[j].append(net_feature[1][4][1])
			X[j].append(net_feature[1][4][2])
			for k in net_feature[1][5]:
				X[j].append(k)

			j = j+ 1





			#X.append(net_feature)
			print 'OK'
print 'room done'





with open('door_test') as f:
	for line in f:
		
		points = [] ##It is a 2d array
		points_x_y = []
		if line[0] != 'H':
			X.append([])

			Y.append(2)
			parts = line.split('(')
			for i in range(1,len(parts)):
				value = parts[i].split(' , ')
				angle = value[0]
				angle = float(angle) 
				useless = value[1].split(' )')
				distance = float(useless[0])
				x = distance*math.cos(angle)
				y = distance*math.sin(angle)
				points.append([distance,angle])
				points_x_y.append([x,y])
			feat = a1.a1_9_10(points,len(points));
			feat_a_1 = ([a1.a1_1(points,len(points)),a1.a1_2(points,len(points)),a1.a1_3(points,len(points)),a1.a1_4(points,len(points)), a1.a1_5(points,len(points)),a1.a1_6(points,len(points)),a1.a1_7(points,len(points)), feat[0], feat[1], a1.a1_11(points,len(points)),a1.a1_12(points,len(points)),a1.a1_13(points,len(points)),a1.a1_14(points,len(points)),a1.a1_15(points,len(points)),a1.a1_16(points,len(points))])
			feat_a_2 = []
			feat_a_2.append(a2.a2_1(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_2(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_3(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_4(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_5(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_8(points_x_y,len(points_x_y)))
			net_feature = []
			net_feature.append(feat_a_1)
			net_feature.append(feat_a_2)


			for k in net_feature[0] :
				X[j].append(k)



			for i in range(0,4):
				X[j].append(net_feature[1][i]);

			
			for k in net_feature[1][4][0]:
				X[j].append(k)

			X[j].append(net_feature[1][4][1])
			X[j].append(net_feature[1][4][2])
			for k in net_feature[1][5]:
				X[j].append(k)

			j = j+ 1





			#X.append(net_feature)
			print 'OK'
print 'door done'



with open('corridor_test') as f:
	for line in f:
		
		points = [] ##It is a 2d array
		points_x_y = []
		if line[0] != 'H':
			X.append([])

			Y.append(1)
			parts = line.split('(')
			for i in range(1,len(parts)):
				value = parts[i].split(' , ')
				angle = value[0]
				angle = float(angle) 
				useless = value[1].split(' )')
				distance = float(useless[0])
				x = distance*math.cos(angle)
				y = distance*math.sin(angle)
				points.append([distance,angle])
				points_x_y.append([x,y])
			feat = a1.a1_9_10(points,len(points));
			feat_a_1 = ([a1.a1_1(points,len(points)),a1.a1_2(points,len(points)),a1.a1_3(points,len(points)),a1.a1_4(points,len(points)), a1.a1_5(points,len(points)),a1.a1_6(points,len(points)),a1.a1_7(points,len(points)), feat[0], feat[1], a1.a1_11(points,len(points)),a1.a1_12(points,len(points)),a1.a1_13(points,len(points)),a1.a1_14(points,len(points)),a1.a1_15(points,len(points)),a1.a1_16(points,len(points))])
			feat_a_2 = []
			feat_a_2.append(a2.a2_1(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_2(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_3(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_4(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_5(points_x_y,len(points_x_y)))
			feat_a_2.append(a2.a2_8(points_x_y,len(points_x_y)))
			net_feature = []
			net_feature.append(feat_a_1)
			net_feature.append(feat_a_2)


			for k in net_feature[0] :
				X[j].append(k)



			for i in range(0,4):
				X[j].append(net_feature[1][i]);

			
			for k in net_feature[1][4][0]:
				X[j].append(k)

			X[j].append(net_feature[1][4][1])
			X[j].append(net_feature[1][4][2])
			for k in net_feature[1][5]:
				X[j].append(k)

			j = j+ 1





			#X.append(net_feature)
			print 'OK'
print 'corridors done'

X = np.array(X);
y_pred = clf.predict(X);
print accuracy_score(Y, y_pred)