```vba
Public Sub Cria_Etiqueta()
    
    Application.ScreenUpdating = False

    'ThisWorkbook.Sheets("Etiquetas").Visible = True
    ThisWorkbook.Sheets("Etiquetas").Cells.Delete Shift:=xlUp
    ThisWorkbook.Sheets("Etiquetas").DrawingObjects.Delete
    
    Dim ind As Integer
    Dim linha As Integer
    Dim vQtdEtq, NumCar As Integer
    
    ind = 9
    linha = 1
    
    ThisWorkbook.Sheets("Modelo").Visible = True

    Do While ThisWorkbook.Sheets("Dados").Cells(ind, 1).Value <> ""
    vQtdEtq = ThisWorkbook.Sheets("Dados").Cells(ind, 4).Value
    If vQtdEtq = 0 Then vQtdEtq = 1
    If Not IsNumeric(vQtdEtq) Then vQtdEtq = 1
        For i = 1 To vQtdEtq
            ThisWorkbook.Sheets("Modelo").Select
            ThisWorkbook.Sheets("Modelo").Rows("2:11").Select
            Selection.Copy
            ThisWorkbook.Sheets("Etiquetas").Select
    
            
            ThisWorkbook.Sheets("Etiquetas").Cells(linha, 1).Select
            
            Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, _
            SkipBlanks:=False, Transpose:=False
            
            ActiveSheet.Paste
            
            ThisWorkbook.Sheets("Etiquetas").Cells(linha, 6).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(4, 5).Value)         'PEP                | CAMPO FIXO
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 3, 1).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(ind, 3).Value)   'DESCRIÇÃO MATERIAL | CAMPO MÓVEL
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 5, 3).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(ind, 2).Value)   'COD MATERIAL       | CAMPO MÓVEL
            If Len(ThisWorkbook.Sheets("Dados").Cells(5, 2).Value) <> 8 Then GoTo MsgErroCentro
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 8, 1).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(5, 2).Value)     'CP                 | CAMPO FIXO
            'If Len(ThisWorkbook.Sheets("Dados").Cells(6, 2).Value) <> 10 Then GoTo MsgErroNumSer
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 8, 3).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(6, 2).Value)     'NUM SERIE          | CAMPO FIXO
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 8, 5).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(4, 2).Value)     'PEP                | CAMPO FIXO
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 5, 1).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(ind, 1).Value)   'QTD                | CAMPO MÓVEL
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 5, 5).Value = Trim(ThisWorkbook.Sheets("Dados").Cells(3, 2).Value)     'CLIENTE            | CAMPO FIXO
            
            ResizeFont ThisWorkbook.Sheets("Etiquetas").Cells(linha + 3, 1)
            ResizeFont ThisWorkbook.Sheets("Etiquetas").Cells(linha + 5, 5)
            
            'Inserir máscara PEP
            pep = ThisWorkbook.Sheets("Etiquetas").Cells(linha + 8, 5).Value
            pep = Left(pep, 3) & "-" & Mid(pep, 5, 7) & "-" & Mid(pep, 13, 4)
            ThisWorkbook.Sheets("Etiquetas").Cells(linha + 8, 5).Value = pep
            
            linha = linha + 10
            
        Next i

        ind = ind + 1

    Loop
    
    ThisWorkbook.Sheets("Etiquetas").Columns("A:F").ColumnWidth = 8
        

    ThisWorkbook.Sheets("Modelo").Visible = False
    ThisWorkbook.Sheets("Etiquetas").Select
    Cells(1, 1).Select
    Exit Sub
    
MsgErroCentro:
    NumCar = Len(ThisWorkbook.Sheets("Dados").Cells(5, 2).Value)
    MsgBox ("A CP tem " & NumCar & " dígitos ao invés de 8")
    ThisWorkbook.Sheets("Etiquetas").Cells.Delete Shift:=xlUp
    ThisWorkbook.Sheets("Etiquetas").DrawingObjects.Delete
    ThisWorkbook.Sheets("Dados").Select
    Cells(5, 2).Select
    MsgBox ("Finalizado com Sucesso!")
    
    Application.ScreenUpdating = True
    Exit Sub
    
MsgErroNumSer:
    NumCar = Len(ThisWorkbook.Sheets("Dados").Cells(6, 2).Value)
    MsgBox ("O Número de Série tem " & NumCar & " dígitos ao invés de 10")
    ThisWorkbook.Sheets("Etiquetas").Cells.Delete Shift:=xlUp
    ThisWorkbook.Sheets("Etiquetas").DrawingObjects.Delete
    ThisWorkbook.Sheets("Dados").Select
    Cells(6, 2).Select
    Exit Sub

End Sub


Sub ResizeFont(ByVal Target As Range)
    With Target
        If .MergeCells And .WrapText Then
            numColumns = Target.MergeArea.Columns.Count
            Set firstCell = Target.Cells(1, 1)
            ColumnWidth = firstCell.ColumnWidth
            RowHeight = firstCell.RowHeight
            Set mergedArea = firstCell.MergeArea
            For Each cell In mergedArea.Cells
                MergeWidth = MergeWidth + cell.ColumnWidth
            Next
            
            mergedArea.MergeCells = False
            firstCell.ColumnWidth = MergeWidth
            firstCell.EntireRow.AutoFit
            newRowHeight = firstCell.RowHeight
            
            While newRowHeight > RowHeight And firstCell.Font.Size > 3
                firstCell.Font.Size = firstCell.Font.Size - 1
                firstCell.EntireRow.AutoFit
                newRowHeight = firstCell.RowHeight
            Wend
            
            firstCell.ColumnWidth = ColumnWidth
            
            Target.Resize(1, numColumns).MergeCells = True
            Target.RowHeight = RowHeight
            ColumnWidth = 0: MergeWidth = 0
        End If
    End With
End Sub


Sub DelLinhas()
    ThisWorkbook.Sheets("Dados").Rows("9:1000").Delete
End Sub



Public Function code128$(chaine$)
  'This function is governed by the GNU Lesser General Public License (GNU LGPL)
 'V 2.0.0
 'Parameters : a string
 'Return : * a string which give the bar code when it is dispayed with CODE128.TTF font
 '         * an empty string if the supplied parameter is no good
 Dim i%, checksum&, mini%, dummy%, tableB As Boolean
  code128$ = ""
  If Len(chaine$) > 0 Then
  'Check for valid characters
   For i% = 1 To Len(chaine$)
      Select Case Asc(Mid$(chaine$, i%, 1))
      Case 32 To 126, 203
      Case Else
        i% = 0
        Exit For
      End Select
    Next
    'Calculation of the code string with optimized use of tables B and C
   code128$ = ""
    tableB = True
    If i% > 0 Then
      i% = 1 'i% devient l'index sur la chaine / i% become the string index
     Do While i% <= Len(chaine$)
        If tableB Then
          'See if interesting to switch to table C
         'yes for 4 digits at start or end, else if 6 digits
         mini% = IIf(i% = 1 Or i% + 3 = Len(chaine$), 4, 6)
          GoSub testnum
          If mini% < 0 Then 'Choice of table C
           If i% = 1 Then 'Starting with table C
             code128$ = Chr$(205)
            Else 'Switch to table C
             code128$ = code128$ & Chr$(199)
            End If
            tableB = False
          Else
            If i% = 1 Then code128$ = Chr$(204) 'Starting with table B
         End If
        End If
        If Not tableB Then
          'We are on table C, try to process 2 digits
         mini% = 2
          GoSub testnum
          If mini% < 0 Then 'OK for 2 digits, process it
           dummy% = Val(Mid$(chaine$, i%, 2))
            dummy% = IIf(dummy% < 95, dummy% + 32, dummy% + 100)
            code128$ = code128$ & Chr$(dummy%)
            i% = i% + 2
          Else 'We haven't 2 digits, switch to table B
           code128$ = code128$ & Chr$(200)
            tableB = True
          End If
        End If
        If tableB Then
          'Process 1 digit with table B
         code128$ = code128$ & Mid$(chaine$, i%, 1)
          i% = i% + 1
        End If
      Loop
      'Calculation of the checksum
     For i% = 1 To Len(code128$)
        dummy% = Asc(Mid$(code128$, i%, 1))
        dummy% = IIf(dummy% < 127, dummy% - 32, dummy% - 100)
        If i% = 1 Then checksum& = dummy%
        checksum& = (checksum& + (i% - 1) * dummy%) Mod 103
      Next
      'Calculation of the checksum ASCII code
     checksum& = IIf(checksum& < 95, checksum& + 32, checksum& + 100)
      'Add the checksum and the STOP
     code128$ = code128$ & Chr$(checksum&) & Chr$(206)
    End If
  End If
  Exit Function
testnum:
  'if the mini% characters from i% are numeric, then mini%=0
 mini% = mini% - 1
  If i% + mini% <= Len(chaine$) Then
    Do While mini% >= 0
      If Asc(Mid$(chaine$, i% + mini%, 1)) < 48 Or Asc(Mid$(chaine$, i% + mini%, 1)) > 57 Then Exit Do
      mini% = mini% - 1
    Loop
  End If
Return
End Function




```