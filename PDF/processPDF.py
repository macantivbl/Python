import PyPDF2

with open('dummy.pdf','rb') as File:
    reader = PyPDF2.PdfFileReader(File)
    print(reader.numPages)
    print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('Salida.pdf','wb') as nw_file:
        writer.write(nw_file)
    print(reader)
