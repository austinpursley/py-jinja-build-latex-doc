# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:20:38 2022

@author: austin.pursley
"""

import build

section_titles = ["Introduction", "All About Bugs"]
appendix_titles = ["List of Many Things"]
out_dir = "out_doc_test2/"

build.setup_latex_doc(section_titles, appendix_titles, out_dir, temp_sub_fn = "sub-plus.tpl")