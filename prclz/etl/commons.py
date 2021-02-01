from pathlib import Path
from typing import Dict

PRCLZ_ROOT = Path(__file__).parent.parent.absolute()

def build_data_dir(root: str) -> Dict[str, Path]:
    '''
    Builds data directory structure
    '''
    root = Path(root)
    geofabrik    = root / 'input'
    geojson      = root / 'geojson'
    blocks       = root / 'blocks'
    bldgs        = root / 'buildings'
    parcels      = root / 'parcels'
    lines        = root / 'lines'
    complexity   = root / 'complexity'
    gadm         = root / 'GADM'
    gadm_geojson = root / 'geojson_gadm'

    data_paths = {
      'root'        : root,
      'geofabrik'   : geofabrik,
      'geojson'     : geojson,
      'blocks'      : blocks,
      'bldgs'       : bldgs,
      'parcels'     : parcels,
      'lines'       : lines,
      'complexity'  : complexity,
      'gadm'        : gadm,
      'gadm_geojson': gadm_geojson
    }
    for v in data_paths.values():
        v.mkdir(parents=True, exist_ok=True)

    return data_paths