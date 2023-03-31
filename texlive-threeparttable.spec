Name:		texlive-threeparttable
Version:	17383
Release:	2
Summary:	Tables with captions and notes all the same width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/threeparttable
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a scheme for tables that have a structured note
section, after the caption. This scheme provides an answer to
the old problem of putting footnotes in tables -- by making
footnotes entirely unnecessary. Note that a threeparttable is
not a float of itself; but you can place it in a table or a
table* environment, if necessary.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/threeparttable/3parttable.sty
%{_texmfdistdir}/tex/latex/threeparttable/threeparttable.sty
%doc %{_texmfdistdir}/doc/latex/threeparttable/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/threeparttable/threeparttable.pdf
%doc %{_texmfdistdir}/doc/latex/threeparttable/threeparttable.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
