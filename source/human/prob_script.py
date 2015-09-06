from human.models import *

states = State.objects.all()
phones = Phone.objects.all()


numbers = []

for phone in phones:
    if phone.frequency >=2:
        numbers.append(phone)

states_dict = {}

for state in states:
    if state not in states_dict:
        states_dict[state.state_name] = 0


for each in numbers:
    state = each.state.state_name
    states_dict[state] += 1


print states_dict


x_values = []
y_values = []


for key in states_dict:
    x_values.append(str(key))
    y_values.append(int(states_dict[key]))


print x_values
print y_values
