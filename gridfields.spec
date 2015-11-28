Summary:	GridFields - convenient, algebraic manipulation of unstructured grids
Summary(pl.UTF-8):	GridFields - wygodne operacje algebraiczne na tablicach bez struktury
Name:		gridfields
%define	snap	20140423
Version:	1.0.3
Release:	0.%{snap}.2
# project page says "MIT", but included spec and COPYING say LGPL v2+
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://code.google.com/p/gridfields/downloads/list
Source0:	https://gridfields.googlecode.com/files/tag.tgz
# Source0-md5:	05e1aeb82fac693e57ed9e16c6a09556
# released source is too old, so:
# svn checkout http://gridfields.googlecode.com/svn/trunk/ gridfields
# diff -Nur -x .svn tag/gridfieldsclib-0.7 gridfields/clib
Patch0:		%{name}-clib-svn.patch
# diff -Nur -x .svn tag/pygridfields-0.7 gridfields/pygridfields
Patch1:		%{name}-py-svn.patch
Patch2:		%{name}-python.patch
URL:		https://code.google.com/p/gridfields/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	netcdf-devel >= 4
BuildRequires:	netcdf-cxx-devel >= 4
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig-python >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GridFields library provides convenient, algebraic manipulation of
unstructured grids in C++ and Python.

%description -l pl.UTF-8
Biblioteka GridFields udostępnia wygodne operacje algebraiczne na
tablicach bez struktury z poziomu C++ i Pythona.

%package devel
Summary:	Header files for GridFields library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GridFields
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	netcdf-devel >= 4
Requires:	netcdf-cxx-devel >= 4

%description devel
Header files for GridFields library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GridFields.

%package static
Summary:	Static GridFields library
Summary(pl.UTF-8):	Statyczna biblioteka GridFields
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GridFields library.

%description static -l pl.UTF-8
Statyczna biblioteka GridFields.

%package -n python-gridfield
Summary:	Python GridField library
Summary(pl.UTF-8):	Biblioteka GridField dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-gridfield
GridFields library provides convenient, algebraic manipulation of
unstructured grids in C++ and Python.

This package contains Python library.

%description -n python-gridfield -l pl.UTF-8
Biblioteka GridFields udostępnia wygodne operacje algebraiczne na
tablicach bez struktury z poziomu C++ i Pythona.

Ten pakiet zawiera bibliotekę dla Pythona.

%prep
%setup -q -c
cd tag
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd tag/gridfieldsclib-0.7
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-netcdf-include=/usr/include \
	--with-netcdf-libdir=%{_libdir}
%{__make}

cd ../pygridfields-0.7
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C tag/gridfieldsclib-0.7 install \
	DESTDIR=$RPM_BUILD_ROOT

cd tag/pygridfields-0.7
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc tag/gridfieldsclib-0.7/README
%attr(755,root,root) %{_libdir}/libgridfields.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgridfields.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gridfields-config
%attr(755,root,root) %{_libdir}/libgridfields.so
%{_libdir}/libgridfields.la
%{_includedir}/gridfields

%files static
%defattr(644,root,root,755)
%{_libdir}/libgridfields.a

%files -n python-gridfield
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_core.so
%attr(755,root,root) %{py_sitedir}/elio.so
%{py_sitedir}/gridfield
%{py_sitedir}/gridfield-0.5-py*.egg-info
