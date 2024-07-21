from time import sleep

try:
    from explorerhat import motor

    def set_speeds(power_left, power_right):
        motor.one.speed(-power_right)
        motor.two.speed(power_left)

    def stop_motors():
        motor.stop()

except ImportError:
    def set_speeds(power_left, power_right):
        print('Left: {}, Right: {}'.format(power_left, power_right))
        sleep(0.1)

    def stop_motors():
        print('Motors stopping')

from approxeng.input.selectbinder import ControllerResource

class RobotStopException(Exception):
    pass

def mixer(yaw, throttle, max_power=100):
    left = throttle + yaw
    right = throttle - yaw
    scale = float(max_power) / max(1, abs(left), abs(right))
    return int(left * scale), int(right * scale)

try:
    while True:
        try:
            with ControllerResource(dead_zone=0.1, hot_zone=0.2) as joystick:
                while joystick.connected:
                    x_axis, y_axis = joystick['lx', 'ly']
                    power_left, power_right = mixer(yaw=x_axis, throttle=y_axis)
                    set_speeds(power_left, power_right)
                    joystick.check_presses()
                    if joystick.has_presses:
                        print(joystick.presses)
                    if 'home' in joystick.presses:
                        raise RobotStopException()
        except IOError:
            print('No controller found yet')
            sleep(1)
except RobotStopException:
    stop_motors()
