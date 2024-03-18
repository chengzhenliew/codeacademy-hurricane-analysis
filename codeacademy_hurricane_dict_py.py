#codeacademy_hurricane_dict_py 

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def damage_convert(list_of_damages):
  damages_float = []
  for item in list_of_damages:
    if item == 'Damages not recorded':
      damages_float.append(item)
    elif 'M' in item:
      damages_float.append(float(item[:-1]) * 10 ** 6)
    elif 'B' in item:
      damages_float.append(float(item[:-1]) * 10 ** 9)
  return damages_float

damages = damage_convert(damages)


# 2 
# Create a Table

# Create and view the hurricanes dictionary
def make_dictionary(names, months, years, max_sustained_winds, areas_affected, damages,deaths):
  new_dict = {names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damages': damages[i], 'Deaths': deaths[i]} for i in range(0, len(names))}
  return new_dict

name_dict = make_dictionary(names, months, years, max_sustained_winds, areas_affected, damages,deaths)
print('this is a dictionary sorted by name:')
print(name_dict)
# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

# def make_year_dict(dictionary):
#   hurricane_dictionary = {}
#   information = dictionary.values()
#   for hurricane in dictionary:
#     for current_cane in information:
#       current_year = current_cane.get('Year')
#       if current_year not in hurricane_dictionary:
#         hurricane_dictionary[current_year] = current_cane
#       else:
#         hurricane_dictionary[current_year] += current_cane
#   return hurricane_dictionary

# your previous code

def make_year_dict(dictionary):
    hurricane_dictionary = {}
    for current_cane in dictionary.values():
        current_year = current_cane['Year']
        if current_year not in hurricane_dictionary:
            hurricane_dictionary[current_year] = [current_cane]
        else:
            hurricane_dictionary[current_year].append(current_cane)
    return hurricane_dictionary

year_dict = make_year_dict(name_dict)
print('\nthis is the new dictionary sorted by year: ')
print(year_dict)

    

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def make_area_dict(dictionary):
  area_dictionary = {}
  for current_cane in dictionary.values():
    for area in current_cane['Areas Affected']:
      if area not in area_dictionary:
        count = 1
        area_dictionary[area] = count
      else:
        area_dictionary[area] += 1
  return area_dictionary

area_dict = make_area_dict(name_dict)
print('\nthis is the new dictionary sorted by area: ')
print(area_dict)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_freq_affected_area(dictionary):
  max_area = 'Central America'
  max_area_count = 0
  for area in dictionary:
    if dictionary[area] > max_area_count:
      max_area = area 
      max_area_count = dictionary[area]
    else:
      max_area = max_area
      max_area_count = max_area_count
  # return max_area, max_area_count
  print('\nthe most affected area is ' + str(max_area) + ', with the frequency being ' + str(max_area_count))

most_freq_affected_area(area_dict)





# 6
# Calculating the Deadliest Hurricane
def deadliest_cane(dictionary):
  deadly_cane = 'Cuba I'
  deadly_deaths = 0
  for cane in dictionary.values():
    if cane['Deaths'] > deadly_deaths:
      deadly_cane = cane['Name']
      deadly_deaths = cane['Deaths']
    else:
      deadly_cane = deadly_cane
      deadly_deaths = deadly_deaths
  # return deadly_cane, deadly_deaths
  print('\nthe deadliest hurricane is {deadly_cane}, with number of deaths being {deadly_deaths}'.format(deadly_cane=deadly_cane, deadly_deaths=deadly_deaths))

deadliest_cane(name_dict)

# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key
def mort_scale(dictionary):
  mort_dict = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': ''}
  for cane in dictionary.values():
    if cane['Deaths'] == 0:
      mort_dict['0'] += (cane['Name'] + ', ')
    elif cane['Deaths'] < 100:
      mort_dict['1'] += (cane['Name'] + ', ')
    elif cane['Deaths'] < 500:
      mort_dict['2'] += (cane['Name'] + ', ')
    elif cane['Deaths'] < 1000:
      mort_dict['3'] += (cane['Name'] + ', ')
    elif cane['Deaths'] < 10000:
      mort_dict['4'] += (cane['Name'] + ', ')
    else:
      mort_dict['5'] += (cane['Name'] + ', ')
  return mort_dict

mortality_dict = mort_scale(name_dict)
print('\nthis is the new dictionary sorted by mortality rating: ')
print(mortality_dict)
# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def highest_damage(dictionary):
  highest_damage_cane = 'Cuba I'
  highest_damage_amount = 0
  for cane in dictionary.values():
    if cane['Damages'] == 'Damages not recorded':
      pass
    elif cane['Damages'] > highest_damage_amount:
      highest_damage_cane = cane['Name']
      highest_damage_amount = cane['Damages']
    else:
      highest_damage_cane = highest_damage_cane 
      highest_damage_amount = highest_damage_amount 
  return highest_damage_cane, highest_damage_amount 

the_highest_damage = highest_damage(name_dict)
print("\nthis is the hurricane that caused the most damage")
print(the_highest_damage)
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
def damage_scale(dictionary):
  damage_dict = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': ''}
  for cane in dictionary.values():
    if cane['Damages'] == 'Damages not recorded':
      damage_dict['0'] += (cane['Name'] + ', ')
    elif cane['Damages'] < 100000000:
      damage_dict['1'] += (cane['Name'] + ', ')
    elif cane['Damages'] < 1000000000:
      damage_dict['2'] += (cane['Name'] + ', ')
    elif cane['Damages'] < 10000000000:
      damage_dict['3'] += (cane['Name'] + ', ')
    elif cane['Damages'] < 50000000000:
      damage_dict['4'] += (cane['Name'] + ', ')
    else:
      damage_dict['5'] += (cane['Name'] + ', ')
  return damage_dict

the_damage_dict = damage_scale(name_dict)
print("\nthis is the new dictionary that sorts hurricanes into their damage ratings")
print(the_damage_dict)
# categorize hurricanes in new dictionary with damage severity as key
