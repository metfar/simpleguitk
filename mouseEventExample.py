#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mouseEventExample.py

#
#  Copyright 2014 William Sebastian Martinez Bas <metfar@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


#  To hide debug info (key pressed and mouse event), touch NODBG
#  For no cursor, touch NOCURS
#  To hide Control Area, touch NOCTRL  (only if you do not use control area labels and buttons)

import time;
from math import *;


try:
    import simpleguitk as simplegui;
    Escape='escape';
    compenso=.9;
except:
    import simplegui;
    Escape=27;
    compenso=1;





false=False;
true=True;
cursor=false;
evento=false;
lgr=1;
#pseudoconstants and not-dependent variables
pulsos=5;

outMessage="Come back soon!!! Bye!!!";
WIDTH=800;
HEIGHT=400;
Space=32;
Enter=13;
Backspace=8;
conv=pi/180
charSize=17;
fontSize=charSize;
xi=0;yi=1;
xf=2;yf=3;
x=0;y=1;

goIn="getMouseFocus";goOver="mouseOver";goOut="lostMouseFocus";
Eventos=[goIn, goOver, goOut];
Exit="Exit";Off=Exit;
AddField="Add Field";
AddLabel="Add Label";
AddButton="Add Button";
#Arrays
Buttons=[Exit,False,
         AddField,False,
         AddLabel,False,
         AddButton,False,
         False,False];

#program variables
top=10;
lft=10;
row=5;
lines=5;
buttonsPerLine=2;
recentClick=0;
selected='_';


def isset(variable):
    try:
        return (variable in locals() or variable in globals());
    except:
        return(false);

#generalIsimas purpose functions
def major(a,b): return (a if a>b else b);
def minor(a,b): return (a if a<b else b);
def abs(a=0):   return (-a if a<0 else a);
def sign(a): return (-1 if a<0 else 1);

def mayor(a,b):
    return (False if type(a)!=type(b) else major(a,b));
def menor(a,b):
    return (False if type(a)!=type(b) else minor(a,b));


def translate (a=[(0,0),(1,1)],tx=0,ty=0):
    b=range(0,len(a));
    for f in range(0,len(a)):
        b[f]=(a[f][0]+tx,a[f][1]+ty);
    return (b);
def scale (a=[(0,0),(1,1)],ex=1,ey=1):
    b=range(0,len(a));
    for f in range(0,len(a)):
        b[f]=(a[f][0]*ex,a[f][1]*ey);
    return (b);
def rotatepoint(ix,iy,rxy=1):
    ang=(rxy%360)*conv;
    sa=sin(ang);
    ca=cos(ang);
    return(ix*ca-iy*sa,-ix*sa+iy*ca);

#general purpose functions
def circle(canvas,pos, radius=1, cCfa="white", cCircle="Seba"):
    global lgr;
    thin=lgr;
    try:
        canvas.draw_circle(pos, radius, thin, cCfa, cCircle);
    except:
        try:
            canvas.draw_circle(pos, radius, thin, cCfa);
        except:
            o=0;

def rectangle(canvas,a,b,Ink='White',Paper='Seba'):
    global lgr;
    try:
        canvas.draw_polygon([(a[x], a[y]), (a[x], b[y]),(b[x], b[y]),(b[x], a[y])], lgr, Ink,Paper);
    except:
        canvas.draw_polygon([(a[x], a[y]), (a[x], b[y]),(b[x], b[y]),(b[x], a[y])], lgr, Ink);



def line(canvas,a,b,Ink='Black'):
    global lgr;
    canvas.draw_line((a[x], a[y]), (b[x], b[y]),lgr, Ink);

def button(canvas,x0=0,y0=0,width=10,height=10,txt="Okjxxx",front='Black',back='White',e=5,face="#ccc",chrSize=-1):
    x1=x0+width; y1=y0+height;

    rectangle(canvas,(x0,y0),(x1,y1),front,back);


    for f in range(1,e):
        line(canvas,(x0+f, y0+f), (x0+f, y1-f),  grey[100-f*5]);
        line(canvas,(x0+f, y0+f), (x1-f, y0+f),  grey[100-f*5]);
        line(canvas,(x1-f, y0+f), (x1-f, y1-f),  grey[ 50+f*5]);
        line(canvas,(x0+f, y1-f), (x1-f, y1-f),  grey[ 50+f*5]);
    f=e;
    rectangle(canvas,(x0+f, y0+f), (x1-f, y1-f),face,back);

    if chrSize==-1:
        a=16;
        m=abs(y1-y0-f*4);
        while(frame.get_canvas_textwidth("X",a*compenso)>m and a>4):
            a-=1;
        #(y1-y0)/3
    else:
        a=charSize;

    text=txt;
    dx=abs(x1-x0-a/2);
    while (frame.get_canvas_textwidth(text, a*compenso)>dx):
        text=text[:-1];

    centrox=(x1+x0-e)/2; centroy=(y1+y0)/2;
    centra=abs(centrox-frame.get_canvas_textwidth(text, a*compenso)/2);
    canvas.draw_text(text, [centra+e/2,centroy+e], a*compenso, front);

