# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:33:13 2022

@author: austin.pursley

This script is used for creating a template LaTeX document.
Set-up includes:
- Writing the main.tpl and sub.tpl Jinja template files
- Setting-up files to copy into project in the "include" folder
- In this file, set-up the list of setcions and appendices for the document
"""

import jinja2
from pathlib import Path
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree

def int2alpha(number):
    return chr(ord('@')+number)

def str2acronym(stng):
   
    # add first letter
    oupt = stng[0]
     
    # iterate over string
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
           
            # add letter next to space
            oupt += stng[i]
             
    # uppercase oupt
    oupt = oupt.upper()
    return oupt

# output directory set-up
out_dir = "out_doc_0/"
remove_tree(out_dir)
Path(out_dir).mkdir(exist_ok=True)
sec_dir = out_dir + "Sections/"
apx_dir = out_dir + "Appendices/"
Path(sec_dir).mkdir(exist_ok=True)
Path(apx_dir).mkdir(exist_ok=True)

# list of document main body document sections and appendices
section_titles = ["Hipster Ipsum", "Taco Wayfarers"]
appendix_titles = ["Banjo Greenjuice", "Roof Bar Chia Seeds",
                   "Mumblecore Distillery"]

# build up data from input
sections = []
for cnt, title in enumerate(section_titles):
    filename = str(cnt+1).zfill(2) + "_" + title.replace(" ", "")
    label = "s" + str2acronym(title)
    sections.append({"title" : title, "filename" : filename, "label" : label})
    
appendices = []
for cnt, title in enumerate(appendix_titles):
    filename = int2alpha(cnt+1) + "_" + title.replace(" ", "")
    label = "a" + str2acronym(title)
    appendices.append({"title" : title, "filename" : filename, "label" : label})
data = {"sections" : sections,
        "appendices" : appendices}

# set-up Jinja template environment
templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
main_temp = templateEnv.get_template("main.tpl")
sub_temp = templateEnv.get_template("sub.tpl")
# render templates
main_tex = (main_temp.render(data))
p = Path(out_dir + "main.tex")
with open(p, 'w') as f:
    f.write(main_tex)

for s in sections:
    data = {"title" : s["title"],
            "label" : s["label"]}
    sub_tex = (sub_temp.render(data))
    p = Path(sec_dir + s["filename"] + ".tex")
    with open(p, 'w') as f:
        f.write(sub_tex)
        
for a in appendices:
    data = {"title" : a["title"],
            "label" : a["label"]}
    sub_tex = (sub_temp.render(data))
    p = Path(apx_dir + a["filename"] + ".tex")
    with open(p, 'w') as f:
        f.write(sub_tex)
        
# copy "include" files
src_path = 'includes'
trg_path = out_dir
copy_tree(src_path, trg_path)
