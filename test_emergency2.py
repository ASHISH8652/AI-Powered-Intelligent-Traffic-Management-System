from traffic_ai.signal_control import EmergencyPriority

system = EmergencyPriority()

objects = [

    ("car","North"),

    ("truck","North"),

    ("bus","East"),

    ("ambulance","South")

]

decision = system.detect(objects)

print("="*60)

print("Emergency :", decision.emergency_detected)

print("Vehicle :", decision.vehicle_type)

print("Lane :", decision.lane)

print("Action :", decision.action)

print("Green Time :", decision.green_time)