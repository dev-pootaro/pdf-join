"""
main.py
export function pdf_join
"""

import glob
import time
import os
import logging
import re
from pypdf import PdfWriter
from natsort import natsorted


def pdf_join(
    input_dir,
    output_dir='dist/',
    marged_file_name='merged.pdf',
    log_file_name='pdf-join.log',
):
    """
    pdf_join function.
    Args:
        input_dir (string):*reqired input directory
        output_dir (string): output directory (default='dist/')
        marged_file_name (string): marged pdf file name (default='merged.pdf')
        log_file_name (string): log file name (default='pdf-join.log')
    """

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        filename=log_file_name,
        encoding='utf-8',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S',
    )

    start = time.time()

    logger.info('pdf_join start.')
    logger.info(
        'paramater=[input_dir=%s,output_dir=%s,marged_file_name=%s]',
        input_dir,
        output_dir,
        marged_file_name,
    )

    if not input_dir:
        logger.error('input_dir is required.')
        return

    dir_pattern = '.*/$'
    input_dir = input_dir + ('*' if re.compile(dir_pattern).match(input_dir) else '/*')
    output_dir = output_dir + ('' if re.compile(dir_pattern).match(output_dir) else '/')

    try:
        file_dirs = glob.glob(input_dir)
        if len(file_dirs) < 1:
            # pylint: disable=broad-exception-raised
            raise Exception(f'no search file directorys in "{input_dir}".')
        for file_dir in file_dirs:
            merger = PdfWriter()
            files = natsorted(glob.glob(file_dir + '/*.pdf'), reverse=True)
            for file in files:
                merger.append(file)
            dir_names = file_dir.split("/")
            last_dir_name = dir_names[len(dir_names) - 1] + '/'
            out_dir_name = output_dir + last_dir_name
            os.makedirs(out_dir_name, exist_ok=True)
            merger.write(out_dir_name + marged_file_name)
            merger.close()
            logger.info(
                'marged %i files and created file : %s',
                len(files),
                last_dir_name + marged_file_name,
            )
    # pylint: disable=broad-except
    except Exception as e:
        logger.exception(e)

    end = time.time()
    logger.info('pdf_join finish : %ss', str(end - start))
