from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
class ZD(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            self.world_position += self.forward * self.speed * time.dt
            if self.y>3:
                help_position = self.world_position-(0,2,0)
            else:
                help_position = self.world_position
            destroy(self)
            if help_position[1]<0:
                help_position=(help_position[0],0.5,help_position[2])
            zdpd.position=help_position
class DZD(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
            if self.rotation_x < 90:
                self.rotation_x+=0.03
        else:
            self.world_position += self.forward * self.speed * time.dt*self.lifetime
            if self.y>3:
                help_position = self.world_position-(0,2,0)
            else:
                help_position = self.world_position
            destroy(self)
            if help_position[1]<0:
                help_position=(help_position[0],0.5,help_position[2])
            dzdpd.position=help_position
class PD(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
            if self.rotation_x < 90:
                self.rotation_x+=0.1
        else:
            self.world_position += self.forward * self.speed * time.dt*self.lifetime
            if self.y>3:
                help_position = self.world_position-(0,2,0)
            else:
                help_position = self.world_position
            destroy(self)
            if help_position[1]<0:
                help_position=(help_position[0],0.5,help_position[2])
            invoke(Audio, 'files/sound/boom.ogg')
            boom = Entity(model = 'cube',texture = 'files/image/boom.png',position = help_position)
            pdpd.position=help_position
            destroy(boom,delay = 5)
class SLD(Entity):
    def __init__(self,speed=150,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
            if self.rotation_x < 90:
                self.rotation_x+=0.6
        else:
            self.world_position += self.forward * self.speed * time.dt*self.lifetime
            if self.y>3:
                help_position = self.world_position-(0,2,0)
            else:
                help_position = self.world_position
            destroy(self)
            if help_position[1]<0:
                help_position=(help_position[0],0.5,help_position[2])
            invoke(Audio, 'files/sound/boom.ogg')
            boom = Entity(model = 'cube',texture = 'files/image/boom.png',position = help_position)
            sdpd.position=help_position
            destroy(boom,delay = 5)
class DL(Entity):
    def __init__(self):
        super().__init__(model='files/3d/lei.obj',scale=0.5,color=color.orange,position=(player.x+1,0.5,player.z+1))
    def update(self):
        help_position=self.position
        if (abs(self.x-player.x)<0.5 and abs(self.z-player.z)<0.5)or((abs(self.x-dlpd.x)<7 and abs(self.y-dlpd.y)<4 and abs(self.z-dlpd.z)<7))or((abs(self.x-sdpd.x)<8 and abs(self.y-sdpd.y)<5 and abs(self.z-sdpd.z)<8))or((abs(self.x-zdpd.x)<3 and abs(self.y-zdpd.y)<3 and abs(self.z-zdpd.z)<3))or((abs(self.x-pdpd.x)<15 and abs(self.y-pdpd.y)<5 and abs(self.z-pdpd.z)<15))or((abs(player.x-dzdpd.x)<3 and abs(player.y-dzdpd.y)<3 and abs(player.z-dzdpd.z)<3))or((abs(self.x-tzb.x)<3 and abs(self.y-tzb.y)<3 and abs(self.z-tzb.z)<3))or((abs(self.x-bzb.x)<3 and abs(self.y-bzb.y)<3 and abs(self.z-bzb.z)<3)):
            destroy(self)
            invoke(Audio, 'files/sound/boom.ogg')
            boom = Entity(model = 'cube',texture = 'files/image/boom.png',position = help_position)
            dlpd.position=help_position
            destroy(boom,delay = 5)
class tk(Entity):
    def __init__(self,time=2,life=4):
        super().__init__(model='files/3d/tk.obj',collider='box',rotation_y=180,position=(-130,1.5,random.randint(-45,45)))
        self.time=time
        self.life=life
    def update(self):
        if lifefz.x==1:
           destroy(self,delay=0.25)
        tzb.position=self.position
        self.x+=self.life/20
        if self.x>130:
            player.fx-=0.05
            destroy(self,delay=0.25)
        if self.time!=0:
            self.time-=0.01
        if self.time<0:
            self.time=0
        if self.time==0:
            self.time=6
            self.look_at(player,axis='left')
            invoke(Audio, 'files/sound/fs.ogg')
            PD(model="files/3d/hjd.obj",
                   scale=0.1,
                   position=self.world_position+(0,2.5,0),
                   rotation=self.world_rotation-((((pow((self.x-player.x)**2+(self.z-player.z)**2,0.5)/2)/36)*0.1)+3,90,0))
            self.rotation=(0,180,0)
        if ((abs(self.x-dlpd.x)<8 and abs(self.y-dlpd.y)<5 and abs(self.z-dlpd.z)<8))or((abs(self.x-sdpd.x)<8 and abs(self.y-sdpd.y)<5 and abs(self.z-sdpd.z)<8))or((abs(self.x-pdpd.x)<15 and abs(self.y-pdpd.y)<5 and abs(self.z-pdpd.z)<15)):
            self.life-=0.5
        if ((abs(self.x-zdpd.x)<8 and abs(self.y-zdpd.y)<5 and abs(self.z-zdpd.z)<8)):
            self.life-=0.01
        if self.life<0:
            self.life=0
            destroy(self,delay=0.25)
            player.jif+=1
class b(Entity):
    def __init__(self,time=2,life=1):
        super().__init__(model='files/3d/b.obj',scale=0.5,collider='box',rotation_y=90,color=color.orange,position=(-130,1.5,random.randint(-45,45)))
        self.time=time
        self.life=life
    def update(self):
        if lifefz.x==1:
           destroy(self,delay=0.25)
        bzb.position=self.position
        self.x+=0.1
        if self.x>130:
            player.fx-=0.05
            destroy(self,delay=0.25)
        if self.time!=0:
            self.time-=0.01
        if self.time<0:
            self.time=0
        if self.time==0:
            self.time=2
            invoke(Audio, 'files/sound/fs.ogg')
            self.look_at(player,axis='left')
            invoke(Audio, 'files/sound/fs.ogg')
            DZD(model="sphere",
                   scale=0.1,
                   position=self.world_position+(0,2.5,0),
                   rotation=self.world_rotation-((((pow((self.x-player.x)**2+(self.z-player.z)**2,0.5)/2)/36)*0.1)+3,90,0))
            self.rotation_y=90
        if ((abs(self.x-dlpd.x)<7 and abs(self.y-dlpd.y)<4 and abs(self.z-dlpd.z)<7))or((abs(self.x-sdpd.x)<8 and abs(self.y-sdpd.y)<5 and abs(self.z-sdpd.z)<8))or((abs(self.x-pdpd.x)<15 and abs(self.y-pdpd.y)<5 and abs(self.z-pdpd.z)<15)):
            self.life-=0.5
        if ((abs(self.x-zdpd.x)<8 and abs(self.y-zdpd.y)<5 and abs(self.z-zdpd.z)<8)):
            self.life-=0.01
        if self.life<0:
            self.life=0
            destroy(self,delay=0.25)
            player.jif+=0.5
class kt(Entity):
    def __init__(self):
        super().__init__(model='files/3d/kt.obj',collider='box',color=color.red,position=(random.randint(100,130),100,random.randint(-45,45)))
    def update(self):
        if self.y>1.5:
            self.y-=0.1
        if abs(self.x-player.x)<3:
            if abs(self.z-player.z)<3:
                if abs(self.y-player.y)<2:
                    if pd.x<7:
                        pd.x+=3
                    else:
                        pd.x=10
                    if sd.x<15:
                        sd.x+=5
                    else:
                        sd.x=20
                    if zd.x<40:
                        zd.x+=30
                    else:
                        zd.x=70
                    if player.life<5:
                        player.life+=1
                    if dl.x<5:
                        dl.x+=5
                    else:
                        dl.x=10
                    destroy(self)
def input(key):
    if key == "escape":
        quit()
    if key == "1":
    	flag.x=1
    	hjt.y=-100
    	sld.y=-100
    	qiang.y=1.3
    if key == "2":
    	flag.x=2
    	qiang.y=-100
    	sld.y=-100
    	hjt.y=-0.5
    if key == "3":
    	flag.x=3
    	qiang.y=-100
    	hjt.y=-100
    	sld.y=1.5
    if key == 'left mouse down' and flag.x==1 and zd.x>0:
        invoke(Audio, 'files/sound/fs.ogg')
        zd.x-=1
        ZD(model="sphere",
               scale=1,
               color=color.orange,
               position=player.camera_pivot.world_position,
               rotation=player.camera_pivot.world_rotation)
    if key == 'left mouse down' and flag.x==2 and pd.x>0 and pd.z==0:
        invoke(Audio, 'files/sound/fs.ogg')
        pd.x-=1
        pd.z=1.5
        PD(model="files/3d/hjd.obj",
               scale=0.1,
               position=player.camera_pivot.world_position,
               rotation=player.camera_pivot.world_rotation)
    if (key == 'left mouse down' or key=='right mouse down') and flag.x==3 and sd.x>0 and sd.z==0:
        invoke(Audio, 'files/sound/fs.ogg')
        sd.x-=1
        sd.z=1
        SLD(model="files/3d/sld.obj",
               scale=0.2,
               position=player.camera_pivot.world_position,
               rotation=player.camera_pivot.world_rotation)
    if key == 'l' and dl.x>0:
        dl.x-=1
        DL()
def update():
    if ((abs(player.x-dlpd.x)<7 and abs(player.y-dlpd.y)<4 and abs(player.z-dlpd.z)<7))or((abs(player.x-sdpd.x)<8 and abs(player.y-sdpd.y)<5 and abs(player.z-sdpd.z)<8))or((abs(player.x-pdpd.x)<15 and abs(player.y-pdpd.y)<5 and abs(player.z-pdpd.z)<15)):
        player.life-=0.1
    if ((abs(player.x-dzdpd.x)<8 and abs(player.y-dzdpd.y)<5 and abs(player.z-dzdpd.z)<8)):
        player.life-=0.01
    pdsl.text=('paodanshuliang:'+str(int(pd.x))+'/10')
    pdcd.text=('paodanCD:'+str(round(pd.z,2)))
    if pd.z!=0 and flag.x==2:
        pd.z-=0.01
    if pd.z!=0 and flag.x!=2:
    	pd.z=1.5
    if pd.z<0:
        pd.z=0
    sdsl.text=('shouliudanshuliang:'+str(int(sd.x))+'/20')
    sdcd.text=('shouliudanCD:'+str(round(sd.z,2)))
    if sd.z!=0 and flag.x==3:
        sd.z-=0.01
    if sd.z!=0 and flag.x!=3:
    	sd.z=1
    if sd.z<0:
        sd.z=0
    if sd.x==0:
        sld.y=-100
    zdsl.text=('zidanshuliang:'+str(int(zd.x))+'/70')
    life.text=('life:'+str(int(player.life)))
    dlsl.text=('dileishuliang:'+str(int(dl.x))+'/10')
    jifen.text=('jifen:'+str(int(player.jif)))
    fangxianlife.text=('fangxianlife:'+str(int(player.fx)))
    if (int(player.life)==0 or int(player.fx)==0) and lifefz.x==0:
    	lifefz.x=1
    	invoke(Audio, 'files/sound/no.ogg')
    player.speed=player.life*2
    if int(player.life)==0 or player.life<0:
        player.life=0
    if kttime.x!=0:
        kttime.x-=0.01
    if kttime.x<0:
        kttime.x=0
    if kttime.x==0 and lifefz.x==0:
        kt()
        kttime.x=15
    if dlpd.y!=-20:
        if dlpd.rotation_z<0:
            dlpd.rotation_z=0
        if dlpd.rotation_z!=0:
            dlpd.rotation_z-=0.01
        if dlpd.rotation_z==0:
            dlpd.y=-20
            dlpd.rotation_z=0.1
    if sdpd.y!=-20:
        if sdpd.rotation_z<0:
            sdpd.rotation_z=0
        if sdpd.rotation_z!=0:
            sdpd.rotation_z-=0.01
        if sdpd.rotation_z==0:
            sdpd.y=-20
            sdpd.rotation_z=0.1
    if zdpd.y!=-20:
        if zdpd.rotation_z<0:
            zdpd.rotation_z=0
        if zdpd.rotation_z!=0:
            zdpd.rotation_z-=0.01
        if zdpd.rotation_z==0:
            zdpd.y=-20
            zdpd.rotation_z=0.1
    if pdpd.y!=-20:
        if pdpd.rotation_z<0:
            pdpd.rotation_z=0
        if pdpd.rotation_z!=0:
            pdpd.rotation_z-=0.01
        if pdpd.rotation_z==0:
            pdpd.y=-20
            pdpd.rotation_z=0.1
    if cb.x!=0:
        cb.x-=0.01
    if cb.x<0:
        cb.x=0
    if cb.x==0 and lifefz.x==0:
        cb.x=5
        b()
    if cb.z!=0:
        cb.z-=0.01
    if cb.z<0:
        cb.z=0
    if cb.z==0 and lifefz.x==0:
        cb.z=7
        tk()
app = Ursina()
Sky()
player = FirstPersonController(speed=5,life=5,jif=0,x=130,fx=5)
ground1 = Entity(model = 'cube',scale = (300,1,100),color = color.lime,texture = "td.png",texture_scale = (300,100),collider="box")
qiang = Entity(model = 'files/3d/q.obj',parent = player,position = (0.3,1.3,0),rotation_y = -10,color = color.white)
hjt = Entity(model = 'files/3d/hjt.obj',parent = player,position = (1,-100,0),rotation_y = 170,color = color.orange,scale=0.7)
sld = Entity(model = 'files/3d/sld.obj',parent = player,position = (0.3,-100,0.5),scale=0.2,rotation_y=180,color = color.white)
zdpd = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
pdpd = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
sdpd = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
dlpd = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
dzdpd = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
tzb = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
bzb = Entity(model = 'cube',scale=0.001,position=(0,-20,0))
flag=Entity(model = 'cube',position=(1,-5,0))
pd=Entity(model = 'cube',position=(10,-5,0))
pdsl=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.46))
pdcd=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.4))
sd=Entity(model = 'cube',position=(20,-5,0))
sdsl=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.34))
sdcd=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.28))
zd=Entity(model = 'cube',position=(40,-5,0))
zdsl=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.22))
dl=Entity(model = 'cube',position=(5,-5,0))
dlsl=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.16))
life=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.1))
jifen=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.04))
fangxianlife=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,0.02))
lifefz=Entity(model = 'cube',position=(0,-5,0))
kttime=Entity(model = 'cube',position=(0,-5,0))
cb=Entity(model = 'cube',position=(0,-5,0))
x=140
y=1
z=0
m = Entity(model='cube', scale=(10, 1, 10), color=color.white, texture="td.png", texture_scale=(10, 10),
               collider="box", position=(x, y, z))
