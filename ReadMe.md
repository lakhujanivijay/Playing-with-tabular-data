# Getting my hands dirty with csvtk!!
> [*Vijay Lakhujani*](https://www.vijaylakhujani.me/)*, June 18, 2018*

![](https://github.com/lakhujanivijay/Playing_with_tabular_data/blob/master/tenor.gif)


### What the heck is csvtk?
csvtk a cross-platform, efficient and practical CSV/TSV toolkit. For more information, click [here](https://bioinf.shenwei.me/csvtk/) 


I will be dealing with some demo data sets which could be accessed [here](https://github.com/lakhujanivijay/Playing_with_tabular_data/tree/master/data_set).


#### 1. Getting headers
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

#### 2. Getting stats of file
-------------------------
```
[ csvtk]$ cat test.txt | csvtk stat 
file   num_cols   num_rows
-             7        100
```
- _csvtk assumes that file has headers_, if not, use `-H`

- `-H`, `--no-header-row` specifies that the input CSV file does not have header row

```
[ csvtk]$ cat test.txt | csvtk stat -H
file   num_cols   num_rows
-             7        101
```

#### 3. Getting summary of selected digital fields
----------------------------------------------

- either mention a column name (mandatory) - obtained from `csvtk headers test.txt` as shown below
- getting headers

```
[ csvtk]$ csvtk headers test.txt
# test.txt
1	GeneID
2	FPKM_Control
3	FPKM_Disease
4	fold_change
5	log2_foldChange
6	Regulation
7	Description
```

- now, either mention a column name 
```
[ csvtk]$ cat test.txt | csvtk stats2 -f FPKM_Control
field               num     sum   min    max   mean   stdev
FPKM_Control   100   97.43     0   8.31   0.97    1.42
```
- or mention a column number

```
[ csvtk]$ cat test.txt | csvtk stats2 -f 2
field               num     sum   min    max   mean   stdev
FPKM_Control   100   97.43     0   8.31   0.97    1.42
```

- can use multiple columns

```
[ csvtk]$ csvtk stats2 test.txt -f 2,3
field               num      sum   min     max   mean   stdev
FPKM_Control   100    97.43     0    8.31   0.97    1.42
FPKM_Disease   100   159.92     0   12.18    1.6    2.17
```

#### 4. Read through an excel file
-----------------------------

```
[ csvtk]$ csvtk xlsx2csv test.xlsx | csvtk head -n 2

GeneID,FPKM_Control,FPKM_Disease,fold_change,log2_foldChange,Regulation,Description
ENSRNA049442018,0,0.365817,N.A,N.A,N.A,2|51544689|51544760|-1|tRNA-Asp|tRNA-Asp for anticodon GUC
ENSRNA049443086,0,0.660504,N.A,N.A,N.A,1|94669664|94669735|-1|tRNA-Gly|tRNA-Gly for anticodon UCC
```
- `head` command to display first 2 lines


#### 5. Retrieve sheet names
-----------------------

- `test.xlsx` has 2 subsheets named `demo1` and `demo2`

```
[ csvtk]$ csvtk xlsx2csv test.xlsx -a
index	sheet
1	demo1
2	demo2
```
- Retrieve data with sheet number (sheet number 1)
```
[ csvtk]$ csvtk xlsx2csv test.xlsx -i 2
```

> _Not all data shown_

```
ENSRNA049453302,0,0.657116,N.A,N.A,N.A,12|34735376|34735483|1|snoZ103|Small nucleolar RNA Z103
ENSRNA049453317,2.972869,5.359037,1.80264821625,0.850117884742,Upregulated,12|34734956|34735052|1|snoR1|Small nucleolar RNA snoR1
 ...
 ...

```
- or with sheet name (sheet name `demo2`)

```
[ csvtk]$ csvtk xlsx2csv test.xlsx -n demo2

ENSRNA049453302,0,0.657116,N.A,N.A,N.A,12|34735376|34735483|1|snoZ103|Small nucleolar RNA Z103
ENSRNA049453317,2.972869,5.359037,1.80264821625,0.850117884742,Upregulated,12|34734956|34735052|1|snoR1|Small nucleolar RNA snoR1
 ...
 ...
```

#### 6. Retreive a subset of rows from a subsheet and output by adding a delemiter
-----------------------------------------------------------------------------

- take first 2 rows (`head -n 2`) of subsheet demo2 (`-n demo2`) from excel file `test.xlsx` and output the data with delimiter `"|"` (`-D "|"`)

```
[ csvtk]$ csvtk xlsx2csv test.xlsx -n demo2 | csvtk head -n 2 -D "|"

GeneID|FPKM_Control|FPKM_Disease|fold_change|log2_foldChange|Regulation|Description
ENSRNA049442018|0|0.365817|N.A|N.A|N.A|"2|51544689|51544760|-1|tRNA-Asp|tRNA-Asp for anticodon GUC"
ENSRNA049443086|0|0.660504|N.A|N.A|N.A|"1|94669664|94669735|-1|tRNA-Gly|tRNA-Gly for anticodon UCC"
```

#### 7. Subsetting files
-----------------------------------------------------------------------------
- fetching the first 2 columns, a range like parameter `1-3` is supported
- `head` allows getting first few rows, in this case that is `10`
```
[ csvtk]$ csvtk cut -f 1-3 test.txt | csvtk head -n 10
GeneID,FPKM_Control,FPKM_Disease
ENSRNA049442018,0.0,0.365817
ENSRNA049443086,0.0,0.660504
ENSRNA049444084,0.539982,0.0
ENSRNA049444226,0.188993,0.266948
ENSRNA049444463,0.286740,0.0
ENSRNA049445412,0.0,0.034605
ENSRNA049446362,0.034341,0.000000
ENSRNA049448638,0.0,0.731635
ENSRNA049453010,0.427827,0.000000
ENSRNA049453044,0.582730,1.169653
```
