import StationSearcher
import DataReader
import DataConverter
import Reporter
import DataOutputer
import pickle

#Defining input parameters for extracting weather data
#In the later version of the program this will be done in the user interface
year = 2016
lat = 52.93
lon = 8.23

serialization = 1

if __name__ == '__main__':

    if not serialization:
        # Calling the StationSearcher constructor using input parameters
        print('StationSearcher')
        searcher = StationSearcher.StationSearcher(year, lat, lon)
        #Output -  list of 7 stations that are most favourable for given input paramaters, saved in variable station_list
        station_list = searcher.station_list

        #Calling the DataReader constructor using previously created station list
        print('DataReader')
        extractor = DataReader.DataReader(year, station_list)
        #Output - unconverted set of data extracted from zip files in the form of list
        extracted_data = extractor.raw_data_set

        #Calling the DataConverter constructor using previously created raw data
        print('DataConverter')
        convertor = DataConverter.DataConverter(year, extracted_data)

        pickle_out = open("data/serialization/station_list.pickle", "wb")
        pickle.dump(station_list, pickle_out)
        pickle_out.close()

        pickle_out = open("data/serialization/convertor.pickle", "wb")
        pickle.dump(convertor, pickle_out)
        pickle_out.close()
    
    if serialization:
        pickle_in = open("data/serialization/convertor.pickle","rb")
        convertor = pickle.load(pickle_in)
        pickle_in.close()

        pickle_in=open("data/serialization/station_list.pickle","rb")
        station_list = pickle.load(pickle_in)
        pickle_in.close()


    #Output: converted data with calculated additional values needed in energy analisys programs
    converted_data = convertor.converted_data
    #Additionally, periods with missing entries in the original data set as well as number of those enries are saved
    missing_list = convertor.missing_list                       #list with missing periods
    missing_entries_list = convertor.missing_entries_list       #list with number of missing entries

    #Writing the EPW file
    outputer = DataOutputer.DataOutputer(converted_data,station_list)

    #Calling the Reporter class that based on the data generated in steps before, creates report files in the reports/
    #directory
    reporter = Reporter.Reporter(year, lon, lat, station_list, missing_list, missing_entries_list,
                             converted_data)