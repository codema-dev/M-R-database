# M-R-database
Monitoring and Reporting database for Dublin Energy


All the file for the database are created seperately for each database type.

### Existing files

1. convert_gprn_to_X.py 
    Builds dataframe for gas based buildings for year 2020. The year can be changed by making the change to the code.
    File can be used for all councils but the adjustment in reading the file has to be made.
    Areas for further improvement: 
        1. Streamline and merge the reading process of all csv files.
        2. Write a mapping funtion to map the site ids to the buildings 

2. convert_mprn_to_X.py 
    Similar structure to the GPRN code. Builds dataframe for electricity based buildings for year 2020. The year can be changed by making the change to the code.
    File can be used for all councils but the adjustment in reading the file has to be made.
    Areas for further improvement: 
        1. Streamline and merge the reading process of all csv files.
        2. Write a mapping funtion to map the site ids to the buildings 

3. cost_table.py 
    The reference python function to calculate the cost of consumption in all areas , Building(gas), Buildings(electricity), heating feuls and vehicle feuls.

    Any changes in the values of cost need to be changed in this file only
    Areas for further improvement: 
        1. There are 2-3 parts in the table which are commented and are giving conflict due to the ranges. On observation these were not being used but have to be accounted for still.

4. heating_fuels.py 
    Builds the dataframe for heating fuels (kerosene and LPG). Needs to take manual input in litres for both.
    Areas for further improvement: 
        1. Automate the input process to eliminate the manual input.

5. vehicle_fuels.py 
    Builds the dataframe for vehicle fuels (gasoil, petrol and diesel). Needs to take manual input in litres for both.
    Areas for further improvement: 
        1. Automate the input process to eliminate the manual input.

6. unmetered_public_lighting.py 
    Function currently gives the total final consumption for all the GNPRNs combined for unmetered public lighting. 
    The code is constumizable to build  the dataframe for just unmetered public lighting.
    The input the manually entered for each GNPRN.
    Areas for further improvement: 
        1. Automate the input process to eliminate the manual input.
    
    Metered lighting is accounted for the the buildings dataframes.

7. SEUdb.py
    Aggregated  dataframe and displays all the individual python files combined.
    Areas of improvement:
        1. Bug and error fixes required.
        2. Incomplete table and performance indicators aspect of the database still needs to be added.

For future work and analytics python code to be written for the dataframes to analyse and visualize the data in the SEU database.