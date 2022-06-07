class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # create convert_height here
    def convert_height(self):
        f_to_m_factor = 0.3048
        return self.height / f_to_m_factor
