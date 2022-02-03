from gettext import find

# We start by adding a list of destinations and a test traveler dataset to see if everything works as intended
# The traveler data set will always follow the ['name', 'destination', ['interest_1', 'interest_2', ...]] format
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Since we only work with a set list of destinations and don't plan on adding new ones for this project, we can reason with the index and not worry about it being out of the list.
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# This matches the destination of the traveler with the destination in the list
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = destinations.index(traveler_destination)
    return traveler_destination_index

#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

# We use a list comprehension to create a list of attractions for each destination in destinations
attractions = [[] for destination in destinations]
#print(attractions)

# This function will add an attraction to attractions depending on where it is located. Attractions will follow a ['name', ['interest_tag_1', 'interest_tag_2', ...]] format
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

# Adding one attraction and testing it with a print() statement
add_attraction("Los Angeles, USA", ["Venice beach", ["beach"]])
#print(attractions)

# Just a bunch more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# This function will return the name of the attractions that match a certain destination and a certain interest (or one of the interests listed)
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0]) #possible_attraction[0] only appends the name of the attraction, if you want the full list item remove the '[0]'
    return attractions_with_interest

#la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

# This takes the functions written before and simply make them applied to a new traveler. It returns a formatted string with punctuation.
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi {name}, we think you'll like these places around {destination}: ".format(name = traveler[0], destination = traveler_destination)
    for attraction in traveler_attractions:
        interests_string = interests_string + str(attraction)
        if attraction == traveler_attractions[-1]:
            interests_string = interests_string + "."
        else:
            interests_string = interests_string + ", "
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument', 'art']])
print(smills_france)



