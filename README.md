# Image Search Engine
## Root Directory Structure
- data
- queries
- indexes
- results
- index.py
- search.py
- searcher.py
- ImageDescriptor.py

## How To Use?
### 1. Indexing
When you've prepared your dataset, you're ready to make indexing which is index.py's job. Here is how you use index.py:
`python index.py -d .\data\ -i .\indexes\WhatYouName.csv`
Note: You can use --index/--dataset instead of -i/-d.
### 2.Searching
At first step, we got the index file. Now you're ready to make a search. Decide which image would you like to use for query. If everything is OK, lets go!
`python search.py -i .\indexes\WhatYouName.csv -q .\queries\QueryImage.jpg -r .\results\`

Note: You can use --index/--query/--results instead of -i/-d/-r.
<font color="orange">Warning:</font><font color="black"> Results directory cleans itself every time search.py runs.</font>
A search example:
**Query Image:**
![queryimage](https://i.hizliresim.com/hhtyu20.jpg)

**Results:**
<table>
  <tr >
    <td> <img src="https://i.hizliresim.com/hhtyu20.jpg" width = 200></td>
    <td><img src="https://i.hizliresim.com/ke4p72v.png" width="200"></td>
	<td><img src="https://i.hizliresim.com/8fem1eg.png" width="200"></td>
	<td><img src="https://i.hizliresim.com/g9jkfj6.png" width="200"></td>
   </tr> 
   <tr>
    <td> <img src="https://i.hizliresim.com/n8l6fgn.png" width = 200></td>
    <td><img src="https://i.hizliresim.com/toqiyfd.png" width="200"></td>
	<td><img src="https://i.hizliresim.com/ro7baaw.png" width="200"></td>
	<td><img src="https://i.hizliresim.com/or4n7oa.png" width="200"></td>
  </tr>
</table>


