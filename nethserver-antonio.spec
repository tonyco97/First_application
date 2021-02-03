Summary: First Antonio applications.
Name: nethserver-antonio
Version: 1.0
Release: 1%{?dist}
License: GPLv3
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-cockpit.tar.gz
BuildArch: noarch

Requires: nethserver-base
Requires: clamd
Requires: clamav-unofficial-sigs
Obsoletes: clamav-data

BuildRequires: nethserver-devtools


%description
First Antonio applications.

%prep
%setup

%build
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
tar xvf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

%{genfilelist} %{buildroot} \
    --file /etc/sudoers.d/50_nsapi_nethserver_antivirus 'attr(0440,root,root)' \
 > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

