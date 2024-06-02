# -*- coding: utf-8 -*-
"""
ReaderPDFImage : in charge to read PDF file and convert data of pages into
                 images.
"""

import fitz

from PIL import Image, ImageTk


class ReaderPDFImage:
    """
    Class in charge of read PDF file and converts data of pages into image.
    """

    def read_pdf(
        filename: str = None
    ) -> fitz.fitz.Document:
        """
        Reads data of PDF file or create a new PDF file.
        """
        if filename is None:
            return fitz.open()
        else:
            return fitz.open(filename, filetype='pdf')

    def to_image(
        pdf_document: fitz.fitz.Document,
        height: int,
        width: int
    ) -> list:
        """
        PDF file page image generator.
        """
        # images = []
        for page in pdf_document:
            page_pix = page.get_pixmap()
            currentImage = Image.frombytes(
                                    mode='RGB',
                                    size=[page_pix.width, page_pix.height],
                                    data=page_pix.samples
                                )

            resized_img = currentImage.resize(
                            (width, height),
                            Image.LANCZOS
                        )

            imageTK = ImageTk.PhotoImage(resized_img)
            yield imageTK