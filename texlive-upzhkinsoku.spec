Name:		texlive-upzhkinsoku
Version:	47354
Release:	1
Summary:	Supplementary Chinese kinsoku for Unicode *pTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/upzhkinsoku
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upzhkinsoku.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upzhkinsoku.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides supplementary Chinese kinsoku (line
breaking rules etc.) settings for Unicode (e-)upTeX (when using
Unicode as its internal encoding), and ApTeX. Both LaTeX and
plain TeX are supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/upzhkinsoku
%doc %{_texmfdistdir}/doc/generic/upzhkinsoku

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
