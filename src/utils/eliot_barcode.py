def build_eliot_barcode(mts: str):
    meters = mts
    size = 6
    if len(meters) > size:
        raise Exception('Meters are bigger')
    if size > len(meters):
        length = size - len(meters)
        list_zeros = ['0'] * length
        meters = ''.join(list_zeros) + meters
    return meters
