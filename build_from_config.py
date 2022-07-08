# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:33:13 2022

@author: austin.pursley
"""

import yaml
from yaml.loader import SafeLoader
import build
# input data
config_file = "config.yaml"
with open(config_file, 'r') as f:
    config = yaml.load(f, Loader=SafeLoader)

build.setup_latex_doc(config["Sections"], config["Appendices"], config["out_dir"],
                      doc_title = config["doc_title"],
                      static_dir = config["static_dir"],
                      templates_dir = config["templates_dir"],
                      temp_main_fn = config["template_main"],
                      temp_sub_fn = config["template_sub"])
