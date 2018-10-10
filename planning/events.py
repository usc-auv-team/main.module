class Events(object):
    """
    Allows discrete actions to be performed at designated points along an autonomous path
    Unlike a Leash object, which constantly controls propulsion, an Events object only runs
    commands when triggers are reached.
    """
    def __init__(self, commands, triggers):
        """
        commands: a list of (lambda) functions that update the state of the drivetrain and other subsystems
        triggers: a list of percentages that indicate when/where to execute the commands
        """
        if len(commands) != len(triggers): raise ValueError('Each command must have a corresponding trigger.')

        self.commands = commands# list of actions to perform
        self.triggers = triggers# list of values where independent_variable triggers a command

        self.init()

    def init(self):
        self.step = -1
        self.done_running = len(self.commands) == 0

    def check(self, independent_variable):
        """
        If not done_running, increments step when independent_variable has reached a trigger
        If step is the last index of commands, done_running will be set to true

        independent_variable: should increase as autonomous progresses
        """
        # if done running, don't bother checking [counter + 1] because it will be out of bounds
        if not self.done_running and independent_variable >= self.triggers[self.step + 1]:
            # move on when the independent variable is greater than the trigger value
            self.step += 1
            if self.step + 2 > len(self.triggers): self.done_running = True

    def execute(self, propulsion, subsystems):
        """
        Runs the function in commands[step]
        """
        if self.step > -1: self.commands[self.step](propulsion, subsystems)
