class Shoe:
    def __init__(self, brand, size, style):
        self.brand = brand
        self.size = size
        self.style = style

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        if len(value) < 1 or len(value) > 30:
            raise ValueError("Brand must be between 1 and 30 characters")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Size must be a number")
        if value < 1 or value > 99:
            raise ValueError("Size must be between 1 and 99")
        self._size = value

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        if not isinstance(value, str):
            raise ValueError("Style must be a string")
        if len(value) < 1 or len(value) > 30:
            raise ValueError("Style must be between 1 and 30 characters")
        self._style = value