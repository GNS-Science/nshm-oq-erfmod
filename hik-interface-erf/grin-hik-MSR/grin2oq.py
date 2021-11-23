
""" Module :mod:`openquake.converters.ucerf.converter` 
    Modified from Marco's orginal code -- converter.py
    
    Command line syntax:
    python grin2oq.py <source>.config
    example:
    python grin2oq.py grin-hik-MSR01.config
    
"""

import os
import sys
import toml
from pathlib import Path

from openquake.baselib import sap
from openquake.hazardlib.sourcewriter import write_source_model
from openquake.converters.ucerf.parsers.sections_geojson import (
    get_multi_fault_source)

CONFIG_EXAMPLE = """
# Example of .toml configuration file. Copy and paste into a text file the
# lines below.
# The .toml synthax is described here: https://github.com/toml-lang/toml

# Options for the `type` parameter: 'geojson' or 'bin'
type = 'geojson'
source_id = 'hik'
source_name = 'Hikurangi'
# Unit of measure for the rupture sampling: km
rupture_sampling_distance = 5
# The `tectonic_region_type` label must be consistent with what you use in the
# logic tree for the ground-motion characterisation
tectonic_region_type = 'Subduction Interface'
# Unit of measure for the `investigation_time`: years
investigation_time = 1.0
data_folder = 'data/nzl03/' 
output_folder = 'output/nzl03/'
"""


def prnt():
    print(CONFIG_EXAMPLE)


def main(config_fname, *, print_config: bool = False):
    """
    Code for converting a UCERF3 model (represented either using the original
    binary format or the model recent .geojson format) into an OQ Engine model.
    """
    if print_config:
        prnt()
        sys.exit()

    config = toml.load(config_fname)
    dip_sd = config['rupture_sampling_distance']
    strike_sd = dip_sd
    source_id = config['source_id']
    source_name = config['source_name']
    tectonic_region_type = config['tectonic_region_type']
    investigation_time = config['investigation_time']
    data_folder = config['data_folder']
    output_folder = config['output_folder']
    
    if config['type'] == 'geojson':
        computed = get_multi_fault_source(data_folder, dip_sd, strike_sd, source_id,
                                          source_name, tectonic_region_type,
                                          investigation_time)
    elif config['type'] == 'bin':
        computed = get_multi_fault_source(data_folder, dip_sd, strike_sd, source_id,
                                          source_name, tectonic_region_type,
                                          investigation_time)
    else:
        msg = 'Unknown option for the type of input. Check the config file'
        raise ValueError(msg)

    Path(output_folder).mkdir(parents=True, exist_ok=True)
   
    fname = source_id+'.xml'
    out_file = os.path.join(output_folder, fname)

    write_source_model(out_file, [computed], name=source_name,
                       investigation_time=investigation_time)
    print('Created output in: {:s}'.format(output_folder))


main.config_fname = "Name of the .toml file with the configuration params"
main.folder = "Path to the folder containing the UCERF3 model"
main.out_folder = "Path to the folder where to write the output model"
main.print_config = "Path to the folder containing the UCERF3 model"

if __name__ == "__main__":
    sap.run(main)
