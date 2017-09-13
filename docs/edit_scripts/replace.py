
import os, sys

def filter_file(infile_name, no, yes):
	outfile_name = infile_name[:-3] + '_temp.md'
	with open(infile_name, 'r') as infile, open(outfile_name, 'w') as outfile:
		data = infile.read()
		data = data.replace(no, yes)
		outfile.write(data)
	os.system('mv ' + outfile_name + ' ' + infile_name)

def replace_in_dr(old, new, dr):

    for root, drs, fles in os.walk(dr):
            for fle in fles:         
                    filter_file(os.path.join(root, fle), old, new)

dr = '/home/nknapp/LaGriT/docs/pages/'

replace_in_dr('{style="font-family: Courier;"[', '', dr)
replace_in_dr(']]{style="font-family: Times;"', '', dr)
replace_in_dr('style="font-family: Courier;"', '', dr)
replace_in_dr('style="font-family: Courier;"', '', dr)
replace_in_dr('style="font-family: Times;', '', dr)
replace_in_dr('style="font-family: Times;', '', dr)
replace_in_dr('{style="font-family: Courier;"', '', dr)
replace_in_dr('{style="font-family: Courier;"', '', dr)

