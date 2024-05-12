from plivo.utils.validators import validate_args, required, of_type_exact

class Location:
    @validate_args(
        latitude=[required(of_type_exact(str))],
        longitude=[required(of_type_exact(str))],
        name=[required(of_type_exact(str))],
        address=[required(of_type_exact(str))]
    )
    def __init__(self, latitude, longitude, name, address):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.address = address
