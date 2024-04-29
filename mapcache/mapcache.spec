Name:           mapcache
Version:        1.14.0        
Release:        1%{?dist}
Summary:        Caching server for WMS layers
Group:          Development/Tools
License:        MIT
URL:            http://mapserver.org/trunk/en/mapcache/
Source:         mapcache-%{version}.tar.gz
#Obtain source using git archive available at https://github.com/mapserver/mapcache:
#git archive --format=tar --prefix=mapcache-1.1dev/ master | gzip > mapcache-1.1dev.tar.gz
#or adjust archive available at: https://github.com/mapserver/mapcache/archive/master.tar.gz
Requires:       webserver, apr-util

BuildRequires:  httpd-devel cmake libcurl-devel
BuildRequires:  geos311-devel proj90-devel gdal35-devel libjpeg-turbo-devel
BuildRequires:  libpng-devel libtiff-devel pixman-devel sqlite-devel


%description
MapCache is a server that implements tile caching to speed up access to WMS layers. 
The primary objectives are to be fast and easily deployable, while offering the 
essential features (and more!) expected from a tile caching solution.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_LIBDIR=lib64 -DCMAKE_PREFIX_PATH="/usr/gdal35;/usr/geos311;/usr/proj90;" -DWITH_FCGI=0 .
#make %{?_smp_mflags}
%cmake_build

%install
rm -rf %{buildroot}
#make DESTDIR=%{buildroot} \
#    install
%cmake_install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL* README* LICENSE* 
%{_bindir}/*
%{_libdir}/*

%changelog
