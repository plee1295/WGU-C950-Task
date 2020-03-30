# WGU-C950-Task
Task for Western Governors University C950 - Data Structures and Algorithms II


Scenario:
The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution 
for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their 
promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to 
deliver each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in 
the attached “WGUPS Package File,” will be delivered on time with the least number of miles added to the combined 
mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” 
and distances to each location are given in the attached “WGUPS Distance Table.”

While you work on this assessment, take into consideration the specific delivery time expected for each package and the
possibility that the delivery requirements—including the expected delivery time—can be changed by management at any 
time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be able 
to see, at assigned points, the progress of each truck and its packages by any of the variables listed in 
the “WGUPS Package File,” including what has been delivered and what time the delivery occurred.

The intent is to use this solution (program) for this specific location and to use the same program in many cities in each 
state where WGU has a presence. As such, you will need to include detailed comments, following the industry-standard Python 
style guide, to make your code easy to read and to justify the decisions you made while writing your program.


Assumptions:
1. Each truck can carry a maximum of 16 packages.
2. Trucks travel at an average speed of 18 miles per hour.
3. Trucks have a “infinite amount of gas” with no need to stop.
4. Each driver stays with the same truck as long as that truck is in service.
5. Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
   The day ends when all 40 packages have been delivered.
6. Delivery time is instantaneous, i.e., no time passes while at a delivery 
   (that time is factored into the average speed of the trucks).
7. There is up to one special note for each package.
8. The wrong delivery address for package #9, Third District Juvenile Court, will be corrected 
   at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
9. The package ID is unique; there are no collisions.
10. No further assumptions exist or are allowed.
