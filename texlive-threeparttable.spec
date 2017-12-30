# revision 17383
# category Package
# catalog-ctan /macros/latex/contrib/threeparttable
# catalog-date 2010-03-09 13:13:30 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-threeparttable
Version:	20170414
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100309-2
+ Revision: 756836
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100309-1
+ Revision: 719732
- texlive-threeparttable
- texlive-threeparttable
- texlive-threeparttable

