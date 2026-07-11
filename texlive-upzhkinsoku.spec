%global tl_name upzhkinsoku
%global tl_revision 47354

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Supplementary Chinese kinsoku for Unicode *pTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/upzhkinsoku
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upzhkinsoku.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upzhkinsoku.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides supplementary Chinese kinsoku (line breaking rules
etc.) settings for Unicode (e-)upTeX (when using Unicode as its internal
encoding), and ApTeX. Both LaTeX and plain TeX are supported.

