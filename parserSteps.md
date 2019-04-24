# Parser excel file

- [x] `C` column --> sample names
  - 11 digits filter
  - `G` column --> `Cantidad` --> skip `0` value

- [x] Delete `empty` columns and leave `0` columns
- [x] Normalization time
- [x] Save file with all sub-matrixsd
- [x] Interpolation and get X / Y vectors interpolated
- [x] Normalization vector by its number of samples
---
---
- [x] If a columns is empty, I skipped
- [x] Variables should be same length among products
- [x] Matrix belongs to one specific time: time 0 --> Matrix of products and variables
- [x] Get index of vectors than can be interpolated and then loop through it
- [x] Vector X time --> Number if samples, incremental index by 1 --> then normalize
---
---
- [ ] excelParser.py: - Delete skipColumns array
                      - Insert by `argv` the name of the sheet