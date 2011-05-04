%define name madwifi-source
%define short_name madwifi

%define version 0.9.3.3
%define snaprev r3114
%define snapdate 20080104
%define rel 11
%if %{snapdate}
%define distname madwifi-ng-%{snaprev}-%{snapdate}
%define release %mkrel %{rel}.%{snaprev}
%else
%define distname %{short_name}-%{version}
%define release %mkrel %{rel}
%endif

Summary: Madwifi drivers source code
Name: %{name}
Version: %{version}
Release: %{release}
# to run in BUILD tree of madwifi package:
# tar cjf madwifi-r3114-20080104-source.tar.bz2 madwifi-ng-r3114-20080104/net80211/*.h madwifi-ng-r3114-20080104/include/*.h
Source0: %{distname}-source.tar.bz2
License: GPL
Group: Development/Kernel
Url: http://madwifi.org/
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
This package contains parts of the madwifi drivers source code.

The whole source code cannot be distributed in the distribution
because it contains non-free binary code in the HAL.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/src/%{short_name}
cp -a net80211 include %{buildroot}/usr/src/%{short_name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /usr/src/%{short_name}
/usr/src/%{short_name}/*
