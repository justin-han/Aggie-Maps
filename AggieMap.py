from collections import deque


bus_stops = {
            "Trigon" : ["Element", "The Cambridge", "University Square", "Scandia", "Welsh Balcones", "The Woodlands", "Callaway Villas"], # Stop 12 
            "Element" : ["Trigon", "Willow Oaks"],
            "Willow Oaks" : ["Element", "Broadmoor"],
            "Broadmoor" : ["Willow Oaks", "Blinn"],
            "Blinn" : ["Willow Oaks"],
            "MSC" : ["Fish Pond", "Kleberg", "Beutel"], # Stop 15
            "Fish Pond" : ["MSC", "College Main Parking Garage", "Ross and Ireland"],
            "College Main Parking Garage" : ["Fish Pond", "Spruce St."],
            "Spruce St." : ["College Main Parking Garage", "Aggie Station"],
            "Aggie Station" : ["Spruce St.", "Academic Village"],
            "Academic Village" : ["Howdy Street"],
            "Howdy Street" : ["Villa Maria"],
            "Villa Maria" : ["Wellborn"],
            "Wellborn" : ["Reveille Ranch"],
            "Reveille Ranch" : ["Z Islander"],
            "Z Islander" : ["Village on the Creek"],
            "Village on the Creek" : ["Aggie Station"],
            "The Cambridge" : ["Trigon", "The Rail"], # Stop 22
            "The Rail" : ["The Cambridge", "Cripple Creek"],
            "Cripple Creek" : ["The Rail", "Briarwood"],
            "Briarwood" : ["Scarlett O'Hara"],
            "Scarlett O'Hara" : ["Cripple Creek"],
            "University Square" : ["Trigon", "Ashburn"], # Stop 25
            "Ashburn" : ["University Square", "April Bloom"],
            "April Bloom" : ["Authumn Cir", "Ashburn"],
            "Authumn Cir" : ["Laurel Ridge"],
            "Laurel Ridge" : ["April Bloom"],
            "Scandia" : ["Trigon", "Lexington"], # Stop 26
            "Lexington" : ["Scandia", "Lemon Tree"],
            "Lemon Tree" : ["Lexington", "Alpine Circle"],
            "Alpine Circle" : ["Lemon Tree", "Brentwood"],
            "Brentwood" : ["Arbor Square"],
            "Arbor Square" : ["Southwest Parkway"],
            "Southwest Parkway" : ["Eastmark"],
            "Eastmark" : ["Trails"],
            "Trails" : ["Colgate Circle"],
            "Colgate Circle" : ["Redstone"],
            "Redstone" : ["Alpine Circle"],
            "The Woodlands" : ["Trigon", "The Wick", "The Zone"], # Stop 31
            "The Wick" : ["Yellow House"],
            "Yellow House" : ["Medina"],
            "Medina" : ["Renaissance Park"], 
            "Renaissance Park" : ["Madison Pointe"],
            "Madison Pointe" : ["The Woodlands"],
            "Welsh Balcones" : ["Trigon", "Welsh Navarro"], # Stop 34
            "Welsh Navarro" : ["Welsh Balcones", "Welsh Deacon"],
            "Welsh Deacon" : ["Rock Prairie", "Welsh Navarro"],
            "Rock Prairie" : ["Deacon West"],
            "Deacon West" : ["Fraternity Row"],
            "Fraternity Row" : ["Welsh Deacon"], 
            "Kleberg" : ["MSC", "Physical Education", "Reed Arena"], # Stop 35
            "Physical Education" : ["Kleberg", "Park West"], 
            "Park West" : ["Physical Education", "Woodsman", "Callaway Villas", "Olsen Field"],
            "Woodsman" : ["Gridiron", "Park West"],
            "Gridiron" : ["The Retreat"],
            "The Retreat" : ["University Trails"],
            "University Trails" : ["Fox Run"],
            "Fox Run" : ["The London"],
            "The London" : ["Park West"],
            "Callaway Villas" : ["Trigon", "U-Club"], # Stop 36
            "U-Club" : ["Gateway"],
            "Gateway" : ["Woodsman"],
            "The Zone" : ["Woodsman", "Legacy"], # Stop 40
            "Legacy" : ["Woodsman", "Holleman South"],
            "Holleman South" : ["Aspen Heights", "Legacy"],
            "Aspen Heights" : ["The Junction"],
            "The Junction" : ["Holleman South"],
            "Ross and Ireland" : ["Asbury Water Tower", "Ross and Bizzell"], # Stop 1
            "Ross and Bizzell" : ["Ross and Ireland", "Commons", "Wisenbaker"],
            "Commons" : ["Lewis St."],
            "Lewis St." : ["Ross and Bizzell"],
            "Asbury Water Tower" : ["Wehner"],
            "Wehner" : ["Kleberg", "School of Public Health", "MSC"],
            "Reed Arena" : ["Lot 100G"],
            "Lot 100G" : ["Rec Center"],
            "Rec Center" : ["Kleberg"],
            "Beutel" : ["Kleberg", "Wehner"], # Stop 8
            "Olsen Field" : ["Rec Center"],
            "School of Public Health" : ["White Creek"], # Stop 3
            "White Creek" : ["PA 101", "Wehner"],
            "PA 101" : ["NCTM", "White Creek"],
            "NCTM" : ["PA 101"],
            "Wisenbaker" : ["The Gardens 1"], # Stop 1
            "The Gardens 1" : ["Becky Gates Center"],
            "Becky Gates Center" : ["Hensel"],
            "Hensel" : ["Zachry"],
            "Zachry" : ["Ross and Bizzell"]


}

