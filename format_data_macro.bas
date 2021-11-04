Attribute VB_Name = "Module1"
Sub delete()
'
' delete Macro
'

'
    Range("A1:L239").Select
    ActiveWorkbook.Worksheets("newdata").Sort.SortFields.Clear
    ActiveWorkbook.Worksheets("newdata").Sort.SortFields.Add2 Key:=Range( _
        "A1:A239"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    With ActiveWorkbook.Worksheets("newdata").Sort
        .SetRange Range("A2:L239")
        .Header = xlNo
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
    Rows("161:161").Select
    Selection.delete Shift:=xlUp
    Rows("83:83").Select
    Selection.delete Shift:=xlUp

    Columns("C:F").Select
    Selection.delete Shift:=xlToLeft
    Columns("D:E").Select
    Selection.delete Shift:=xlToLeft
    Columns("E:F").Select
    Selection.delete Shift:=xlToLeft
    Columns("C:C").Select
    Selection.Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
    
    Workbooks("Book1.xlsx").Worksheets("Sheet1").Range("A1:E1").Copy _
    Workbooks("newdata.csv").Worksheets("newdata").Range("A1")
    
    Workbooks("Book1.xlsx").Worksheets("Sheet1").Range("B2:C237").Copy _
    Workbooks("newdata.csv").Worksheets("newdata").Range("B2")

    
End Sub

