import io
from PyPDF2 import PdfFileWriter, PdfFileReader

def ReadPdfFile( fName ):
    found = False
    while( not found ):
        try:
            with open( fName, 'rb' ) as f:
                found = True
                print(PdfFileReader)
                return PdfFileReader(f)
        except FileNotFoundError:
            print( "File not found: " , fName )
        fName = input( "Enter filename :> ")

def ReversePdf( pdfFile ):
    revPdf = PdfFileWriter()
    endPage = pdfFile.getNumPages()
    for i in reversed(range(endpage)):
        revPdf.addPage(pdfFile.getpage(i))
    return revPdf


#outputNameStr = input( "Output filename:" )
#outPdf = PdfFileWriter()


if __name__ == "__main__":
    print("-=-=- MergeBrother -=-=-")
    print("Please enter the first and second file names to merge, and the output file name")
    #fName1 = input( "File 1 (odd pages straight) :> " )
    fName1 = "first.pdf"
    pdf1 = PdfFileReader(open( fName1, 'rb' ))
    #fName2 = input( "File 2 (even pages reverse) :> " )
    fName2 = "second.pdf"
    pdf2 = PdfFileReader(open( fName2, 'rb' ))
    #outfile = input( "Output file name :> " )
    outfile = "merged.pdf"
    outputStream = open(outfile, 'wb')

    revPdf = PdfFileWriter()
    endPage2 = pdf2.getNumPages()
    endPage1 = pdf1.getNumPages()

    for i in reversed(range(endPage2)):
        revPdf.addPage(pdf2.getPage(i))
    pdf2 = revPdf

    outPdf = PdfFileWriter()
    for i in range(endPage2):
        outPdf.addPage(pdf1.getPage(i))
        outPdf.addPage(pdf2.getPage(i))

    #pdf2 = revPdf.write(outputStream)
    outPdf.write(outputStream)
    outputStream.close()


