import cv2, pandas, math, time
count = 0
#variable
coorlist = []
coordinate = {}   
coordinate ['x']=[]
coordinate ['y']=[]

def mouse_event (event, x, y, flags, params):
    global count
    global coordinate
    if (event== cv2.EVENT_LBUTTONDOWN):
        print (x,',', y,sep='')
        coorlist.append((x, y))
        coordinate['x'].append(x)
        coordinate['y'].append(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(count), (x, y), font, 0.5, (2, 5, 255), 2)
        cv2.imshow ('image', img)
        count+=1
    return

img = cv2.imread ('wallpaper.jpg', 1)
cv2.imshow('image', img)
cv2.setMouseCallback( 'image', mouse_event)
cv2.waitKey (0)
cv2.destroyAllWindows()

a=time.perf_counter()
#saving data into excel file
save= pandas.DataFrame(coordinate)
save.to_excel ('points.xlsx')

#algorithym for measure distance
max1 = tuple()
max2 = tuple()
max_d = -1
for tup1 in coorlist:
    for tup2 in coorlist:
        temp = math.dist (tup1, tup2)
        if temp>max_d:
            max_d = temp
            max1= tup1
            max2 = tup2
cv2.line (img, max1, max2, (233, 5, 6), 3)
cv2.imshow ('image', img)
b= time.perf_counter()
print ("the maximum distance is:", max_d)
print("cordinates are:",max1,max2)
print("Exection time of code is:",b-a)
