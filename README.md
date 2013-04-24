<h1>USA_Zipcodes_Py</h1>

<h3>Simple Python Script for Getting USA Zipcode Info</h3>


This module gets its data from <a href="http://www.boutell.com/zipcodes/">http://www.boutell.com/zipcodes/</a>. 

It has info for 43,204 zipcodes and is based off of year 2000 US Census Bureau data.

<h4>Usage</h4>

    from USA_Zipcodes import get_zipcodes
    zipcode_data = get_zipcodes()  
    # zipcode_data is huge:
    #  [{'is_dst_observed': True, 'city': 'Portsmouth', 'state': 'NH', 'zip': '00210', 'latitude': 43.005895000000002, 'timezone': -5, 'longitude': -71.013202000000007}, ...]

It also includes an (unrelated) useful function for converting a CSV file to a Python table (array of arrays):

    from USA_Zipcodes import convert_csv_to_table
    table = convert_csv_to_table(open('my_csv_file.csv'))

If you experience any issues, let me know...

<h4>License</h4>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
