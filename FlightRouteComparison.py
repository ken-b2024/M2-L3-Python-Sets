our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destinations = our_routes.intersection(competitor_routes)
print(same_destinations)

our_unique_destinations = our_routes.difference(competitor_routes)
print(our_unique_destinations)

exclusive_destinations = our_routes.symmetric_difference(competitor_routes)
print(exclusive_destinations)