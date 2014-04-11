Summary:	Lightweight suffix-sorting library
Summary(pl.UTF-8):	Lekka biblioteka do sortowania sufiksowego
Name:		libdivsufsort
Version:	2.0.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://code.google.com/p/libdivsufsort/downloads/list
Source0:	https://libdivsufsort.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	bc4c5638dd07cd8a02b15034c0f098fb
URL:		https://code.google.com/p/libdivsufsort/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libdivsufsort project provides a fast, lightweight, and robust C
API library to construct the suffix array and the Burrows-Wheeler
transformed string for any input string of a constant-size alphabet.

%description -l pl.UTF-8
Projekt libdivsufsort dostarcza szybką, lekką i pełną bibliotekę API
C do tworzenia tablic sufiksowych oraz łańcuchów z przekształcenia
Burrowsa-Wheelera dla dowolnego łańcucha składającego się z alfabetu
stałego rozmiaru.

%package devel
Summary:	Header files for libdivsufsort library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdivsufsort
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdivsufsort library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdivsufsort.

%package static
Summary:	Static libdivsufsort library
Summary(pl.UTF-8):	Statyczna biblioteka libdivsufsort
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdivsufsort library.

%description static -l pl.UTF-8
Statyczna biblioteka libdivsufsort.

%prep
%setup -q

%build
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdivsufsort.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libdivsufsort.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdivsufsort.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdivsufsort.so
%{_includedir}/divsufsort.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdivsufsort.a
