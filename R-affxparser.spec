%define		packname	affxparser

Summary:	Affymetrix File Parsing SDK
Name:		R-%{packname}
Version:	1.34.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	dbcd64c4d496799d932af88b54eb3881
URL:		http://bioconductor.org/packages/release/bioc/html/affxparser.html
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package for parsing Affymetrix files (CDF, CEL, CHP, BPMAP, BAR).
It provides methods for fast and memory efficient parsing of
Affymetrix files using the Affymetrix' Fusion SDK. Both ASCII- and
binary-based files are supported. Currently, there are methods for
reading chip definition file (CDF) and a cell intensity file (CEL).
These files can be read either in full or in part. For example,
probe signals from a few probesets can be extracted very quickly
from a set of CEL files into a convenient list structure.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/extras
%{_libdir}/R/library/%{packname}/info
%{_libdir}/R/library/%{packname}/testscripts

