This folder contains the data used as input in the MIKE3HD model. The inputs are:

| File | Description | Unit |
| --- | --- | --- | 
| mesh_EMOD.mesh | The computational mesh used in the model | - |
| init/2D_hot_2021.dfsu | Initial conditions for hot-starting simulation. 2D.  | - |
| init/3D_hot_2021.dfsu | Initial conditions for hot-starting simulation. 3D.  | - |
| North_BND_UVTS.dfsu | Boundary value input in North boundary. U- and V-velocity, temperature, salinity, 3D. | m/s, m/s, deg. C, PSU |
| North_BND_WL.dfs1 | Boundary value input in North boundary. 1D Water level. | m |
| South_BND_UVTS.dfsu | Boundary value input in South boundary. U- and V-velocity, temperature, salinity, 3D. | m/s, m/s, deg. C, PSU |
| South_BND_WL.dfs1 | Boundary value input in South boundary. 1D Water level. | m |
| ERA5_UVP.dfs2 | Mean sea level pressure, and 100m u- and v- component of wind. | m/s, m/s, hPa |
| ERA5_T2.dfs2 | Air temperature at 2 meters above sea or land surface. | deg. C |
| ERA5_RH2.dfs2 | Relative humidity at 2 meters above sea or land surface. | % |
| ERA5_CLEARNESS.dfs2 | Cloud coverage  | % |
| ERA5_ICE.dfs2 | Sea-ice cover. Fraction of grid box that is covered by ice.  | % |
| ERA5_PRECIPITATION.dfs2 | Precipitation.  | mm/d |
| hdif_LONLAT_v2.dfs3 | Horizontal computational diffussivity matrix, static. | - |
| vdif_LONLAT_v1B_oresund.dfs3 | Vertical computational diffussivity matrix, static. | - |


Descriptions of the sources can be found in the table in in the parent folder README.md.

