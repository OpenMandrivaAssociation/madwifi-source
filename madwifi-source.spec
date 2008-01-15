%define name madwifi-source
%define short_name madwifi
%define version 0.9.3
%define release %mkrel 3

Summary: Madwifi drivers source code
Name: %{name}
Version: %{version}
Release: %{release}
# http://prdownloads.sourceforge.net/madwifi/madwifi-%{madwifi_version}.tar.bz2
# tar cjf madwifi-source-0.9.2.tar.bz2 madwifi-0.9.2/net80211/ madwifi-0.9.2/include
Source0: %{name}-%{version}.tar.bz2
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
%setup -q -n %{short_name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/%{short_name}
cp -a net80211 include $RPM_BUILD_ROOT/usr/src/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/src/%{short_name}
/usr/src/%{short_name}/*
