import json
import argparse
import configparser
from get_injection_times import get_trigger_time

if __name__ == '__main__' :
    
    print("args...")
    #Get RA/DEC, as well as configfile/framefile/channel_name
    parser = argparse.ArgumentParser()
    parser.add_argument("-ra", action="store", type=float, default=None,
                        help="Override right ascension of the injection")
    parser.add_argument("-dec", action="store", type=float, default=None,
                        help="Override declination of the injection")
    
    parser.add_argument("-c", action="store", type=str, default=None,
                    help="Name of the config file")
    parser.add_argument("-ff", action="store", type=str, default=None,
                    help="Name of the frame file")
    parser.add_argument("-cn", action="store", type=str, default=None,
                    help="Name of the channel")
    
    args = parser.parse_args()
    
    print("config_inj...")
    #Change the config file to have the proper ra-dec pair
    parser = configparser.ConfigParser()
    parser.read('inj_config.ini')
    RA=str(args.ra)
    DEC=str(args.dec)
    parser.set('extrinsic', 'ra', RA)
    parser.set('extrinsic', 'dec', DEC)
    with open('inj_config.ini', 'w') as config_file:
        parser.write(config_file)
    
    print("trigger time...")
    t=get_trigger_time(args.c, args.ff, args.cn)
    
    key=args.cn[:2]+"_"+str(RA)+str(DEC)
    output_dict={ key : t }
    
    print("json dump...")
    with open("indiv_timekey_folder/{}.json".format(key), "w") as f:
            json.dump(output_dict, f, indent=2, sort_keys=True)
    
    

        