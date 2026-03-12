from pyspark.sql import SparkSession
from pyspark import SparkContext

# Initialize Spark session and context
spark = SparkSession.builder.appName("ProximityCheckTwoCSV").getOrCreate()
sc = spark.sparkContext

# Paths to the CSV files and output file
people_csv_path = "Task1/output/people.csv"
activated_csv_path = "Task1/output/activated_small.csv"
output_path = "Task1/query_output/query1"  # Replace with your desired output path

# Read the people CSV file as an RDD
people_raw_rdd = sc.textFile(people_csv_path)
people_header = people_raw_rdd.first()  # Extract the header
people_rdd = people_raw_rdd.filter(lambda line: line != people_header).map(lambda line: line.split(","))

# Read the activated CSV file as an RDD
activated_raw_rdd = sc.textFile(activated_csv_path)
activated_header = activated_raw_rdd.first()  # Extract the header
activated_rdd = activated_raw_rdd.filter(lambda line: line != activated_header).map(lambda line: line.split(","))

# Structure: (id, x, y, full_record)
people_rdd = people_rdd.map(lambda row: (int(row[0]), int(row[1]), int(row[2]), tuple(row)))
activated_rdd = activated_rdd.map(lambda row: (int(row[0]), int(row[1]), int(row[2]), tuple(row)))

# Broadcast the activated people list
activated_list = activated_rdd.collect()
activated_broadcast = sc.broadcast(activated_list)

# Function to check if two people are within 6 units (Manhattan distance)
def within_distance(person1, person2):
    x1, y1 = person1[1], person1[2]  # Coordinates from person1
    x2, y2 = person2[1], person2[2]  # Coordinates from person2
    return abs(x1 - x2) + abs(y1 - y2) <= 6

# Find all people within range of the activated people
def find_nearby_people(person):
    nearby_checks = []
    for activating_person in activated_broadcast.value:
        if within_distance(person, activating_person):
            nearby_checks.append([person[0], activating_person[0]])  # Add the full record
    return nearby_checks

# Apply the function to find all people within range
new_people_to_check_rdd = people_rdd.flatMap(find_nearby_people)

# Collect and print the final list of people to be checked
final_list = new_people_to_check_rdd.collect()
for person in final_list:
    print("" + str(person[0]) + ", " + str(person[1]))  # Print full record

# Stop Spark context
sc.stop()