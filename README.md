# mario_clouds_xls
**Google sheets settings only allow recalculation updates to happen every hour or every minute. So that version is slow as heck.**

*In the /img_processing folder i have included a py script that converts png files to csv files that states what colour each pixel/cell in the cloud graphic is. Conditional formatting in the spread sheet is used to change their colour according to the words in the cell. So cells containing 'white' are formatted as white text and white highlight. Empty cells as cyan for the sky.*

**The single cloud and triple length cloud each have their own sheet in the xls file. from this the main Matio_Clouds_xls sheet pulls in the other two sheets for 'graphics'  info.**

**Marion_Clouds_xls cells (200x200) are each set to 10px x 10px**


On the google spreadsheet version the main sky sells iterate this formula
```
=IF(
    AND( ROW() >= $E$206, ROW() < $E$206 + 24, COLUMN() >= $E$205, COLUMN() < $E$205 + 64 ),
    INDEX(triple!$A$1:$BL$24, ROW() - $E$206 + 1, COLUMN() - $E$205 + 1),
  IF(
    AND( ROW() >= $B$206, ROW() < $B$206 + 24, COLUMN() >= $B$205, COLUMN() < $B$205 + 32 ),
    INDEX(single!$A$1:$AF$24, ROW() - $B$206 + 1, COLUMN() - $B$205 + 1),
    IF(
      AND( ROW() >= $C$206, ROW() < $C$206 + 24, COLUMN() >= $C$205, COLUMN() < $C$205 + 32 ),
      INDEX(single!$A$1:$AF$24, ROW() - $C$206 + 1, COLUMN() - $C$205 + 1),
      ""
    )
  )
)
```

and in 
B205 and B206 a helper animation formulae for the first single cloud:
```
=MOD(200 - INT((NOW()-TODAY())*86400*0.1), 200 - 32 + 1)
```
and
```
=IF( OR(B206 = "", B206 = 0, $B$205 >= 168), RANDBETWEEN(1,47), B206)
```
respectively.


C205 and C206 a helper animation formulae for the second single cloud:
```
=MOD(200 - INT((NOW()-TODAY())*86400*0.12), 200 - 32 + 1)
```
and
```
=IF( OR(C206 = "", C206 = 0, $C$205 >= 168), RANDBETWEEN(71,117), C206)
```
respectively.


E205 and E206 a helper animation formulae for triple cloud:
```
=MOD(200 - INT((NOW()-TODAY())*86400*0.15), 200 - 64 + 1)
```
and
```
=IF( OR(E206 = "", E206 = 0, $E$205 >= 136), RANDBETWEEN(141,154), E206)
```
respectively.

