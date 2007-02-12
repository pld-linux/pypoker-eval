Summary:	Python adaptor for poker-eval
Summary(pl.UTF-8):   Pythonowy adapter dla poker-eval
Name:		pypoker-eval
Version:	126.0
Release:	0.1
License:	GPL
Group:		Libraries/Python
#orig. 125.0:	http://dl.sourceforge.net/pokersource/%{name}-%{version}.tar.gz
Source0:	http://download.gna.org/underware/dists/%{name}-%{version}.tar.gz
# Source0-md5:	33f482c627c48c63c711a2b1b2308a5e
URL:		http://pokersource.sourceforge.net/
BuildRequires:	poker-eval-devel
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is python adaptor for the poker-eval toolkit for writing
programs which simulate or analyze poker games. The python interface
is somewhat simpler than the C API of poker-eval. It assumes that the
caller is willing to have a higher level API and is not interested in
a one to one mapping of the poker-eval API.

%description -l pl.UTF-8
Ten pakiet to pythonowy adapter dla narzędzia poker-eval do pisania
programów symulujących lub analizujących grę w pokera. Interfejs w
Pythonie jest w pewnym sensie łatwiejszy niż API w C. Zakłada, że
użytkownik potrzebuje wysokopoziomowego API i nie interesuje go
mapowanie całego API biblioteki poker-eval.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
# '*' because of missing -avoid-version
%attr(755,root,root) %{py_sitedir}/pypokereval.so*
%{py_sitedir}/pokereval.py[co]
