## Scrapping SIPP Files

The goal of these files is to help you get files efficiently https://www.nber.org/research/data/survey-income-and-program-participation-sipp for panels before the redesign (i.e., up to and including the 2008 panel). Downloading appears to be straightforward if you are an internal NBER user but difficult otherwise. You may also want to check out https://ceprdata.org/sipp-uniform-data-extracts/sipp-extraction-programs/.

**Caution**: 
* I have encountered *ad hoc* issues with this scrapping procedure as written, mostly due to the fact that the undelrying SIPP files are not formatted consistently. **Please pay attention to my comments in the code files** in case you encounter any issues. Worst comes worst, you can always manually download and then unzip a few files that are giving you problems.
* Change file paths everywhere in the code files to where you see fit.

All in all, these files are far from perfect. In the event that you need to work with old SIPP files but is not an NBER user, I hope these codes can still prove to be somewhat useful. Should you have any questions, feel free to reach me at bryantxia2435@gmail.com. 

## The workflow:

1. ```scrape_zip.py``` is intended to download all the zip files found on NBER's SIPP web page. 
2. ```unzip_and_move.py``` is intedned to unzip your downloaded zip files and move to your desired location.
    * Since I placed each panel in a different folder, the code is written to handle one panel at a time, but you can modify this easily.
    * I have experienced weird data corruption issues in this step. Doing it panel by panel helps to identify when this happens. I added something in my code to indicate when this occurs; the only remedy I see is to download the zip file in question by hand. If you find a clever remedy, great.
3. ```scrape_dct.py``` scrapes the corresponding dct files.
4. ```load_old.py``` Stata ado program to combine the dct and dat files.
    * Again, I do this panel by panel, but you can modify the structure easily.