def screener(canvas,l=0,t=0,w=100,h=50,txt="test"):
    button(canvas,l,t,w,h,txt,'#e34','FloralWhite',     6);
def screenerDisabled(canvas,l=0,t=0,w=100,h=50,txt="test"):
    button(canvas,l,t,w,h,txt,'#AAA','#ccc',5,"#ccc");
def buttonNotPressed(canvas,l=0,t=0,w=100,h=50,txt="test",charSize=-1):
    button(canvas,l,t,w,h,txt,'#EFF','#AAA',5,"#ccc",charSize);
def buttonPressed(canvas,l=0,t=0,w=100,h=50,txt="test",charSize=-1):
    button(canvas,l,t,w,h,txt,"#AAA",'#222',5,"#333",charSize);
def buttonSelected(canvas,l=0,t=0,w=100,h=50,txt="test",charSize=-1):
    global lgr;
    e=5;
    button(canvas,l,t,w,h,txt,'#EFF','#AAA',e);
    u=lgr; lgr=5; rectangle(canvas,l,t,l+w,t+h,'#E00','None');lgr=u;


#this app functions

def draw_handler(canvas):
    global charSize,recentClick,selected,flu,cursor,evento;

    #an.draw_circle((CX, CY), 145, 5, "#A9A9A9", "#A9A9A9");
    #an.draw_circle((CX, CY), 180, 5, "Black",'#FAFAD2');
    cl=10;#crux large
    cc=4;#crux center
    #canvas.draw_line((10, 20), (30, 40), 12, 'Red');
    canvas.draw_oval([(1, 20),(50, 40)], 2, 'Red', fill_color=None);

    try:
        flu;
    except:
        flu=0;

    #Buttons
    i=0;
    flet=0;
    nobut=false;
    for f in range(0,lines):
        for g in range(0,buttonsPerLine):
            if  (Buttons[i]!=False and
                Buttons[i]!=True and
                type(pB[i])==type([1,2,3,4,5])
                ):
                if (selected==Buttons[i] and
                      recentClick>0):
                        buttonPressed(canvas,
                                      pB[i][xi],
                                      pB[i][yi],
                                      pB[i][xf],
                                      pB[i][yf],
                                      Buttons[i],
                                      charSize*.66);
                        if Buttons[i]==Off:
                            if recentClick<=1:
                                exit(outMessage);
                            else:
                                flet=1;
                else:
                        buttonNotPressed(canvas,
                                         pB[i][xi],
                                         pB[i][yi],
                                         pB[i][xf],
                                         pB[i][yf],
                                         Buttons[i],
                                         charSize);

            i+=1;
            if flet==1:
                canvas.draw_text(outMessage,[(CX-frame.get_canvas_textwidth(outMessage,charSize)),CY],40, "#f00", "monospace");
                if   (flu==0):
                    flu=seconds;
                elif (seconds>flu+2):
                    exit(outMessage);

    #recuadro overbutton
    last=i;
    i=0;
    for f in range(0,lines):
        for g in range(0,buttonsPerLine):
            if  (Buttons[i]!=False and
                Buttons[i]!=True and
                type(pB[i])==type([1,2,3,4,5])
                ):
                p=pB[i];i+=1;

                if ( len(p)>=5 and cursor and
                cursor[x]>=p[xi] and
                cursor[x]<=p[xf] and
                cursor[y]>=p[yi] and
                cursor[y]<=p[yf]):
                    rectangle(
                        canvas,
                        (p[xi], p[yi]),
                        (p[xf], p[yf]),
                        '#538457');


    if recentClick<=1:
        selected=' ';


    #Cursor
    if (cursor):
        if      (evento==goOver):
            circle(canvas,(cursor[x],cursor[y]), 20, "#538457");
            line(canvas,(cursor[x]-cl-cc,cursor[y]),(cursor[x]-cc,cursor[y]), "#538457");
            line(canvas,(cursor[x]+cc,cursor[y]),(cursor[x]+cl+cc,cursor[y]), "#538457");
            line(canvas,(cursor[x],cursor[y]-cl-cc),(cursor[x],cursor[y]-cc), "#538457");
            line(canvas,(cursor[x],cursor[y]+cc),(cursor[x],cursor[y]+cl+cc), "#538457");
        elif    (evento==goOut):
            line(canvas,(cursor[x]-cl-cc,cursor[y]-cl-cc),(cursor[x]-cc,cursor[y]-cc), "#754835");
            line(canvas,(cursor[x]+cc,cursor[y]+cc),(cursor[x]+cl+cc,cursor[y]+cl+cc), "#754835");
            line(canvas,(cursor[x]+cl+cc,cursor[y]-cl-cc),(cursor[x]+cc,cursor[y]-cc), "#754835");
            line(canvas,(cursor[x]-cc,cursor[y]+cc),(cursor[x]-cl-cc,cursor[y]+cl+cc), "#754835");




