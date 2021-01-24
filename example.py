import URBasic
import time


host = '192.168.56.101'   #E.g. a Universal Robot offline simulator, please adjust to match your IP
acc = 1.2
vel = 0.8
        

if __name__ == '__main__':
    robot_model = URBasic.model.RobotModel()
    robot = URBasic.scriptExt.UrScriptExt(host=host,robotModel=robot_model)
    robot.robotConnector.DashboardClient.ur_close_popup()
    robot.reset_error()

    print('movel with pose specification')
    robot.movel(pose=[0.3,-0.3,0.3, 0,3.14,0], a=acc, v=vel)

    print('movej with joint specification')
    robot.movej(q=[-3.14,-1.,0.5, -1.,-1.5,0], a=acc, v=vel)

    print('movej with pose specification')
    robot.movej(pose=[0.3,0.3,0.3, 0,3.14,0], a=acc, v=vel)
                
    print('force_mode')
    robot.force_mode(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., -20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
    time.sleep(1)
    robot.end_force_mode()
    robot.close()
    