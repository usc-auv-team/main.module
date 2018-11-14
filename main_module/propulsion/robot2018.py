from main_module.angle import OneD

from ._abstract import Propulsion
class Robot2018(Propulsion):
    TRANSLATIONAL_P = 0.05
    TRANSLATIONAL_I = 0.0
    TRANSLATIONAL_D = 0.0

    ROTATIONAL_P = 0.05
    ROTATIONAL_I = 0.0
    ROTATIONAL_D = 0.0

    MAX_YAW_ERROR_WHILE_TRANSLATING = 5.0# Degrees

    def __init__(self, gyro):
        self.gyro = gyro

        self.speed_target = 0.0
        self.angular_speed_target = 0.0
        self.depth_speed_target = 0.0

    def set_speed(self, speed):
        """See comments in abstract"""
        self.speed_target = speed

    def set_spin(self, spin):
        """See comments in abstract"""
        self.angular_speed_target = spin

    def set_depth_speed(self, speed):
        """See comments in abstract"""
        self.depth_speed_target = speed

    def correct_for(self, error_vector, P = 0.05):
        """See comments in abstract"""
        self.set_depth_speed(error_vector.z*P)

        target_yaw = OneD.convert_to_angle(error_vector.x, error_vector.y)

        if abs(self.travel_towards(target_yaw)) < Robot2018.MAX_YAW_ERROR_WHILE_TRANSLATING:
            error_magnitude_xy = (error_vector.x**2 + error_vector.y**2)**0.5
            self.set_speed(error_magnitude_xy*P)# TODO use full PID

    def travel_towards(self, heading):
        """See comments in abstract"""
        return self.face(heading)

    def face(self, heading, P = 0.05):
        """See comments in abstract"""
        error = self.gyro.path_to([0.0, 0.0, heading])[2]
        self.set_spin(error*P)# TODO use full PID
        return error
