import sys,math,operator, json
import csv


# This function calls and returns the distance between 2 points in miles given their latitude and longitude.
# This function also returns if the distance between given 2 points is less than radius or not
def is_dist_within_radius(x1,y1,x2,y2,radius):


    lat1 = math.radians(float(x1))
    lon1 = math.radians(float(y1))
    y2 = float(y2)
    x2 = float(x2)
    lat2 = math.radians(x2)
    lon2 = math.radians(y2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.pow(math.sin(dlat/2),2) + math.cos(lat2)*math.cos(lat1) * math.pow(math.sin(dlon/2),2)
    c = 2 * math.atan2( math.sqrt(a) , math.sqrt(1-a))
    d = 3961 * c
    if(d < radius):
        return (True , d)
    else:
        return (False , d)

def calculate_distance(location_data , **kwargs):

    # May comment the following 5 line logic for local testing (No need to construct, pass and parse json to retrieve latitude and longitude)

    json_coord = location_data
    x = float(json_coord['lat'])
    y = float(json_coord['long'])

    data_file = "Mobile_Food_Facility_Permit.csv"
    csv_file = csv.DictReader(open(data_file, 'rb'), delimiter=',')
    raw_data = []

    for row in csv_file:
        table_entries = dict()
        for key, value in row.items():
                table_entries[key] = value
        raw_data.append(table_entries)

    data = []

    # Omitting all the foodtrucks who don't have Approved status
    for d in raw_data:
        if(d['Status'] == "APPROVED"):
            data.append(d)

    distance = {}
    # Default number of results. To be modified in later versions of the script as this parameter will be retrieved from user.
    #  So, will most probably be in if-else fashion. If user enters use that or else use default
    if("number_of_results" in kwargs.keys()):
        print "INSIDE FILTER PROCESSING : no of results : " , kwargs['number_of_results']
        number_of_results = kwargs['number_of_results']
    else:
        number_of_results = 5


    # While computing distance records whose Location details are not available are ignored.
    for d in data:
        if d['Latitude'] == None or d['Longitude'] == None or d['Latitude'] == "" or d['Longitude'] == "":
            distance[(d['Applicant'], d['Latitude'],d['Longitude'])] = sys.maxint
        else:

            # Check if keyword arguments contain radius. If yes, use the radius information in calculation.
            # Otherwise, set radius = sys.maxint since in that case their is no restriction on perimeter

            if("radius" in kwargs.keys()):
                #print "INSIDE FILTER PROCESSING"
                radius = kwargs['radius']

                # is_dist_within_radius returns a tuple t. t[0] => True if distance between 2 points is less than radius.
                # t[1] is the actual distance d (miles) between 2 points.

                if(is_dist_within_radius(x,y,float(d['Latitude']),float(d['Longitude']),radius)[0]):
                    #print "INSIDE FILTER PROCESSING - FOUND ONE POSSIBLE RESULT LOCATION"
                    distance[(d['Applicant'], d['Latitude'],d['Longitude'])] = is_dist_within_radius(x,y,d['Latitude'],d['Longitude'],radius)[1]
                else:
                    distance[(d['Applicant'], d['Latitude'],d['Longitude'])] = sys.maxint

            else:
                distance[(d['Applicant'], d['Latitude'],d['Longitude'])] = is_dist_within_radius(x,y,d['Latitude'],d['Longitude'],sys.maxint)[1]

    # Sorting the disctionary (using it's list of values) in ascending order
    sorted_distance = sorted(distance.items() , key=operator.itemgetter(1))
    if("number_of_results" in kwargs.keys()):
        print sorted_distance
        print "Length of sorted idstance : " , len(sorted_distance)
        print "type of Number of Results : " , number_of_results
        print "Radius : " , radius
        # Format of output - key -> value. Examples: ID -> (Latitude , Longitude).
    output = {}
    for i in range(0,number_of_results):
        print "Populating OUTPUT"
        output[sorted_distance[i][0][0]] = (sorted_distance[i][0][1],sorted_distance[i][0][2])


    if("number_of_results" in kwargs.keys()):
        print "OUTSIDE----------------********************"
        print "Lenth of sorted distance"
        print len(sorted_distance)
        print "Printing OUTPUT (not in JSON)"
        print "Lenth of output"
        print len(output)
        print "Actual Output"
        print output

    # Convert the output to json and return
    output_json = json.dumps(output)
    return output_json


#if __name__ == "__main__":
#     print calculate_distance(37.791777988510,-122.39751708644, radius=5, number_of_results=10)
# No if __name__ = "__main__" yet as this script will scrictly be imported in other scripts and won't be executed standalone.


