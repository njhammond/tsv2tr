# tsv2tr

tsv2tr converts a file in tab separated value (TSV) format to HTML <tr> format. It wraps each element in the TSV file in a <td>element</td> line. Optionally a column can be excluded from having a <td> wrapper added.

It is a standalone Python script.

## Installation

There is one way to get `tsv2tr`:

- Download the script directly: `wget https://raw.githubusercontent.com/njhammond/tsv2tr/master/tsv2tr.py`

## Usage

Simply:

```bash
python tsv2tr.py [-i column_number_to_ignore, [col_2]] file1.tsv [file2.tsv ...]
```

Output is written to a file with extension ".tr".

## Example conversion

Cell 1<tab>Cell 2<tab>Cell 3

converts to

<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>

## Typical usage

If you have an Excel spreadsheet with data that you want to convert to an HTML table.
Copy/paste the data from Excel to a local file.
Run tsv2tr on the local file.
Copy/paste the output into an HTML table.

## Real world examples
I wrote the script to help with creating http://www.bridgescoreplus.com/news/wroclaw_lead_card.html.

This page was written by copy/pasting data from an Excel spreadsheet. To make the tables sortable, I used datatables.

The file examples/1.tsv shows the raw contents of first table on the web page. Simple copy/paste the data to a file, run the script, cut/paste the output to the web page.

In order to be able to use the data sort options of datatables, e.g. <td data-sort="1">, I added an option to tsv2tr to not add the <td> wrapper to a defined column.

Consider a table that contains a list of the playing cards. I want to be able to sort on the order of playing cards so using Excel I create cell elements that contain the cards in order AS, KS, QS, ... 2C. Spades, hearts, diamonds, clubs is the traditional sort order for the card game Bridge. In order to sort, I used Excel CONCATENATE() to add <td data-sort="number"></td> wrappers around each column. When exporting data containing this field, I do not want an extra <td> wrapper around those columns. See http://www.bridgescoreplus.com/news/wroclaw_lead_card.html#dda_tricks for a real world table created using this script.
