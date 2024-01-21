* Anchi (Bryant) Xia
* 07/04/2023

* This file combines .dat and .dct files to make .dta data sets for subsequent analysis
* Because differences in naming conventions, # of waves per panel, etc., I decided against
* writing one big file that performs this operation for all panels, opting instead to repeat
* this exercise for different panels, renaming and editing along the way.

clear all
set maxvar 30000

local year_full = "REPLACE WITH YR." // eg. 1996
local year_ab = "REPLACE WITH YR. ABBREVIATION" // eg. 96

local tms // specify a list of topical modules; note that this main contain gaps (for 1996: 2 3 4 5 6 7 8)

local ws // specifiy a list of the number of waves; 1 2 3 4 5 6 7 8 9 10 11 12

foreach i of local ws{
 	local dat_name "~\data\raw_before_redesign\raw_`year_full'\sipp`year_ab'l`i'.dat"
 	local dct_name "~\data\raw_before_redesign\raw_`year_full'\96w`i'.dct"
 	quietly infile using "`dct_name'", using("`dat_name'") clear
	save "~\data\raw_before_redesign\raw_`year_full'\l`year_ab'puw`i'.dta", replace
}

foreach i of local tms{
  	local dat_name "~\data\raw_before_redesign\raw_`year_full'\sipp`year_ab't`i'.dat"
  	local dct_name "~\data\raw_before_redesign\raw_`year_full'\90tm`i'.dct"
  	quietly infile using "`dct_name'", using("`dat_name'") clear
 	save "~\data\raw_before_redesign\raw_`year_full'\p`year_ab'putm`i'.dta", replace
}

