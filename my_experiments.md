# Getting my hands dirty with [csvtk](https://bioinf.shenwei.me/csvtk/) 

> Vijay Lakhujani, June 14, 2018

![alt text](https://github.com/lakhujanivijay/Playing_with_tabular_data/blob/master/pig3.jpeg "Like a pig!")

I will be dealing with a csv file which could be accessed [here](https://raw.githubusercontent.com/lakhujanivijay/Playing_with_tabular_data/master/test.txt).


##### 1. Getting headers
-------------------------
```
[ csvtk]$ csvtk headers test.txt 
test.txt
1	GeneID
2	FPKM_Control
3	FPKM_Disease
4	fold_change
5	log2_foldChange
6	Regulation
7	Description
```

##### 2. Getting stats of file
-------------------------
```
[ csvtk]$ cat test.txt | csvtk stat 
file   num_cols   num_rows
-             7        100
```
> _csvtk assumes that file has headers_, if not, use `-H`

> `-H`, `--no-header-row` specifies that the input CSV file does not have header row

```
[ csvtk]$ cat test.txt | csvtk stat -H
file   num_cols   num_rows
-             7        101
```

##### 3. Getting summary of selected digital fields
----------------------------------------------

> either mention a column name (mandatory) - obtained from `csvtk headers test.txt`

```
[ csvtk]$ cat test.txt | csvtk stats2 -f FPKM_Control
field               num     sum   min    max   mean   stdev
FPKM_Control   100   97.43     0   8.31   0.97    1.42
```
> or mention a column number

```
[ csvtk]$ cat test.txt | csvtk stats2 -f 2
field               num     sum   min    max   mean   stdev
FPKM_Control   100   97.43     0   8.31   0.97    1.42
```

> can use multiple columns

```
[ csvtk]$ csvtk stats2 test.txt -f 2,3
field               num      sum   min     max   mean   stdev
FPKM_Control   100    97.43     0    8.31   0.97    1.42
FPKM_Disease   100   159.92     0   12.18    1.6    2.17
```

##### 4. Read through an excel file
-----------------------------

```
[ csvtk]$ csvtk xlsx2csv test.xlsx | csvtk head -n 2

GeneID,FPKM_Control,FPKM_Disease,fold_change,log2_foldChange,Regulation,Description
ENSRNA049442018,0,0.365817,N.A,N.A,N.A,2|51544689|51544760|-1|tRNA-Asp|tRNA-Asp for anticodon GUC
ENSRNA049443086,0,0.660504,N.A,N.A,N.A,1|94669664|94669735|-1|tRNA-Gly|tRNA-Gly for anticodon UCC
```
> `head` command to display first 2 lines


##### 5. Retrieve sheet names
-----------------------

> `test.xlsx` has 2 subsheets named `demo1` and `demo2`

```
[ csvtk]$ csvtk xlsx2csv test.xlsx -a
index	sheet
1	demo1
2	demo2
```
> Retrieve data with sheet number (sheet number 1)
```
[ csvtk]$ csvtk xlsx2csv test.xlsx -i 2

ENSRNA049453302,0,0.657116,N.A,N.A,N.A,12|34735376|34735483|1|snoZ103|Small nucleolar RNA Z103
ENSRNA049453317,2.972869,5.359037,1.80264821625,0.850117884742,Upregulated,12|34734956|34735052|1|snoR1|Small nucleolar RNA snoR1
 ...
 ...

```
> or with sheet name (sheet name `demo2`)

```
[ csvtk]$ csvtk xlsx2csv test.xlsx -n demo2

ENSRNA049453302,0,0.657116,N.A,N.A,N.A,12|34735376|34735483|1|snoZ103|Small nucleolar RNA Z103
ENSRNA049453317,2.972869,5.359037,1.80264821625,0.850117884742,Upregulated,12|34734956|34735052|1|snoR1|Small nucleolar RNA snoR1
 ...
 ...
```

##### 6. Retreive a subset of rows from a subsheet and output by adding a delemiter
-----------------------------------------------------------------------------

> take first 2 rows (`head -n 2`) of subsheet demo2 (`-n demo2`) from excel file `test.xlsx` and output the data with delimiter `"|"` (`-D "|"`)

```
[ csvtk]$ csvtk xlsx2csv test.xlsx -n demo2 | csvtk head -n 2 -D "|"

GeneID|FPKM_Control|FPKM_Disease|fold_change|log2_foldChange|Regulation|Description
ENSRNA049442018|0|0.365817|N.A|N.A|N.A|"2|51544689|51544760|-1|tRNA-Asp|tRNA-Asp for anticodon GUC"
ENSRNA049443086|0|0.660504|N.A|N.A|N.A|"1|94669664|94669735|-1|tRNA-Gly|tRNA-Gly for anticodon UCC"
```



