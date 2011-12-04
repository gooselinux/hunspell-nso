Name: hunspell-nso
Summary: Northern Sotho hunspell dictionaries
%define upstreamid 20060120
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://downloads.translate.org.za/spellchecker/northern_sotho/myspell-ns_ZA-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Northern Sotho hunspell dictionaries.

%prep
%setup -q -c -n hunspell-nso

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ns_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/nso_ZA.dic
cp -p ns_ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/nso_ZA.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ns_ZA.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20060120-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060120-1
- initial version
