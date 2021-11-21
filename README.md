# OOP_Ex1_Py
Assignment ex1

Main algo :
The main idea of this algorithm is to classify the elevators by range in the most traffic areas in the building,
and then allocate the most accurate elevator in the call range (src <-> des). 
The division is calculating by the fastest elevator to the slowest.

Class Building:
This class reads the json file and gets the min floor , max floor and array of elevator .

Class  Elevator :
This class  represents elevators. Each elevator have different feature and the main of them is horsepower .

Class  E sort :
This class sorts an array of elevators by horsepower .

Class  Call list :
This class reads the csv file and get all the calls for the elevator .

Class  call for elevator :
This class gives the info of the call like src ,dest  , time  .

Class  B traffic :
This class  gets all the calls and elevator , by going on the building floor we add +1 on all the floors over the( src - dest) and +2 for the floor src and dest.
so we can find the traffic area.

Class  T NODE class :
this class has node and each node represents the range of the current elevator and pointing on the next traffic area 

Class  T Range  : 
this class is the data structures of the T node in addition this data structure use to  search and allocate elevator 
to call from the call list use by the main algorithm .



![img.png](img.png)
