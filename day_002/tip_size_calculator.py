total = round(float(input('whats the size of the bill? ')), 2)

tip_size = 0
while tip_size not in {10, 12, 15}:
    tip_size = int(input('whats the size of the tip? 10/12/15? '))

number_of_people = int(input('how many to split up the bill? '))

total_with_tips = total + total * tip_size / 100
per_person = round((total_with_tips / number_of_people), 2)

print(f'it is {per_person} for each')
