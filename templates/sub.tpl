{%- set title = "{" ~ title ~ "}" -%}
{%- set label = "{" ~ label ~ "}" -%}
\documentclass[class=myArticleClass, float=false, crop=false]{standalone}

%=====================================================================
%  {{ title }}
%=====================================================================
\begin{document}
\section{{ title }}
\label{{ label }}

\end{document}