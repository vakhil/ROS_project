from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
import math
import cmath
import numpy as np
import Features.a1 as a1
import Features.a2 as a2
import cPickle
import gzip

def load(file_name):
    # load the model
    stream = gzip.open(file_name, "rb")
    model = cPickle.load(stream)
    stream.close()
    return model


def save(file_name, model):
    # save the model
    stream = gzip.open(file_name, "wb")
    cPickle.dump(model, stream)
    stream.close()


X = []
Y = []
## 0 for room
## 1 for corridor
## 2 for door
with open('room_train') as f:
	for line in f:
		points = [] ##It is a 2d array
		points_x_y = []
		if line[0] != 'H':
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
			X.append(net_feature)
			print 'OK'
print 'room done'

with open('door_train') as f:
	for line in f:
		points = [] ##It is a 2d array
		points_x_y = []
		if line[0] != 'H':
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
			X.append(net_feature)

print 'door done'
with open('corridor_train') as f:
	for line in f:
		points = [] ##It is a 2d array
		points_x_y = []
		if line[0] != 'H':
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
			X.append(net_feature)
print 'corridor done'

save("Y_data", Y)
save("X_data", X)



#X = load('X_final')
#Y = load('Y_data')
X_final = np.array(X)
Y_final = np.array(Y)


clf = AdaBoostClassifier(n_estimators=100)
clf = clf.fit(X_final, Y_final)
with open('adaboost_classifier.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)  

    