def tecla(key):
    global selected,recentClick;
    if(key==Escape):
        selected=Exit;
        recentClick=pulsos;

def raton(position):
    global selected,recentClick;
    px=position[0];
    py=position[1];
    i=0;
    for f in range(0,lines):
        for g in range(0,buttonsPerLine):
            if (i<len(Buttons) and
                Buttons[i]!=False and
                Buttons[i]!=True and
                type(pB[i])==type([1,2,3,4])
                ):
                    l=pB[i][xi];
                    t=pB[i][yi];
                    w=pB[i][xf];
                    h=pB[i][yf];
                    if (l<=px) and (px<=l+w) and  (t<=py<=t+h):
                        selected=Buttons[i];
                        recentClick=pulsos;

            i+=1;


##program variables
maxRadio=major(WIDTH,HEIGHT);
pB=range(0,len(Buttons));
CX=WIDTH/2-charSize/2;
CY=HEIGHT/2+charSize;
pos=[(CX+12*charSize)/2,CY*1.25];
cdX=CX;
cdY=CY*1.4;
cSize=charSize*.5;
blue=range(0,256);
red=range(0,256);
green=range(0,256);
grey=range(0,256);

keyWidth=major(HEIGHT,WIDTH)/13
keyHeight=major(HEIGHT,WIDTH)/14

for f in range(0,256):
        col=str(hex(f));
        e=col.find('x')+1;
        col=col[e:4];
        grey[f]="#"+col+col+col;
        red[f]="#"+"ff"+col+col;
        green[f]="#"+col+"FF"+col;
        blue[f]="#"+col+col+"FF";

i=0;
for f in range(0,lines):
    for g in range(0,buttonsPerLine):
        if (i<len(Buttons) and
            Buttons[i]!=False and
            Buttons[i]!=True
            ):
               ajustx=ajusty=0;
               if (i+1<len(Buttons)  and not Buttons[i+1]):
                  ajustx=(row+keyWidth);
               if (i+buttonsPerLine<len(Buttons) and
                   Buttons[i+buttonsPerLine]==True):
                  ajusty=(keyHeight+row);
               cara=menor(keyWidth+ajustx,keyHeight+row)/2;
               if (cara)>(keyHeight-row):
                    cara-=16;
               pB[i]=[
                    lft+g*(keyWidth+row),
                    HEIGHT-keyHeight-top-(f*(keyHeight+row))-ajusty,
                    keyWidth+ajustx,
                    keyHeight+ajusty,
                    cara
                    ];
        i+=1;



def timex():
    global seconds;
    try: seconds+=1;
    except: seconds=0;

def ratonapretado(position):
    global selected,recentClick;
    print position;


frame = simplegui.create_frame('Start', WIDTH, HEIGHT);
frame.set_canvas_background("FloralWhite");
frame.set_mouseclick_handler(raton);

frame.set_keydown_handler(tecla);
frame.set_draw_handler(draw_handler);
can=frame._canvas._get_widget();


def enterB(event):
    global cursor,evento;
    cursor=(event.x, event.y);
    evento=goIn;


def leaveB(event):
    global cursor,evento;
    cursor=(event.x, event.y);
    evento=goOut;

def overB(event):
    global cursor,evento;
    cursor=(event.x, event.y);
    evento=goOver;



'''
{  2: "KeyPress",
   3: "KeyRelease",
   4: "ButtonPress",
   5: "ButtonRelease",
   6: "Motion",
   7: "Enter",
   8: "Leave",
   9: "FocusIn",
   10: "FocusOut",
   12: "Expose",
   15: "Visibility",
   17: "Destroy",
   18: "Unmap",
   19: "Map",
   21: "Reparent",
   22: "Configure",
   24: "Gravity",
   26: "Circulate",
   28: "Property",
   32: "Colormap",
   36: "Activate",
   37: "Deactivate",
   38: "MouseWheel"
}
'''
can.bind('<Enter>', enterB);
can.bind('<Leave>', leaveB);
can.bind('<Motion>', overB);

timer = simplegui.create_timer(500, timex);
timer.start();


print '\033[1;37m';

frame.start();
