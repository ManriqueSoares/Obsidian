```vba
Sub export()

    LIST_FIRST_ROW = 6
    LIST_LENGTH_COLUMN = 12
    LIST_WIDTH_COLUMN = 13
    LIST_HEIGHT_COLUMN = 14

    TAGS_TOTAL_COLUMNS = 10
    TAGS_TOTAL_ROWS = 46
    TAGS_HEADER_FIRST_COLUMN = 3
    TAGS_HEADER_CONTENT_FIRST_COLUMN = 5
    TAGS_DESCRIPTION_FIRST_COLUMN = 1
    TAGS_QUANTITY_COLUMN = 9
    TAGS_OK_COLUMN = 10
    TAGS_CUSTOMER_FIRST_ROW = 1
    TAGS_CP_FIRST_ROW = 2
    TAGS_PEP_FIRST_ROW = 3
    TAGS_PACKING_FIRST_ROW = 4
    TAGS_MODEL_FIRST_ROW = 5
    TAGS_SERIAL_FIRST_ROW = 6
    TAGS_DIMENSIONS_FIRST_ROW = 7
    TAGS_VOLUME_ORDER_FIRST_ROW = 8
    TAGS_CONTENT_FIRST_ROW = 12

    TAGS_GUARNICAO_DESCRIPTION_FIRST_COLUMN = 1
    TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN = 6
    TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN = 8
    TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN = 9
    TAGS_GUARNICAO_OK_FIRST_COLUMN = 10

    ListRow = LIST_FIRST_ROW
    tagsCustomerRow = TAGS_CUSTOMER_FIRST_ROW
    tagsCpRow = TAGS_CP_FIRST_ROW
    tagsPepRow = TAGS_PEP_FIRST_ROW
    tagsPackingRow = TAGS_PACKING_FIRST_ROW
    tagsModelRow = TAGS_MODEL_FIRST_ROW
    tagsSerialRow = TAGS_SERIAL_FIRST_ROW
    tagsDimensionsRow = TAGS_DIMENSIONS_FIRST_ROW
    tagsVolumeOrderRow = TAGS_VOLUME_ORDER_FIRST_ROW
    tagsContentFirstRow = TAGS_CONTENT_FIRST_ROW
    validVolume = True

    DadosRow = 9

    Set WS_LIST = Worksheets("LISTA DE EMBAQUE NACIONAL")
    Set WS_DADOS = Worksheets("Dados")
    Set WS_ETIQUETAS = Worksheets("Etiquetas")
    
    originalPrinter = Application.ActivePrinter
    pdfPrinter = "Microsoft Print to PDF"
    
    If InStr(originalPrinter, pdfPrinter) = 0 Then
        Set resources = CreateObject("WScript.Network")
        resources.SetDefaultPrinter pdfPrinter
        
        If InStr(Application.ActivePrinter, pdfPrinter) = 0 Then
            MsgBox "Erro ao trocar impressora para '" & pdfPrinter & "'." & vbCrLf & "Por favor faça essa configuração manualmente."
        End If
    End If
    
    ThisWorkbook.Unprotect
    For Each ws In Worksheets
        ws.Unprotect
    Next
    Application.ScreenUpdating = False

    Application.DisplayAlerts = False
    For Each ws In ThisWorkbook.Worksheets
        If ws.Name = "Tags" Then
            ws.Delete
        End If
    Next ws

    Set WS_TAGS = Sheets.Add
    WS_TAGS.Name = "Tags"
    WS_TAGS.Columns("C").ColumnWidth = 9.57
    
    Err.Clear
    On Error Resume Next
    With WS_TAGS.PageSetup
        .PaperSize = xlPaperLetter
        .CenterFooter = "&""Arial,Regular""&9 TODOS OS ITENS DEVEM ESTAR CONFORME A ÚLTIMA VERSÃO DA LISTA DE EMBARQUE, NÃO PODENDO HAVER ALTERAÇÕES POR PARTE DA FÁBRICA. QUAISQUER ALTERAÇÕES DEVEM SER SOLICITADAS À ENGENHARIA."
        .LeftFooter = ""
        .RightFooter = ""
    End With
    If Err.Number <> 0 Then
        Worksheets("Definir impressora").Visible = True
        Worksheets("Definir impressora").Activate
        Exit Sub
    End If
    
    For Each Shape In Worksheets("Images").Shapes
        lastImageName = Shape.Name
    Next
    Worksheets("Images").Shapes(lastImageName).Copy
    DoEvents
    
    customer = FormatDescription(RemoveNewLines(UCase(WS_LIST.Cells(2, 10).Value)))
    CP = RemoveNewLines(WS_LIST.Cells(2, 5).Value)
    pep = RemoveNewLines(WS_LIST.Cells(1, 5).Value)
    packingMaterialNumber = RemoveNewLines(WS_LIST.Cells(3, 5).Value)
    modelNumber = RemoveNewLines(WS_LIST.Cells(1, 17).Value)
    serialNumber = RemoveNewLines(WS_LIST.Cells(1, 28).Value)

    DelLinhas

    WS_DADOS.Cells(3, 2) = customer
    WS_DADOS.Cells(4, 2) = pep
    WS_DADOS.Cells(5, 2) = CP
    WS_DADOS.Cells(6, 2) = serialNumber
    
    ' Novo loop: percorre todas as linhas usadas a partir de LIST_FIRST_ROW
    ' Processa apenas até a linha 35
    ' Processa apenas as linhas 6 a 26 da aba LISTA DE EMBAQUE NACIONAL
    ' Processa apenas as linhas 6 a 35 da aba LISTA DE EMBAQUE NACIONAL
    For i = 6 To 35
        Debug.Print "Processando linha geral: i=" & i & ", Quantidade=" & WS_LIST.Cells(i, 7).Value & ", Descrição='" & WS_LIST.Cells(i, 8).Value & "', Coluna J='" & WS_LIST.Cells(i, 10).Value & "'"
        If Not WS_LIST.Cells(i, 7).EntireRow.Hidden Then
            quantity = WS_LIST.Cells(i, 7)
            isInteger = True
            If (IsNumeric(quantity)) Then
                isInteger = Fix(quantity) = quantity
            End If
            Text = FormatDescription(WS_LIST.Cells(i, 8).Value)
            Text = FormatDescriptionText(Text)
            ' Verifica se quantidade é data
            If IsDate(quantity) Then
                Debug.Print "Pulando linha (quantidade é data): " & i & _
                             ", Quantidade: " & quantity & _
                             ", Descrição: '" & Text & "'"
            ElseIf quantity > 0 And isInteger And Text <> "" Then
                Debug.Print "Processando linha: " & i & _
                             ", Quantidade: " & quantity & _
                             ", Descrição: " & Text & _
                             ", Coluna J: " & WS_LIST.Cells(i, 10).Value
                WS_DADOS.Cells(DadosRow, 1) = quantity
                WS_DADOS.Cells(DadosRow, 3) = Text
                ' Nova coluna: valor da coluna J se contiver "PARTE" (apenas número)
                Dim valorColunaJ As String
                Dim valorNumericoJ As Double
                valorColunaJ = WS_LIST.Cells(i, 10).Value
                If InStr(UCase(valorColunaJ), "PARTE") > 0 Then
                    valorColunaJ = Replace(UCase(valorColunaJ), "PARTES", "")
                    valorColunaJ = Replace(valorColunaJ, "PARTE", "")
                    valorColunaJ = Trim(valorColunaJ)
                    If IsNumeric(valorColunaJ) Then
                        valorNumericoJ = CDbl(valorColunaJ)
                        WS_DADOS.Cells(DadosRow, 5) = valorNumericoJ
                    Else
                        WS_DADOS.Cells(DadosRow, 5) = ""
                    End If
                Else
                    WS_DADOS.Cells(DadosRow, 5) = ""
                End If
                ' Ajuste da coluna D: se E tiver valor, D = E, senão mantém valor
                If WS_DADOS.Cells(DadosRow, 5).Value <> "" Then
                    WS_DADOS.Cells(DadosRow, 4) = WS_DADOS.Cells(DadosRow, 5).Value
                Else
                    WS_DADOS.Cells(DadosRow, 4) = quantity
                End If
                DadosRow = DadosRow + 1
            Else
                Debug.Print "Pulando linha: " & i & _
                             ", Quantidade: " & quantity & _
                             ", isInteger: " & isInteger & _
                             ", Descrição: '" & Text & "'"
            End If
        End If
    Next

    hasFoundGuarnicao = False
    lastRow = WS_LIST.UsedRange.Rows.Count
    While (Not hasFoundGuarnicao And ListRow <= lastRow)
        Value = WS_LIST.Cells(ListRow, 2)
        If (Value = "Nº MATERIAL GUARNIÇÃO") Then
            hasFoundGuarnicao = True
        Else
            ListRow = ListRow + 1
        End If
    Wend

    If (hasFoundGuarnicao) Then
    
        guarnicaoMaterialNumber = WS_LIST.Cells(ListRow, 5).Value
        ListRow = ListRow + 2
        tagRow = tagsContentFirstRow
        
        validQuantity = True
        While (validQuantity)
        
            quantity = WS_LIST.Cells(ListRow, 2).Value
            
            If Not IsNumeric(Left(quantity, 1)) Then
                validQuantity = False
            End If
            
            If validQuantity Then

                applicationItem = WS_LIST.Cells(ListRow, 3).Value
                codeNumber = WS_LIST.Cells(ListRow, 12).Value
                dimensions = WS_LIST.Cells(ListRow, 14).Value

                applicationItem = FormatDescription(applicationItem)
                
                WS_DADOS.Cells(DadosRow, 1) = quantity
                WS_DADOS.Cells(DadosRow, 3) = applicationItem
                WS_DADOS.Cells(DadosRow, 4) = 1
                If Trim(dimensions) <> "" Then
                    WS_DADOS.Cells(DadosRow, 2) = dimensions
                Else
                    WS_DADOS.Cells(DadosRow, 2) = codeNumber
                End If
                ' Nova coluna: valor da coluna J se contiver "PARTE" (apenas número)
                Dim valorColunaJGuarnicao As String
                Dim valorNumericoJGuarnicao As Double
                valorColunaJGuarnicao = WS_LIST.Cells(ListRow, 10).Value
                If InStr(UCase(valorColunaJGuarnicao), "PARTE") > 0 Then
                    valorColunaJGuarnicao = Replace(UCase(valorColunaJGuarnicao), "PARTES", "")
                    valorColunaJGuarnicao = Replace(valorColunaJGuarnicao, "PARTE", "")
                    valorColunaJGuarnicao = Trim(valorColunaJGuarnicao)
                    If IsNumeric(valorColunaJGuarnicao) Then
                        valorNumericoJGuarnicao = CDbl(valorColunaJGuarnicao)
                        WS_DADOS.Cells(DadosRow, 5) = valorNumericoJGuarnicao
                    Else
                        WS_DADOS.Cells(DadosRow, 5) = ""
                    End If
                Else
                    WS_DADOS.Cells(DadosRow, 5) = ""
                End If
                ' Comparação e ajuste da coluna D
                If IsNumeric(WS_DADOS.Cells(DadosRow, 1).Value) And IsNumeric(WS_DADOS.Cells(DadosRow, 5).Value) Then
                    If WS_DADOS.Cells(DadosRow, 1).Value > WS_DADOS.Cells(DadosRow, 5).Value Then
                        WS_DADOS.Cells(DadosRow, 4) = WS_DADOS.Cells(DadosRow, 1).Value
                    Else
                        WS_DADOS.Cells(DadosRow, 4) = WS_DADOS.Cells(DadosRow, 5).Value
                    End If
                End If

                ''' Content
                ' Application item
                WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_DESCRIPTION_FIRST_COLUMN).Value = applicationItem
                With WS_TAGS.Range(WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_DESCRIPTION_FIRST_COLUMN), WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN - 1))
                    .Merge
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                    .WrapText = True
                    .EntireRow.AutoFit
                    .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
                End With

                ' Code number
                WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN).Value = codeNumber
                With WS_TAGS.Range(WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN), WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN - 1))
                    .Merge
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                    .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
                End With

                ' Dimensions
                WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN).Value = dimensions
                With WS_TAGS.Range(WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN), WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN - 1))
                    .Merge
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                    .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
                End With
                
                ' Quantity
                WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN).Value = quantity
                With WS_TAGS.Range(WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN), WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_OK_FIRST_COLUMN - 1))
                    .Merge
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                    .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
                End With

                ' OK
                With WS_TAGS.Range(WS_TAGS.Cells(tagRow, TAGS_GUARNICAO_OK_FIRST_COLUMN), WS_TAGS.Cells(tagRow, TAGS_TOTAL_COLUMNS))
                    .Merge
                    .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
                End With
                
                tagRow = tagRow + 1
                ListRow = ListRow + 1
                DadosRow = DadosRow + 1
           End If
        Wend
        
        WS_DADOS.Range(WS_DADOS.Cells(9, 1), WS_DADOS.Cells(DadosRow - 1, 4)).Borders.LineStyle = xlContinuous
        WS_DADOS.Range(WS_DADOS.Cells(9, 1), WS_DADOS.Cells(DadosRow - 1, 4)).Borders.Weight = 2
        WS_DADOS.Range(WS_DADOS.Cells(9, 1), WS_DADOS.Cells(DadosRow - 1, 4)).VerticalAlignment = xlVAlignCenter
        
        WS_TAGS.Range(WS_TAGS.Cells(tagsContentFirstRow - TAGS_CONTENT_FIRST_ROW + 1, 1), WS_TAGS.Cells(TAGS_TOTAL_ROWS + tagsContentFirstRow - TAGS_CONTENT_FIRST_ROW, 10)).Interior.Color = RGB(255, 255, 255)
                
        On Error Resume Next
        Sheets("Images").Pictures("Imagem 2").Copy
        DoEvents
        
        WS_TAGS.Cells(tagsCustomerRow, 1).PasteSpecial
        DoEvents
        
        For Each Shape In WS_TAGS.Shapes
            lastImageName = Shape.Name
        Next
        With WS_TAGS.Shapes(lastImageName)
            .Left = WS_TAGS.Cells(tagsCustomerRow, 1).Left
            .Top = WS_TAGS.Cells(tagsCustomerRow, 1).Top + 2
        End With
        DoEvents
        
        If Err.Number <> 0 Then
            MsgBox "Causa:" & vbTab & "erro ao inserir logo da WEG." & vbCrLf & "Local:" & vbTab & "folha da ordem " & currentVolume - 1 & "º." & vbCrLf & "Solução:" & vbTab & "insira a imagem manualmente.", vbExclamation, "Erro"
            Err.Clear
        End If
        On Error GoTo 0
        
        ''' HEADER
        ' Client
        WS_TAGS.Cells(tagsCustomerRow, TAGS_HEADER_FIRST_COLUMN) = "CLIENTE"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsCustomerRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsCustomerRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        With WS_TAGS.Range(WS_TAGS.Cells(tagsCustomerRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsCustomerRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With
        WS_TAGS.Cells(tagsCustomerRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = customer
        
        ' CP
        WS_TAGS.Cells(tagsCpRow, TAGS_HEADER_FIRST_COLUMN) = "CP"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsCpRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsCpRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsCpRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = CP
        With WS_TAGS.Range(WS_TAGS.Cells(tagsCpRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsCpRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With

        ' PEP
        WS_TAGS.Cells(tagsPepRow, TAGS_HEADER_FIRST_COLUMN) = "PEP"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsPepRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsPepRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsPepRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = pep
        With WS_TAGS.Range(WS_TAGS.Cells(tagsPepRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsPepRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With

        ' PACKING
        WS_TAGS.Cells(tagsPackingRow, TAGS_HEADER_FIRST_COLUMN) = "Nº EMBALAGEM"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsPackingRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsPackingRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsPackingRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = packingMaterialNumber
        With WS_TAGS.Range(WS_TAGS.Cells(tagsPackingRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsPackingRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With

        ' MODEL
        WS_TAGS.Cells(tagsModelRow, TAGS_HEADER_FIRST_COLUMN) = "Nº MODELO"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsModelRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsModelRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsModelRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = modelNumber
        With WS_TAGS.Range(WS_TAGS.Cells(tagsModelRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsModelRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With

        ' SERIAL
        WS_TAGS.Cells(tagsSerialRow, TAGS_HEADER_FIRST_COLUMN) = "Nº DE SÉRIE"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsSerialRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsSerialRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsSerialRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = serialNumber
        With WS_TAGS.Range(WS_TAGS.Cells(tagsSerialRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsSerialRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With

         ' Guarnição material number
        WS_TAGS.Cells(tagsDimensionsRow, TAGS_HEADER_FIRST_COLUMN) = "Nº GUARNIÇÃO"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsDimensionsRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsDimensionsRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsDimensionsRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = guarnicaoMaterialNumber
        With WS_TAGS.Range(WS_TAGS.Cells(tagsDimensionsRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsDimensionsRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With
        
        ' Volume order
        WS_TAGS.Cells(tagsVolumeOrderRow, TAGS_HEADER_FIRST_COLUMN) = "ORDEM VOLUME"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsVolumeOrderRow, TAGS_HEADER_FIRST_COLUMN), WS_TAGS.Cells(tagsVolumeOrderRow, TAGS_HEADER_CONTENT_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        WS_TAGS.Cells(tagsVolumeOrderRow, TAGS_HEADER_CONTENT_FIRST_COLUMN) = currentVolume & "º"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsVolumeOrderRow, TAGS_HEADER_CONTENT_FIRST_COLUMN), WS_TAGS.Cells(tagsVolumeOrderRow, TAGS_TOTAL_COLUMNS))
            .Merge
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
        End With

        
        ' Application item
        WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_DESCRIPTION_FIRST_COLUMN) = "ITEM DE APLICAÇÃO"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_DESCRIPTION_FIRST_COLUMN), WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With

        ' Code number
        WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN) = "Nº CÓDIGO"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_CODE_NUMBER_FIRST_COLUMN), WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With

        ' Dimensions
        WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN) = "DIMENSÕES"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_DIMENSIONS_FIRST_COLUMN), WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
        
        ' Quantity
        WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN) = "QTD"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_QUANTITY_FIRST_COLUMN), WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_OK_FIRST_COLUMN - 1))
            .Merge
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With

        ' Quantity
        WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_OK_FIRST_COLUMN) = "OK"
        With WS_TAGS.Range(WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_GUARNICAO_OK_FIRST_COLUMN), WS_TAGS.Cells(tagsContentFirstRow - 1, TAGS_TOTAL_COLUMNS))
            .Merge
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlCenter
            .BorderAround LineStyle:=xlContinuous, Weight:=xlThin
        End With
    End If
    
    Cria_Etiqueta

    WS_TAGS.Columns(7).ColumnWidth = 3.5
    WS_TAGS.Columns(8).ColumnWidth = 11.6

    WS_TAGS.Activate
    ActiveWindow.View = xlPageLayoutView
    WS_DADOS.Activate
    ActiveWindow.View = xlNormalView
    
    listPath = getDesktopPath() & "\ListaEmbarque.pdf"
    tagsPath = getDesktopPath() & "\Etiquetas.pdf"
    
    WS_TAGS.ExportAsFixedFormat Type:=xlTypePDF, Filename:=listPath, OpenAfterPublish:=True
    WS_ETIQUETAS.ExportAsFixedFormat Type:=xlTypePDF, Filename:=tagsPath, OpenAfterPublish:=True
    
    'resources.SetDefaultPrinter Split(originalPrinter, " em")(0)  ' Busca a impressora selecionada. Como não tenho nenhuma impressora selecionada ele está gerando erro!!
    
    
     
End Sub

Function formatVolume(volume)
    formatVolume = Trim(Replace(Replace(volume, "º", ""), "°", ""))
End Function

Function FormatDescription(description)
    Set regexNote = CreateObject("VBScript.RegExp")
    Set regexDetail = CreateObject("VBScript.RegExp")
    Set regexDrawing = CreateObject("VBScript.RegExp")

    regexNote.Pattern = "[(][vV][eE][rR]\s[nN][oO][tT][aA](.*)[)]"
    regexDetail.Pattern = "[(][vV][eE][rR]\s[dD][eE][tT][aA][lL][hH][eE](.*)[)]"
    regexDrawing.Pattern = "[(][vV][eE][rR]\s[dD][eE][sS][eE][nN][hH][oO]](.*)[)]"

    description = regexNote.Replace(description, "")
    description = regexDetail.Replace(description, "")
    description = regexDrawing.Replace(description, "")
    
    FormatDescription = Trim(description)
End Function

Function FormatPower(Text)
    Set regexPower = CreateObject("VBScript.RegExp")
    regexPower.Pattern = "\d{1,3}(,\d{3})*(\.\d+)?([\s*]|[kK]|[mM])([vV][aA]|[wW])"
    Text = regexPower.Replace(description, "")
    FormatPower = Trim(Text)
End Function

Function getDesktopPath()
    Dim oWSHShell As Object
    Set oWSHShell = CreateObject("WScript.Shell")
    getDesktopPath = oWSHShell.SpecialFolders("Desktop")
    Set oWSHShell = Nothing
End Function


Function AutofitMergedCells(ByVal Target As Range, ByVal tagsTotalRows As Integer)
    With Target
        If .MergeCells And .WrapText Then
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
            firstCell.ColumnWidth = ColumnWidth
            Merge = Int(newRowHeight / RowHeight) - 1
            numRows = Target.Rows.Count
            numColumns = Target.Columns.Count
            Target.Resize(numRows + Merge, numColumns).MergeCells = True
            ColumnWidth = 0: MergeWidth = 0
        End If
    End With
    
    Set AutofitMergedCells = firstCell.MergeArea
End Function

Function FormatDescriptionText(Text)
    Text = Trim(Text)
    While InStr(Text, "   ")
        Text = Replace(Text, "   ", "  ")
    Wend
    Text = Replace(Text, "  ", vbCrLf)
    FormatDescriptionText = Text
End Function

Function RemoveNewLines(Text)
    Text = Trim(Text)
    While InStr(Text, "  ")
        Text = Replace(Text, "  ", " ")
    Wend
    Text = Replace(Text, vbNewLine, "")
    Text = Replace(Text, Chr(10), "")
    Text = Replace(Text, vbCrLf, "")
    Text = Replace(Text, vbCr, "")
    Text = Replace(Text, vbLf, "")
    RemoveNewLines = Text
End Function
```