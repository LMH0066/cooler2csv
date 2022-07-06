# cooler2csv
No tool was found to convert cool files to CSV files, so I wrote this little tool

## Environmental dependency
```
pip install cooler
```

## output CSV default format
|  chrom1   | start1  |  end1   | chrom2  |  start2   | end2  |
|  ----  | ----  |  ----  | ----  |  ----  | ----  |
| chr1  | 1230000 | 1240000  | chr1 | 1230000  | 1240000 |

If you need to do something specific with the CSV results, you can write a small function (similar to utils/import_func_case.py) and then call the handler function with the -f argument：
```
python cool2csv.py -i <input_path> -o <output_path> -m <is_multi> -f ./utils/import_func_case.py
```