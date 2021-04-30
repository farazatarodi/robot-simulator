from robot import Robot

def test_moving():
    robot = Robot()

    assert robot.execute("0 0 NORTH A") == "0 1 NORTH" 
    assert robot.execute("7 3 NORTH RAALAL") == "9 4 WEST" 
    assert robot.execute("0 0 NORTH L") == "0 0 WEST" 
    assert robot.execute("0 0 NORTH R") == "0 0 EAST" 
    assert robot.execute("0 0 NORTH AAAALAAAALAAAALAAAAL") == "0 0 NORTH" 