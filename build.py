# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:33:13 2022

@author: austin.pursley
"""

import jinja2
from pathlib import Path
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
import re

def int2alpha(number):
    # converts number to alphabet equivalent
    # A is 1, B is 2, etc.
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
                'Q','R','S','T','U','V','W','X','W','Z']
    q, m = divmod((number-1),26)
    if q == 0:
        return alphabet[m]
    else:
        return int2alpha(abs(q)) + alphabet[m]
    
def int2word(number):
    # converts number to word equivalent
    # 1 is one, 45 is fourfive, etc..
    number = int(number)
    alphabet = ['zero','one','two','three','four','five','six','seven','eight','nine']
    word_number = ""
    for digit in [int(i) for i in str(number)]:
        word_number += alphabet[digit]
    return word_number

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
    oupt = re.sub("[0-9]", lambda x : int2word(x.group(0)), oupt)
    oupt = re.sub("[^a-zA-Z]", "", oupt)
    return oupt

def buildOutlineDataFromTitles(section_titles, 
                               label_prefix="",sub_prefix="", label_track=[]):
    sections = []
    for t in section_titles:
        entry_subsections = None
        if isinstance(t, str): # no subsections
            entry_title = t
        elif isinstance(t, dict): # yes subsections
            entry_title = list(t.keys())[0]
            entry_subsections = buildOutlineDataFromTitles(
                       list(t.values())[0], "s", sub_prefix + "s", label_track)
        entry_label = label_prefix + sub_prefix + str2acronym(entry_title)
        # avoid duplicate labels
        if entry_label not in label_track:
            label_track.append(entry_label)
        else:
            cnt = 1
            entry_label_base = entry_label
            while entry_label in label_track:
                cnt += 1
                entry_label = entry_label_base + int2word(cnt)
            label_track.append(entry_label)
        entry = {"title" : entry_title, "label" : entry_label}
        if entry_subsections:
            entry["subsection"] = entry_subsections
        sections.append(entry)
    return sections
        
def setup_latex_doc(section_titles, appendix_titles, out_dir,
                    doc_title = "Default Document Title",
                    static_dir = "static/",
                    templates_dir = "templates/",
                    temp_main_fn = "main.tex",
                    temp_sub_fn = "sub.tex"):
    # output directory set-up
    remove_tree(out_dir)
    Path(out_dir).mkdir(exist_ok=True)
    sec_dir = out_dir + "Sections/"
    apx_dir = out_dir + "Appendices/"
    Path(sec_dir).mkdir(exist_ok=True)
    Path(apx_dir).mkdir(exist_ok=True)

    # set-up Jinja template environment
    templateLoader = jinja2.FileSystemLoader(searchpath=templates_dir)
    templateEnv = jinja2.Environment(loader=templateLoader)
    main_temp = templateEnv.get_template(temp_main_fn)
    sub_temp = templateEnv.get_template(temp_sub_fn)

    # build data from input
    # title and label
    sections = buildOutlineDataFromTitles(section_titles,label_prefix="s")
    appendices = buildOutlineDataFromTitles(appendix_titles,label_prefix="a")
    # filename
    for cnt, s in enumerate(sections):
        s["filename"] = str(cnt+1).zfill(2) + "_" + re.sub("[^a-zA-Z\d]", "", s["title"]) 
    for cnt, a in enumerate(appendices):
        a["filename"] = int2alpha(cnt+1) + "_" + re.sub("[^a-zA-Z\d]", "", a["title"])
    data = {"doc_title" : doc_title,
            "sections" : sections,
            "appendices" : appendices}
    # render templates
    main_tex = (main_temp.render(data))
    p = Path(out_dir + "main.tex")
    with open(p, 'w') as f:
        f.write(main_tex)

    for s in data["sections"]:
        data_sub = {"title" : s["title"],
                "label" : s["label"]}
        if "subsection" in s:
            data_sub["subsection"] = s["subsection"]
        sub_tex = (sub_temp.render(data_sub))
        p = Path(sec_dir + s["filename"] + ".tex")
        with open(p, 'w') as f:
            f.write(sub_tex)
    
    for s in data["appendices"]:
        data_sub = {"title" : s["title"],
                "label" : s["label"]}
        if "subsection" in s:
            data_sub["subsection"] = s["subsection"]
        sub_tex = (sub_temp.render(data_sub))
        p = Path(apx_dir + s["filename"] + ".tex")
        with open(p, 'w') as f:
            f.write(sub_tex)
            
    # copy "static" files
    if isinstance(static_dir, str):
        copy_tree(static_dir, out_dir)
    elif isinstance(static_dir, list):
        for d in static_dir:
            copy_tree(d, out_dir)
