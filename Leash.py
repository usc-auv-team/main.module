class Leash(object):
    def __init__(self, path_list, length, growth_rate):
        self.path = path_list
        self.desired_length = length
        self.growth_rate = growth_rate

        self.init()

    def init(self):
        self.current_segment_id = 0
        self.done_generating_targets = len(self.path) == 0

    def increment(self, amount):
        # if current segment has been used up
        if not self.current_segment.increment(amount):
            # if we are able to move on, do so
            if self.current_segment_id + 1 < len(self.path): self.current_segment_id += 1
            # otherwise, say we're done
            else: self.done_generating_targets = True

    def displacement_from_target(self, current_position):
        return magnitude(self.target - current_position)#TODO

    def maintain_length(self, current_position):
        while !self.done_generating_targets and self.displacement_from_target(current_position) < self.desired_length:
            self.increment(self.growth_rate)

    @property
    def target(self):
        return self.current_segment.target

    @property
    def independent_variable(self):
        return self.current_segment.independent_variable

    @property
    def current_segment(self):
        return self.path[self.current_segment_id]
