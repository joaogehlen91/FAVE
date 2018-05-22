A Large-Scale Real-World Dataset for Structured Web Date Extraction

1.Motivation
This dataset is a real-world web page collection used for research on the automatic extraction of structured data (e.g., attribute-value pairs of entities) from the Web. We hope it could serve as a useful benchmark for evaluating and comparing different methods for structured web data extraction.


2.Contents of the Dataset
Currently the dataset involves:
a)	8 verticals with diverse semantics;
b)	80 web sites (10 per vertical);
c)	124,291 web pages (200~2,000 per web site), each containing a single data record with detailed information of an entity;
d)	32 attributes (3~5 per vertical) associated with carefully labeled ground-truth of corresponding values in each web page. The goal of structured data extraction is to automatically identify the values of these attributes from web pages.

The involved verticals are summarized as follows:
Vertical #Sites #Pages #Attributes Attributes
Auto        10	17,923	4	model, price, engine, fuel_economy
Book        10	20,000	5	title, author, isbn_13, publisher, publication_date
Camera      10	5,258	3	model, price, manufacturer
Job         10	20,000	4	title, company, location, date_posted
Movie       10	20,000	4	title, director, genre, mpaa_rating
NBA Player  10	4,405	4	name, team, height, weight
Restaurant  10	20,000	4	name, address, phone, cuisine
University  10	16,705	4	name, phone, website, type


3.Format of Web Pages
Each web page in the dataset is stored as one .htm file (in UTF-8 encoding) where the first tag encodes the source URL of the page.


4.Format of Ground-truth Files
For each web site, the page-level ground-truth of attribute values has been labeled using handcrafted regular expressions and stored in .txt files (in UTF-8 encoding) named as "<vertical>-<site>-<attribute>.txt".
In each such file:
a)	The first line stores the names of vertical, site, and attribute, separated by TAB characters ('\t').
b)	The second line stores some statistics (separated by TABs) w.r.t. the corresponding site and attribute, including:
	[1] the total number of pages,
	[2] the number of pages containing attribute values,
	[3] the total number of attribute values contained in the pages,
	[4] the number of unique attribute values.
c)	Each remaining line stores the ground-truth information (separated by TABs) of one page, in sequence of:
	[1] page ID,
	[2] the number of attribute values in the page,
	[3] attribute values ("<NULL>" in case of non-existence).

	
5.Notes on Ground-truth Labeling
a)	The ground-truth labeling was conducted in the DOM-node level. More specifically, the candidate attribute values in a web page are the non-empty strings contained in text nodes in the corresponding DOM tree.
b)	One page (although containing a single data record) may contain multiple distinct values that correspond to an attribute (e.g., multiple authors of a book, multiple granularity levels of addresses).
c)	Currently, when a text node presents a mixture of multiple attributes, its string value is labeled with each of these attributes, if no substitute is available.
d)	Before being stored in .txt files, the raw attribute values were refined by removing redundant separators (e.g., ' ', '\t', '\n').

	
6.Support
If you have questions about this dataset, please contact Qiang Hao (haoq@live.com).

