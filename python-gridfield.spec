%define	rel	1
%define	snap	20151203
%define	gitref	3b3fad08c21d883984a97c1d03a5c91ad37c27f8
Summary:	Python GridField library
Summary(pl.UTF-8):	Biblioteka GridField dla Pythona
Name:		python-gridfield
Version:	1.0.3
Release:	0.%{snap}.%{rel}
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://code.google.com/p/gridfields/downloads/list
Source0:	https://github.com/OPENDAP/gridfields/archive/%{gitref}/gridfields-%{snap}.tar.gz
# Source0-md5:	abade68d7e7b13210f2885cc266e9608
Patch0:		gridfields-python.patch
URL:		https://github.com/OPENDAP/gridfields
BuildRequires:	libstdc++-devel
BuildRequires:	netcdf-cxx-devel >= 4
BuildRequires:	netcdf-devel >= 4
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GridFields library provides convenient, algebraic manipulation of
unstructured grids in C++ and Python.

This package contains Python library.

%description -l pl.UTF-8
Biblioteka GridFields udostępnia wygodne operacje algebraiczne na
tablicach bez struktury z poziomu C++ i Pythona.

Ten pakiet zawiera bibliotekę dla Pythona.

%prep
%setup -q -n gridfields-%{gitref}
cd pygridfields
%patch -P0 -p2

%build
cd pygridfields
%py_build

%install
rm -rf $RPM_BUILD_ROOT

cd pygridfields
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pygridfields/README
%attr(755,root,root) %{py_sitedir}/_core.so
%attr(755,root,root) %{py_sitedir}/elio.so
%{py_sitedir}/gridfield
%{py_sitedir}/gridfield-0.5-py*.egg-info
