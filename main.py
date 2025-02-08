from panda3d.core import Point3, Vec3, BitMask32
from panda3d.bullet import BulletWorld, BulletRigidBodyNode, BulletBoxShape
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Set up the Bullet physics world
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))
        
        # Create the ground
        ground_shape = BulletBoxShape(Vec3(50, 50, 1))
        ground_node = BulletRigidBodyNode('Ground')
        ground_node.addShape(ground_shape)
        ground_np = self.render.attachNewNode(ground_node)
        ground_np.setPos(0, 0, -2)
        ground_np.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(ground_node)
        
        # Create a box
        box_shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
        box_node = BulletRigidBodyNode('Box')
        box_node.setMass(1.0)
        box_node.addShape(box_shape)
        box_np = self.render.attachNewNode(box_node)
        box_np.setPos(0, 0, 2)
        box_np.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(box_node)
        
        # Add a task to update the physics world
        self.taskMgr.add(self.update_physics, 'UpdatePhysicsTask')
        
    def update_physics(self, task):
        dt = globalClock.getDt()
        self.world.doPhysics(dt)
        return Task.cont

app = MyApp()
app.run()
