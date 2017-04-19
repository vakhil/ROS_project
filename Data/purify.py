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



#print len(load('Y_data'))
Y_final = []
#print (len(load('Y_data')[0]))
for j in range(0,len(load('X_data'))):

	temp = (load('X_data')[j]);
	#print len(temp)
	Y_final.append([])
	
	for k in temp[0] :
		Y_final[j].append(k)



	for i in range(0,4):
		Y_final[j].append(temp[1][i]);

	
	for k in temp[1][4][0]:
		Y_final[j].append(k)

	Y_final[j].append(temp[1][4][1])
	Y_final[j].append(temp[1][4][2])
	for k in temp[1][5]:
		Y_final[j].append(k)

	#print len(Y_final[j])

save('X_final',Y_final);

# for k in load('Y_data')[0][1] :
# 	print (k)