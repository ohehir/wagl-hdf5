import h5py



"""
This is a sample script which reads in a hdf5 dataset
then creates a new dataset with the same dimensions
extracts the dataset as a numpy array, converts it from boolean to uint8
changes the nodata value from 0 to 255 and outputs to new h5
"""

hdf_path = '/path/to/data/LT05_L1TP_099080_19980220_20161228_01_T1.tar.ARD/LT50990801998051ASA00'

hdf_fname = 'LT50990801998051ASA00.wagl.h5'


hdf5 = '%s/%s' % (hdf_path, hdf_fname)

# Read input wagl h5



f = h5py.File(hdf5)


# Read shadow mask layer (sample boolean layer)
ds = f['/LT50990801998051ASA00/RES-GROUP-0/SHADOW-MASKS/SELF-SHADOW']

hdf5 = '%s/%s' % (hdf_path, 'test1.wagl.h5')

# Create output h5
g = h5py.File(hdf5)


# Create output dataset
dset = g.create_dataset('/LT50990801998051ASA00/RES-GROUP-0/SHADOW-MASKS/SELF-SHADOW', ds.shape, dtype=np.uint8)

# get numpy array from input dataset
np_ds = ds.value

# convert boolean array to unit8
np_ds_int = np.uint8(np_ds[:])

# set nodata values from 0 to 255
np_ds_int[np_ds_int == 0] = 255

# write numpy array back to output h5
dset[:] = np_ds_int


