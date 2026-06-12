

### 1. Sub ControlePATIVA repetida:

 - Função antiga (provável duplicante)
```vb
Sub ControlePATIVA()
    Dim wsPAGCV As Worksheet, wsPABTI As Worksheet, wsCONTROLEPA As Worksheet
    Dim mapK As Object, setK As Object
    Dim ws As Worksheet, lastB As Long, r As Long
    Dim key As String, kSrc As String, kCtl As String
    Dim arr As Variant, a As Long
    Dim ultimaLinhaCONTROLEPA As Long

    Set wsPAGCV = ThisWorkbook.Sheets("PA GCV")
    Set wsPABTI = ThisWorkbook.Sheets("PA BTI")
    Set wsCONTROLEPA = ThisWorkbook.Sheets("CONTROLE PA")
    Set mapK = CreateObject("Scripting.Dictionary")

    ' 1) Coletar K por chave nas abas de origem (forma estável)
    arr = Array(wsPAGCV, wsPABTI)
    For a = LBound(arr) To UBound(arr)
        Set ws = arr(a)
        lastB = ws.Cells(ws.Rows.Count, "B").End(xlUp).Row
        For r = 7 To lastB
            If Trim(ws.Cells(r, "E").Value) <> "" Then
                key = Trim(ws.Cells(r, "B").Value) & "|" & Trim(ws.Cells(r, "E").Value)
                kSrc = Trim(ws.Cells(r, "K").Value & "")
                If Len(key) > 1 And Len(kSrc) > 0 Then
                    If Not mapK.Exists(key) Then
                        Set setK = CreateObject("Scripting.Dictionary")
                        mapK.Add key, setK
                    End If
                    Set setK = mapK(key)
                    setK(kSrc) = True
                End If
            End If
        Next r
    Next a

    ' 2) Excluir se K divergir (exclusão de linhas inconsistentes)
    ultimaLinhaCONTROLEPA = wsCONTROLEPA.Cells(wsCONTROLEPA.Rows.Count, "B").End(xlUp).Row
    For r = ultimaLinhaCONTROLEPA To 7 Step -1
        key = Trim(wsCONTROLEPA.Cells(r, "B").Value) & "|" & Trim(wsCONTROLEPA.Cells(r, "E").Value)
        If mapK.Exists(key) Then
            kCtl = Trim(wsCONTROLEPA.Cells(r, "K").Value & "")
            If Len(kCtl) = 0 Then
                wsCONTROLEPA.Rows(r).Delete
            Else
                Set setK = mapK(key)
                If Not setK.Exists(kCtl) Then wsCONTROLEPA.Rows(r).Delete
            End If
        End If
    Next r

    Application.CutCopyMode = Fals

    ' 3) Atualizar coluna J (DATA LT) em CONTROLE PA com valor de PA GCV correspondente
    Dim ultimaLinha As Long, cel As Range, keyCtl As String, dictDataLT As Object
    ultimaLinha = wsCONTROLEPA.Cells(wsCONTROLEPA.Rows.Count, "M").End(xlUp).Row
    Set dictDataLT = CreateObject("Scripting.Dictionary")
    ' Monta dicionário com chave B|E e valor J da PA GCV
    Dim lastPAGCV As Long, rPAGCV As Long, keyPAGCV As String
    lastPAGCV = wsPAGCV.Cells(wsPAGCV.Rows.Count, "B").End(xlUp).Row
    For rPAGCV = 7 To lastPAGCV
        keyPAGCV = Trim(wsPAGCV.Cells(rPAGCV, "B").Value) & "|" & Trim(wsPAGCV.Cells(rPAGCV, "E").Value)
        If Len(keyPAGCV) > 1 Then
            dictDataLT(keyPAGCV) = wsPAGCV.Cells(rPAGCV, "J").Value
        End If
    Next rPAGCV
    ' Atualiza coluna J em CONTROLE PA
    For r = 7 To ultimaLinha
        keyCtl = Trim(wsCONTROLEPA.Cells(r, "B").Value) & "|" & Trim(wsCONTROLEPA.Cells(r, "E").Value)
        If dictDataLT.Exists(keyCtl) Then
            wsCONTROLEPA.Cells(r, "J").Value = dictDataLT(keyCtl)
        End If
    Next r
    ' Pintar células conforme status (Finalizado, Pendente, Em andamento)
    For Each cel In wsCONTROLEPA.Range("M7:M" & ultimaLinha)
        Select Case Trim(UCase(cel.Value))
            Case "FINALIZADO"
                cel.Interior.Color = RGB(146, 208, 80) ' Verde
            Case "PENDENTE"
                cel.Interior.Color = RGB(255, 192, 0) ' Amarelo
            Case "EM ANDAMENTO"
                cel.Interior.Color = RGB(173, 216, 230) ' Azul claro
            Case Else
                cel.Interior.ColorIndex = xlNone
        End Select
    Next cel

    ' 4) Ordenar por datas da coluna J (Data LT) diretamente, sem tratar "NA" como data máxima
    ultimaLinha = wsCONTROLEPA.Cells(wsCONTROLEPA.Rows.Count, "B").End(xlUp).Row
    Dim tempRng As Range
    Set tempRng = wsCONTROLEPA.Range("B7:J" & ultimaLinha)
    With wsCONTROLEPA.Sort
        .SortFields.Clear
        .SortFields.Add key:=wsCONTROLEPA.Range("J7:J" & ultimaLinha), _
            SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
        .SetRange tempRng
        .Header = xlNo
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With

    ' 5) Ordenar por status da coluna M, "Finalizado" no final
    ' Adiciona coluna auxiliar AA para status
    Dim auxCol As String: auxCol = "AA"
    For r = 7 To ultimaLinha
        Select Case Trim(UCase(wsCONTROLEPA.Cells(r, "M").Value))
            Case "FINALIZADO"
                wsCONTROLEPA.Cells(r, auxCol).Value = 2
            Case Else
                wsCONTROLEPA.Cells(r, auxCol).Value = 1
        End Select
    Next r
    Set tempRng = wsCONTROLEPA.Range("B7:" & auxCol & ultimaLinha)
    With wsCONTROLEPA.Sort
        .SortFields.Clear
        .SortFields.Add key:=wsCONTROLEPA.Range(auxCol & "7:" & auxCol & ultimaLinha), _
            SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
        .SetRange tempRng
        .Header = xlNo
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
    wsCONTROLEPA.Range(auxCol & "7:" & auxCol & ultimaLinha).ClearContents ' Limpa coluna auxiliar
End Sub

Private Sub ResetarCF_CONTROLEPA()
    Dim ws As Worksheet
    Dim fc As FormatCondition
    Dim idx As Variant

    Set ws = ThisWorkbook.Worksheets("CONTROLE PA")

    ' Zera CF
    ws.Cells.FormatConditions.Delete

    ' J < HOJE()
    Columns("J:J").Select
    Selection.FormatConditions.Add Type:=xlExpression, Formula1:= _
        "=E(M1<>""finalizado""; M1<>""""; J1<HOJE())"
    Selection.FormatConditions(Selection.FormatConditions.Count).SetFirstPriority
    With Selection.FormatConditions(1).Interior
        .PatternColorIndex = xlAutomatic
        .Color = 255
        .TintAndShade = 0
    End With
    Selection.FormatConditions(1).StopIfTrue = False

    ' M = Status
    With ws.Range("M7:M1048576")
        ' Finalizado -> verde
        Set fc = .FormatConditions.Add(Type:=xlCellValue, Operator:=xlEqual, Formula1:="=""Finalizado""")
        fc.Interior.Color = RGB(146, 208, 80)
        fc.StopIfTrue = True

        ' Pendente -> amarelo
        Set fc = .FormatConditions.Add(Type:=xlCellValue, Operator:=xlEqual, Formula1:="=""Pendente""")
        fc.Interior.Color = RGB(255, 192, 0)
        fc.StopIfTrue = True

        ' Em andamento -> azul claro
        Set fc = .FormatConditions.Add(Type:=xlCellValue, Operator:=xlEqual, Formula1:="=""Em andamento""")
        fc.Interior.Color = RGB(173, 216, 230)
        fc.StopIfTrue = True
    End With

    ' Bordas da “tabela”: B7:M10000 quando B tiver valor
    Set fc = ws.Range("B7:M10000").FormatConditions.Add(Type:=xlExpression, Formula1:="=$B7<>""""")
    For Each idx In Array(xlLeft, xlRight, xlTop, xlBottom)
        With fc.Borders(idx)
            .LineStyle = xlContinuous
            .Weight = xlThin
            .Color = RGB(200, 200, 200)
        End With
    Next idx
End Sub
```