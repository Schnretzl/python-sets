# 1. Python Sets Adventure

# Task 1: Flight Route Comparison
def shared_destinations(our_routes, competitor_routes):
    return our_routes.intersection(competitor_routes)

def unique_destinations(our_routes, competitor_routes):
    return our_routes.difference(competitor_routes)

def unshared_destinations(our_routes, competitor_routes):
    return our_routes.symmetric_difference(competitor_routes)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

print("Shared Destinations: ", shared_destinations(our_routes, competitor_routes))
print("Destinations unique to our airline: ", unique_destinations(our_routes, competitor_routes))
print("Unshared Destinations: ", unshared_destinations(our_routes, competitor_routes))