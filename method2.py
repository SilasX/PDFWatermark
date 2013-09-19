import sys
import os

from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName, IndirectPdfDict, PdfArray
from pdfrw.buildxobj import pagexobj

WATERMARK_PATH = "inputs/watermark.png"
PDF_PATH = "inputs/phd_preneel_feb1993.pdf"
OUTPUT_FILE = "outputs/WMfull_phd_preneel_feb1993.pdf"


def watermark(input_fname, watermark_fname, output_fname=None):
    outfn = output_fname or ('watermark.' + os.path.basename(input_fname))
    w = pagexobj(PdfReader(watermark_fname, decompress=False).pages[0])
    pages = PdfReader(input_fname, decompress=False).pages
    PdfWriter().addpages([fixpage(x, w) for x in pages]).write(outfn)
    return outfn

watermark(PDF_PATH, WATERMARK_PATH, OUTPUT_FILE)