m = Entity(model='cube', scale=(10, 8, 1), color=color.white, texture="td.png", texture_scale=(10, 8),
               collider="box", position=(x, y + 3, z + 5))
m = Entity(model='cube', scale=(10, 8, 1), color=color.white, texture="td.png", texture_scale=(10, 8),
               collider="box", position=(x, y + 3, z - 5))
m = Entity(model='cube', scale=(1, 8, 10), color=color.white, texture="td.png", texture_scale=(10, 8),
               collider="box", position=(x + 5, y + 3, z))
m = Entity(model='cube', scale=(1, 8, 4), color=color.white, texture="td.png", texture_scale=(8, 4),
               collider="box",
               position=(x - 5, y + 3, z + 3))
m = Entity(model='cube', scale=(1, 8, 4), color=color.white, texture="td.png", texture_scale=(8, 4),
               collider="box",
               position=(x - 5, y + 3, z - 3))
m = Entity(model='cube', scale=(1, 4, 2), color=color.white, texture="td.png", texture_scale=(4, 2),
               collider="box",
               position=(x - 5, y + 6, z))
m = Entity(model='cube', scale=(10, 1, 8), color=color.white, texture="td.png", texture_scale=(10, 8),
               collider="box", position=(x, y + 6, z - 1))
m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
               collider="box",
               position=(x + 4, y + 6, z + 4))
m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
               collider="box",
               position=(x + 3, y + 5, z + 4))
m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
               collider="box",
               position=(x + 2, y + 4, z + 4))
m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
               collider="box",
               position=(x + 1, y + 3, z + 4))
m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
               collider="box",
               position=(x, y + 2, z + 4))
m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
               collider="box",
               position=(x - 1, y + 1, z + 4))
app.run()