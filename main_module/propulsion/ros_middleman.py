from main_module.angle import OneD

from ._abstract import Propulsion
class Middleman(Propulsion):
    TRANSLATIONAL_P = 0.05
    TRANSLATIONAL_I = 0.0
    TRANSLATIONAL_D = 0.0

    ROTATIONAL_P = 0.05
    ROTATIONAL_I = 0.0
    ROTATIONAL_D = 0.0

    MAX_YAW_ERROR_WHILE_MOVING = 5.0# Degrees

    def __init__(self, gyro):
        self.gyro = gyro

        self.desired_delta_depth = 0.0
        self.yaw_target = 0.0
        self.speed_target = 0.0

    def set_speed(self, speed):
        """See comments in abstract"""
        self.speed_target = speed

    def correct_for(self, error_vector, P = Middleman.TRANSLATIONAL_P):
        """See comments in abstract"""
        self.desired_delta_depth = error_vector.z
        yaw_target = OneD.convert_to_angle(error_vector.x, error_vector.y)

        if abs(self.travel_towards(yaw_target)) < Middleman.MAX_YAW_ERROR_WHILE_MOVING:
            error_magnitude_xy = (error_vector.x**2 + error_vector.y**2)**0.5
            self.set_speed(error_magnitude_xy*P)# TODO use full PID

    def travel_towards(self, heading):
        """See comments in abstract"""
        return self.face(heading)

    def face(self, heading):
        """See comments in abstract"""
        self.yaw_target = heading
        error = self.gyro.path_to([0.0, 0.0, heading])[2]
        return error

    def bundle_for_ros(self, message):
        message.desired_delta_depth_meters = self.desired_delta_depth
        message.desired_degrees_yaw = self.yaw_target
        message.desired_percent_speed = 100.0*self.speed_target
        return message

    def set_spin(self, spin):
        pass

    def set_depth_speed(self, speed):
        pass

    def complete_loop_update(self):
        pass

    @classmethod
    def configure_class_params(cls, translational_pid, rotational_pid, max_yaw_error_while_moving):
        cls.TRANSLATIONAL_P, cls.TRANSLATIONAL_I, cls.TRANSLATIONAL_D = translational_pid
        cls.ROTATIONAL_P, cls.ROTATIONAL_I, cls.ROTATIONAL_D = rotational_pid
        cls.MAX_YAW_ERROR_WHILE_MOVING = max_yaw_error_while_moving
