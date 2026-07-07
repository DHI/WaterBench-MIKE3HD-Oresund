# WaterBench Review: WaterBench-MIKE3HD-Oresund

> Comments added by FRTP in these cells... 

**Case family detected:** MIKE3HD (model-based)
**EUM content check:** mikeio available
**Total findings:** 2 MUST, 8 SHOULD, 1 NOTE

## MUST (2)
- Committed archive: .publish/MIKE3HD-Oresund-output.zip � *.zip is a gitignored build output; .publish/ holds the zipping scripts, not the archives (�9)
- Committed archive: .publish/MIKE3HD-Oresund.zip � *.zip is a gitignored build output; .publish/ holds the zipping scripts, not the archives (�9)
> .zip files only exist in my local folder. They are not commited!

## SHOULD (8)
- stations.csv has no 'vertical_datum' column (required for water-level stations) (�8.3)
> I have filtered this information out, as I am making sure that the data has same reference as MIKE output...

- observations/Altimetry_wl_3a.dfs0: item 'quality_water_level' has Undefined EUM type (observation variables should carry a real EUM item type) (�8.4)
- observations/Altimetry_wl_3b.dfs0: item 'quality_water_level' has Undefined EUM type (observation variables should carry a real EUM item type) (�8.4)
- observations/Altimetry_wl_c2.dfs0: item 'quality_water_level' has Undefined EUM type (observation variables should carry a real EUM item type) (�8.4)
- observations/Altimetry_wl_j3.dfs0: item 'quality_water_level' has Undefined EUM type (observation variables should carry a real EUM item type) (�8.4)
- observations/Altimetry_wl_sa.dfs0: item 'quality_water_level' has Undefined EUM type (observation variables should carry a real EUM item type) (�8.4)
> It is simply an extra variable that I choose to include for transparancy - maybe a future user wants to use a different quality flag. EUM not relevant.

- README.md missing recommended section: Disclaimer (�5)
> Not true
- README.md missing recommended section: Case Description (�5)
> I renamed the section to me less generic and more specific. 

## NOTE (1)
- Top-level output/ contains files � published cases must ship only output_sample/ (�9)
> only exist in my local folder. They are not commited!

## Summary
2 blocking issue(s) must be fixed before publishing.