routes = {
        "Trigon" : ["12", "22", "25", "26", "31", "34", "36"],
        "Element" : ["12"],
        "Willow Oaks" : ["12"],
        "Broadmoor" : ["12"],
        "Blinn" : ["12"],
        "MSC" : ["15", "35", "40", "1", "8", "3"],
        "Fish Pond" : ["15", "1", "3"],
        "College Main Parking Garage" : ["15"],
        "Spruce St." : ["15"],
        "Aggie Station" : ["15"],
        "Academic Village" : ["15"],
        "Howdy Street" : ["15"],
        "Villa Maria" : ["15"],
        "Wellborn" : ["15"],
        "Reveille Ranch" : ["15"],
        "Z Islander" : ["15"],
        "Village on the Creek" : ["15"],
        "The Cambridge" : ["22"],
        "The Rail" : ["22"],
        "Cripple Creek" : ["22"],
        "Briarwood" : ["22"],
        "Scarlett O'Hara" : ["22"],
        "University Square" : ["25"],
        "Ashburn" : ["25"],
        "April Bloom" : ["25"],
        "Authumn Cir" : ["25"],
        "Laurel Ridge" : ["25"],
        "Scandia" : ["26"],
        "Lexington" : ["26"],
        "Lemon Tree" : ["26"],
        "Alpine Circle" : ["26"],
        "Brentwood" : ["26"],
        "Arbor Square" : ["26"],
        "Southwest Parkway" : ["26"],
        "Eastmark" : ["26"],
        "Trails" : ["26"],
        "Colgate Circle" : ["26"],
        "Redstone" : ["26"],
        "The Woodlands" : ["31"],
        "The Wick" : ["31"],
        "Yellow House" : ["31"],
        "Medina" : ["31"],
        "Renaissance Park" : ["31"],
        "Madison Pointe" : ["31"],
        "Welsh Balcones" : ["34"],
        "Welsh Navarro" : ["34"],
        "Welsh Deacon" : ["34"],
        "Rock Prairie" : ["34"],
        "Deacon West" : ["34"],
        "Fraternity Row" : ["34"],
        "Kleberg" : ["35", "40", "1", "8"],
        "Physical Education" : ["35", "40", "8"],
        "Park West" : ["35", "36", "40"],
        "Woodsman" : ["35", "36", "40"],
        "Gridiron" : ["35"],
        "The Retreat" : ["35"],
        "University Trails" : ["35"],
        "Fox Run" : ["35"],
        "The London" : ["35"],
        "Callaway Villas" : ["36"],
        "U-Club" : ["36"],
        "Gateway" : ["36"],
        "The Zone" : ["40"],
        "Legacy" : ["40"],
        "Holleman South" : ["40"],
        "Aspen Heights" : ["40"],
        "The Junction" : ["40"],
        "Ross and Ireland" : ["1", "3", "4"],
        "Ross and Bizzell" : ["1", "3", "4"],
        "Commons" : ["1"],
        "Lewis St" : ["1"],
        "Asbury Water Tower" : ["1", "4"],
        "Wehner" : ["1", "3"],
        "Reed Arena" : ["1"],
        "Lot 100G" : ["1"],
        "Rec Center" : ["1", "8"],
        "Beutel" : ["8", "3"],
        "Olsen Field" : ["8"],
        "NCTM" : ["3"],
        "PA 101" : ["3"],
        "White Creek" : ["3"],
        "School of Public Health" : ["3"],
        "Wisenbaker" : ["4"],
        "The Gardens 1" : ["4"],
        "Becky Gates Center" : ["4"],
        "Hensel" : ["4"],
        "Zachry" : ["4"]

}

def bfs(source, end):
    visited = {}
    parent = {}
    bfs_traversal = []
    q = deque()

    for node in bus_stops.keys():
        visited[node] = False
        parent[node] = None

    s = source
    visited[s] = True
    q.append(s)

    while q:
        u = q.popleft()
        bfs_traversal.append(u)

        for stop in bus_stops[u]:
            if not visited[stop]:
                visited[stop] = True
                parent[stop] = u
                q.append(stop)

    path = []
    e = end
    while e is not None:
        path.append(e)
        e = parent[e]

    path.reverse()
    return path

start = input("Enter a starting stop: ")
print()
end = input("Enter a destination stop: ")
path = bfs(start, end)
print("To get from " + start + " to " + end + " take: ")
for stop in path:
    print(stop, routes[stop])






