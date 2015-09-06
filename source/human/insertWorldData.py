__author__ = 'rakesh'

from human.models import Phone, State
y = open("worlddata.txt", 'r')
for line in y:
    value = line.split('@')
    try:
        phoneNumber = value[0].strip()
        area_code = phoneNumber[0:3]
        address = value[1].strip()
        latitude = value[2].strip()
        longitude = value[3].strip()
        state_id = 'I'
        print phoneNumber, address, latitude, longitude, state_id
        state  = State.objects.get(state_name = state_id)
        p = Phone(phone_number=int(phoneNumber), area_code=int(area_code), location=address, latitude=latitude,longitude=longitude, state=state)
        p.save()
    except:
        pass


