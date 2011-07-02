Summary: Simple FastCGI wrapper for CGI scripts
Name: fcgiwrap
Version: 1.0.3
Release: 0%{?dist}
License: None
Group: System Environment/Daemons
URL: http://nginx.localdomain.pl/
Source: fcgiwrap-%{version}.tar.gz
Packager: Michael Cutler <m@cotdp.com>
BuildRequires: /usr/bin/make
BuildRequires: gcc, gcc-c++, fcgi-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: fcgi


%description
fcgiwrap is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other web servers
that may need it). 


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.rst
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*


%changelog
* Wed Feb 09 2011 Michael Cutler <cotdp@github>
- See https://github.com/cotdp/fcgiwrap

