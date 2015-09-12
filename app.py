#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
from bottle import route, run, template, request, response

import os
import uuid

@route('/')
def get_simple_form():
    """
    Returns simple images upload form
    :return:
    """
    return ('<form action="/imgs" method="post" enctype="multipart/form-data">\n'
            '    Input: <input name="input" type="file">\n'
            '    Style: <input name="style" type="file">\n'
            '    <input value="Upload" type="submit">\n'
            '</form>')


@route('/imgs', method='POST')
def upload_imgs():
    """
    Upload input & style images and return id
    :return:
    """

    # get files
    input_img = request.files.get('input')
    style_img = request.files.get('style')
    if not check_img_png(input_img) or not check_img_png(style_img):
        return 'File extension not allowed.'

    # assign uuid
    id = uuid.uuid4()
    input_up_path = id.get_hex() + input_img.filename
    style_up_path = id.get_hex() + style_img.filename
    input_img.save(input_up_path)
    style_img.save(style_up_path)

    return template('Uploaded images. ID is "{{id}}".', id=id.get_hex())

def check_img_png(image):
    """
    Check whether
    :param image:
    :return:
    """
    name, ext = os.path.split(image.filename)
    return ext not in ('png', 'jpeg', 'jpg')

@route('/statuses/<id>')
def show_status(id=''):
    return


if __name__ == '__main__':
    run(debug=True)
