from boids import ModelBuilder
from matplotlib import pyplot as plt
from matplotlib import animation


builda = ModelBuilder()
builda.start_model()
builda.set_starling_params(.01/50,10,100,.125/50)
builda.set_eagleish_params(100,5000,.00005)
builda.initialise_random(50)
builda.add_eagle(0,0,0,50)
Boids_Model = builda.finish()


figure=plt.figure()
axes=plt.axes(xlim=(-2000,1500), ylim=(-500,4000))
scatter=axes.scatter([b.position[0] for b in Boids_Model.boids],[b.position[1] for b in Boids_Model.boids])

def color(boid):
	if boid.species=="Eagle":
		return (1,0,0)
	return (0,0,1)

def animate(frame):
    Boids_Model.update()
    scatter.set_offsets([b.position for b in Boids_Model.boids])
    scatter.set_color([color(b) for b in Boids_Model.boids])


anim = animation.FuncAnimation(figure, animate,
        frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
