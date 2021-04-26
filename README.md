# Manual Tools

Manual tools useful in bulk-Formatting Links to the specifications for Prole REI. These are written in python and require dependancies.

## Link Extractor
Create a file with all the text you want to extract links from.  
Under read_file, insert the filepath to the input file. 
Under write_file, insert the filepath to the output file.

```
read_file = "PATH\TO\INPUT\FILE"
write_file = "PATH\TO\OUTPUT\FILE"
```

## MD Formatter
The MD Formatter takes a list of url's and formates it as follows:

```[TEXT](TEXT.URL)```

**This Requires the [Newspaper3K](https://github.com/codelucas/newspaper) Library.**

List of url's should be in a file names and the path specified in the script such as:

```
read_file = "\PATH\TO\input.txt"  
write_file = "\PATH\TO\output.txt"  
```
