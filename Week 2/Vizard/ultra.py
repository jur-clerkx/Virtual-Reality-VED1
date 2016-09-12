import viz
import vizcam
import oculus

#Setup world
viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor(viz.SKYBLUE)
viz.go(viz.FULLSCREEN)
viz.mouse.setVisible(False)
view = viz.MainView

#Setup rift
viz.MainView.setPosition( [5, 1.82, -15] )
hmd = oculus.Rift()
viz.link(hmd.getSensor(), viz.MainView)

#Add playground
viz.addChild('playground.wrl')

#Setup oculus and controls
vizcam.KeyboardCamera(forward='w',backward='s',left='a',right='d',up=None,down=None,turnRight=None,turnLeft=None,pitchDown=None,pitchUp=None,rollRight=None,rollLeft=None)
def mousemove(e):
	euler = view.get(viz.HEAD_EULER)
	euler[0] += e.dx*0.1
	euler[1] += 0
	euler[1] = viz.clamp(euler[1],-90.0,90.0)
	view.setEuler(euler,viz.HEAD_ORI) 

viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)



#Setup collision and gravity
viz.MainView.collision( viz.ON )
viz.MainView.gravity(10)
viz.MainView.stepsize(0.5)

#Setup lightning
headLight = viz.MainView.getHeadLight() 
headLight.disable()
myLight = viz.addLight() 
myLight.setEuler(-15 ,15 ,15)

