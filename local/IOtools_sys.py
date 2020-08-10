def get_filenames_smap(basedirin,years_of_interest,ext,sw_years,sw_isunix):

    import numpy as np
    import datetime as dt
    import os.path

    # Check to see if unix or PC.
    if sw_isunix:
        sep = "/" # the slash is a forward slash on the unix operating system
    else:
        sep = "\" # the slash is a backwards slash on the windows system

    # Define the base input directory.
    # main directory, remember the slash on the end of the pathname
    #example: basedirin = "/Users/ceb1c13/Dropbox/Data/2019-08-01-SMAP/"

    # Define the prefix, suffix, resolution and extension.
    # The total filename will be ... fname = prefx + yyyy_ddd + suffx + ext
    # like ... RSS_smap_SSS_L3_8day_running_2019_365_FNL_v04.0.nc
    prefx = "RSS_smap_SSS_L3_8day_running_"
    suffx = "_FNL_v04.0"
    #ext = ".nc"

    nele = len(years_of_interest)
    if nele < 1: # if empty
        years_of_interest = np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])

    nyear_of_interest = len(years_of_interest)

    days_of_interest = np.arange(366) # add an extra day to handle leap years
    nday_of_interest = len(days_of_interest) # this will be 366

    ifile = 0 # initialise this value
    infiles = {}
    infiles_time_yr = {}
    infiles_time_dy = {}
    for icounter in range(nyear_of_interest): # loop over years
        for jcounter in range(366): # loop over days

            yr = years_of_interest[icounter] # year
            dy = days_of_interest[jcounter] # day

            yyyy = str(yr) # string denoting year
            ddd = str(dy) # string denoting day

            # This part is a bit tricky because we need the numbers to look like
            # "001","002" ... "090" rather than "1","2" ... "90"
            # So we check to see what the value is, and add zeros in front.
            if (dy < 10.0):
                ddd = "00"+ddd
            elif (dy >= 10) & (dy < 100):
                ddd = "0"+ddd
            else:
                ddd = ddd

            yyyy_ddd = yyyy + "_" + ddd

            # Sometimes the folders have a subdirectory in the form of a "year".
            if sw_years:
                subdir = yyyy + sep # subdirectory, remember the slash on the end of the pathname
                pname = basedirin + subdir
            else:
                subdir = "" # subdirectory, remember the slash on the end of the pathname
                pname = basedirin

            # Sometimes no subdirectory.
            fname = prefx + yyyy_ddd + suffx + ext

            infile = pname+fname
            #print(infile)
            #tmp = os.listdir(pname)
            #print(tmp)

            tmp = os.path.exists(infile)
            if tmp:

                # Print this to the screen for the user.
                # Store input filename in another variable.
                print(infile)
                infiles[ifile] = infile # store in a dictionary, if we want to access we type infiles[ifile]
                infiles_time_yr[ifile] = yr # store in a dictionary
                infiles_time_dy[ifile] = dy # store in a dictionary
                ifile = ifile + 1 # increment this variable

    return infiles, infiles_time_yr, infiles_time_dy
