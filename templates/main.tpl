%===================================================================
% PREAMBLE
%===================================================================

	\documentclass{myArticleClass}

	\title{Generic Test Document}
	\author{Austin Pursley}

%===================================================================
% MAIN DOCUMENT
%===================================================================
 
	\begin{document}
	\maketitle
	\pagenumbering{roman}	
	%====================================
	% Table of Changes
	\clearpage
	\import{Sections/}{00a_Introduction}

	%====================================
	% Tables of Contents, Tables, Figures...
	\clearpage
	\tableofcontents
    \newpage
    \begin{center}
    \lhead{}
    \listoftables
    \newpage
    \listoffigures
    \end{center}
    \clearpage
	
	\pagenumbering{arabic}
	\glsresetall % Resets the acronym markers from preamble

	{% for s in sections -%}
	{%- set fn = "{" ~ s.filename ~ "}" -%}
	%====================================
	% {{ s.title }}
	\clearpage
	\import{Sections/}{{ fn }}

	{% endfor -%}

	%====================================
	% References
	\clearpage
	\printbibliography[heading=bibnumbered,title={References}]
    
%===================================================================
% APPENDICES
%===================================================================

	\clearpage
	\renewcommand{\appendixpagename}{\center{\Large{Appendices}}}
	\appendix
	\begin{appendices}
	\glsresetall % Resets the acronym markers from main document

	{% for a in appendices -%}
	{%- set fn = "{" ~ a.filename ~ "}" -%}
	%====================================
	% {{ a.title }}
	\clearpage
	\import{Appendices/}{{ fn }}

	{% endfor -%}

	%====================================
	% Glossaries
	\clearpage
	\printglossary[type=main,style=list]
	\printglossary[type=abbreviations, title={Acronyms}]
	\end{appendices}

	\end{document}