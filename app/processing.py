import sys,math,operator, json
from models import TruckData
raw_data = TruckData.query.all()
data = []


def calculate_distance(x, y):

    # Omitting all the foodtrucks who don't have Approved status
    for d in raw_data:
        if(d.Status == "APPROVED"):
            data.append(d)

    distance = {}

    # Default number of results. To be modified in later versions of the script as this parameter will be retrieved from user.
    #  So, will most probably be in if-else fashion. If user enters use that or else use default
    number_of_results = 5


    # While computing distance records whose Location details are not available are ignored.
    for d in data:
        if d.Latitude == None or d.Longitude == None:
            distance[(d.id, d.Latitude,d.Longitude)] = sys.maxint
        else:
            distance[(d.id, d.Latitude,d.Longitude)] = math.sqrt( (x - d.Latitude)*(x - d.Latitude) + (y - d.Longitude)*(y - d.Longitude) )

    # Sorting the disctionary (using it's list of values) in ascending order
    sorted_distance = sorted(distance.items() , key=operator.itemgetter(1))

    # Format of output - key -> value. Examples: ID -> (Latitude , Longitude).
    output = {}
    for i in range(0,len(sorted_distance)):
        output[sorted_distance[i][0][0]] = (sorted_distance[i][0][1],sorted_distance[i][0][1])
        if i >= number_of_results - 1:
            break

    # Convert the output to json and return
    output_json = json.dumps(output)
    return output_json



# No if __name__ = "__main__" yet as this script will scrictly be imported in other scripts and won't be executed standalone.
'''
if __name__ == "__main__":
    print calculate_distance(37.76,-122.4)
'''