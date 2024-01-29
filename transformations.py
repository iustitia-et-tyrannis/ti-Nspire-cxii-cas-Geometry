x = 0
y = 0
m = 0
xvalues = [0]
yvalues = [0] #vars that are used later on in the program & I'm too lazy to add comments deal with it
bxvalues = []
byvalues = []
tt = [0] 
get_xyv = 0
xshift = 0
xshift = float(xshift)
yshift = 0
yshift = float(yshift)
yx = 0
yy = 0
hsp = 0
dhsp = 0
xpp = 0
ypp = 0
tnub = 0
get_xyv = 0

def over_x_axis(x,y,xvalues,yvalues): 
        y = str(-1*y)
        x= str(x)
        print(x+","+y)
        x = float(x)
        y = float(y)
        xvalues.append(x)
        yvalues.append(y)

def over_y_axis(x,y,xvalues,yvalues):
        x = str(-1*x)
        y= str(y)
        print(x+","+y)
        x = float(x)
        y = float(y)
        xvalues.append(x)
        yvalues.append(y)

def over_y_eq_x(yy,yx,x,y,xvalues,yvalues,xpp,ypp):
        xpp = int(input("x value point: "))
        ypp = int(input("y value point: "))
        x =str(x)
        y= str(y)
        print(y+","+x)
        xpp = float(yx + xpp)
        ypp = float(yy + ypp)
        xvalues.append(xpp)
        yvalues.append(ypp)
                                
def over_y_eq_neg_x(yy,yx,x,y,xvalues,yvalues,xpp,ypp):
        xpp = int(input("x value point: "))
        ypp = int(input("y value point: "))
        x = str(-1*x)
        y = str(-1*y)
        print(y+","+x)
        xpp = float(yx + xpp)
        ypp = float(yy + ypp)
        xvalues.append(xpp)
        yvalues.append(ypp)
                              

def rotate_90_deg_cw(yy,yx,x,y,xvalues,yvalues,xpp,ypp):
        xpp = int(input("x value point: "))
        ypp = int(input("y value point: "))
        x = str(-1*x)
        y= str(y)
        print(y+","+x)
        xpp = float(yx + xpp)
        ypp = float(yy + ypp)
        xvalues.append(xpp)
        yvalues.append(ypp)

def rotate_90_deg_cww(yy,yx,x,y,xvalues,yvalues,ypp,xpp):
        xpp = int(input("x value point: "))
        ypp = int(input("y value point: "))
        y = str(-1*y)
        x =str(x)
        print(y+","+x)
        xpp = float(yx + xpp)
        ypp = float(yy + ypp)
        xvalues.append(xpp)
        yvalues.append(ypp)

def rotate_180_deg(x,y,xvalues,yvalues,xpp,ypp):
        xpp = int(input("x value point: "))
        ypp = int(input("y value point: "))
        y = str(-1*y)
        x = str(-1*x)
        print(x+","+y)
        x = float(x)
        y = float(y)
        xpp = x + xpp
        ypp = y + ypp
        xvalues.append(xpp)
        yvalues.append(ypp)
        
def translations(x,y,xshift,yshift):
        xshift = float(input("x translation: "))
        yshift = float(input("y translation: "))
        x = str(x + xshift)
        y = str(y + yshift)
        print(x+","+y)
        x = float(x)
        y = float(y)
        xvalues.append(x)
        yvalues.append(y)

def reflet_onto_self(hsp,dhsp):
        hsp = float(input("How many points does the shape have: "))
        dhsp = 360/hsp
        lmg = 360/dhsp
        dhsp =str(dhsp)
        lmg = str(lmg*2) 
        print("the angle: "+dhsp+"deg")
        print("the amount of times: "+lmg)

def find_x_y(x,y):
        try:
                x = float(input("X Value: "))
                y = float(input("Y Value: "))
        except ValueError:
                print("Try again idiot")
                return
        print("1: over x axis")
        print("2: over y axis")
        print("3: y = x")
        print("4: y = -x")
        print("5: 90cw")
        print("6: 90ccw")
        print("7: 180 degs")
        print("8: translations")
        print("9: shape reflect")
        ask = input("type of Transfromation you want?: ")
        tt.append(ask)
        if ask == "x axis" or ask == "1":
                over_x_axis(x,y,xvalues,yvalues)
        elif ask == "y axis"  or ask == "2":
                over_y_axis(x,y,xvalues,yvalues)
        elif ask == "y=x"  or ask == "3":
                over_y_eq_x(yy,yx,x,y,xvalues,yvalues,xpp,ypp)
        elif ask == "y=-x"  or ask == "4":
                over_y_eq_neg_x(yy,yx,x,y,xvalues,yvalues,xpp,ypp)
        elif ask == "90cw"  or ask == "5":
                rotate_90_deg_cw(yx,yy,x,y,xvalues,yvalues,xpp,ypp)
        elif ask == "90 ccw"  or ask == "6":
                rotate_90_deg_cww(yy,yx,x,y,xvalues,yvalues,xpp,ypp)
        elif ask == "180"  or ask == "7": 
                rotate_180_deg(x,y,xvalues,yvalues,xpp,ypp)
        elif ask == "translations" or ask == "8":
                        translations(x,y,xshift,yshift)
        elif ask == "shape reflect" or ask =="9":                
                reflet_onto_self(hsp,dhsp)
        else:
                print("Nice try, try again")
                return

def transformations(x,y,m,tnub,yvalues,xvalues,tt,get_xyv):
    tnub = int(input("how many time do you want to loop: "))
    while m < tnub: 
        find_x_y(x,y)
        m = m+1
        if tnub == 0 or tnub == m:
            break
    coordsorno = input("Do you want all coords or no: ")
    if coordsorno == "yes" or coordsorno == "all" or coordsorno == "y" or coordsorno == "1":
        tnub = tnub + 1
        jkl =str(xvalues[1:tnub])
        jkm = str(yvalues[1:tnub])    
        jkn = str(tt[1:tnub])    
        print("x Value: "+jkl)
        print("y Value: "+jkm)
        print("Tmethod: "+jkn)
        print("(Tmethod = transfomation method)")
    elif coordsorno == "n" or coordsorno == "no"or coordsorno == "2":
        get_xyv = int(input("What coord (starts at 1): "))
        print(xvalues[get_xyv],yvalues[get_xyv],tt[get_xyv])
        
              
#Things you need to put in here do it at lunch or math
#Dialations
#make the code cleaner
# transformations(x,y,m,tnub,yvalues,xvalues,tt,get_xyv)
