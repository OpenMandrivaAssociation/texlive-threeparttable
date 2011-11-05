# revision 17383
# category Package
# catalog-ctan /macros/latex/contrib/threeparttable
# catalog-date 2010-03-09 13:13:30 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-threeparttable
Version:	20100309
Release:	1
Summary:	Tables with captions and notes all the same width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/threeparttable
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttable.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttable.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides a scheme for tables that have a structured note
section, after the caption. This scheme provides an answer to
the old problem of putting footnotes in tables -- by making
footnotes entirely unnecessary. Note that a threeparttable is
not a float of itself; but you can place it in a table or a
table* environment, if necessary.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/threeparttable/3parttable.sty
%{_texmfdistdir}/tex/latex/threeparttable/threeparttable.sty
%doc %{_texmfdistdir}/doc/latex/threeparttable/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/threeparttable/threeparttable.pdf
%doc %{_texmfdistdir}/doc/latex/threeparttable/threeparttable.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
