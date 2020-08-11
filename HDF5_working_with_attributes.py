# wagl hdf5 Documentation:

# https://github.com/GeoscienceAustralia/wagl/blob/develop/docs/source/hdf5.rst



import h5py



hdf_path = '/path/to/data/LT05_L1TP_099080_19980220_20161228_01_T1.tar.ARD/LT50990801998051ASA00'

hdf_fname = 'LT50990801998051ASA00.wagl.h5'


hdf5 = '%s/%s' % (hdf_path, hdf_fname)



f = h5py.File(hdf5)


# NBAR group underwhich there are 7 datasets

# NBAR:

nbar_group = f['/LT50990801998051ASA00/RES-GROUP-0/STANDARDISED-PRODUCTS/REFLECTANCE/NBAR']



# Show me the dataset (band) names:

nbar_group.keys()
<KeysViewHDF5 
"""
['BAND-1', 'BAND-2', 'BAND-3', 'BAND-4', 'BAND-5', 'BAND-6', 'BAND-7']>


"""


# iterate through band datasets for nbar group

for key, value in nbar_group.items ():

    print( " %s : %s " % ( key , value ))

 
"""
 BAND-1 : <HDF5 dataset "BAND-1": shape (7891, 7811), type "<i2"> 

 BAND-2 : <HDF5 dataset "BAND-2": shape (7891, 7811), type "<i2"> 

 BAND-3 : <HDF5 dataset "BAND-3": shape (7891, 7811), type "<i2"> 

 BAND-4 : <HDF5 dataset "BAND-4": shape (7891, 7811), type "<i2"> 

 BAND-5 : <HDF5 dataset "BAND-5": shape (7891, 7811), type "<i2"> 

 BAND-6 : <HDF5 dataset "BAND-6": shape (7891, 7811), type "<i2"> 

 BAND-7 : <HDF5 dataset "BAND-7": shape (7891, 7811), type "<i2">
"""




# Sample dataset for band 1

ds = f['/LT50990801998051ASA00/RES-GROUP-0/STANDARDISED-PRODUCTS/REFLECTANCE/NBAR/BAND-1']



# Now I want to print out all attributes and their values:

for key, value in ds.attrs.items ():

    print( " %s : %s " % ( key , value ))

 

"""
CLASS : IMAGE 
 
DISPLAY_ORIGIN : UL 
 
IMAGE_VERSION : 1.2 
 
alias : Coastal-Aerosol 
 
band_id : 1 
 
band_name : BAND-1 
 
crs_wkt : PROJCS["WGS 84 / UTM zone 53N",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",135],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Easting",EAST],AXIS["Northing",NORTH],AUTHORITY["EPSG","32653"]] 
 
description : Contains the brdf corrected reflectance data scaled by 10000. 
 
geotransform : [ 6.248850e+05  3.000000e+01  0.000000e+00 -3.077985e+06  0.000000e+00
 -3.000000e+01] 
 
no_data_value : -999 
 
platform_id : LANDSAT_8 
 
rori_threshold_setting : 0.52 
 
sensor_id : OLI
"""




# OK now just access and single attribute:

ds.attrs.get('alias')

# or
ds.attrs['alias']

# and change it:

ds.attrs['alias'] = 'red'
