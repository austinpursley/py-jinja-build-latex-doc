%========================================================
% CLASS PROVIDED STATEMENT
%========================================================
\ProvidesClass{myArticleClass}[My Article Class]

%========================================================
% CLASS OPTIONS
%========================================================
\LoadClass[11pt, twoside, titlepage]{article}

%========================================================
% Import packages for use
%========================================================
% The geometry of the page is specified in the following line
\RequirePackage[margin=1in, inner=1in, outer=1in, hmarginratio=1:1, paperwidth=8.5in, paperheight=11in, includefoot]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage[pdftex]{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage[toc,page,title,titletoc]{appendix}
\RequirePackage{array}
\RequirePackage{import}
\RequirePackage[subpreambles]{standalone}

\graphicspath{{Resources/Figures/} } % Figure path, relative to the main .tex file 
	
%========================================================
% Glossary, Acronyms
%========================================================
% glossary-extra OPTIONS: 
% "automake" option makes new glossary types work
% "abbreviations" sets an associated conditional which is used to determine
%                 whether or not to define a separate glossary for acronyms. 
% "nopostdot" Boolean option to suppress post description dot. 
% "nonumberlist' suppresses or activates the number list for the given entry. 
% "numberedsection" determines if this glossary should be in a numbered section.
% "nogroupskip" turns off grouping acronyms by letter
% "shortcuts=abbreviations" turns on ability to use abbreviation shortcuts for gls commands
\RequirePackage[automake,abbreviations,nopostdot,nonumberlist,numberedsection,nogroupskip,shortcuts=abbreviations]{glossaries-extra}
\makeglossaries

\loadglsentries{Resources/Glossary.tex}
\loadglsentries{Resources/Acronyms.tex}

%========================================================
% References / Bibliography
%========================================================
\RequirePackage[style=numeric,giveninits=true,sorting=none]{biblatex}% "style=numeric" is default
\addbibresource{Resources/References.bib} % bib style
