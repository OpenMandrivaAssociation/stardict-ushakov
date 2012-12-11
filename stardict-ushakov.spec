%define dict_name	ushakov
%define version		2.4.2
%define release		1

Name: 			stardict-%dict_name
Version: 		2.4.2
Release: 		%mkrel %{release}
Summary: 		Russian Ushakov's Dictionary
License: 		GPLv2+
URL:			http://xdxf.revdanica.com/down/index.php
Group: 			Text tools
Source0: 		%dict_name.dict.dz
Source1: 		%dict_name.idx
Source2: 		%dict_name.ifo
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildArch: 		noarch
Requires: 		stardict

%description
Russian Ushakov's Dictionary in stardict format

%install
rm -rf %{buildroot}
install -p -m644 -D %SOURCE0 %{buildroot}%{_datadir}/stardict/dic/%dict_name.dict.dz
install -p -m644 -D %SOURCE1 %{buildroot}%{_datadir}/stardict/dic/%dict_name.idx
install -p -m644 -D %SOURCE2 %{buildroot}%{_datadir}/stardict/dic/%dict_name.ifo
 	
%clean
rm -rf %{buildroot}
%files
%{_datadir}/stardict/dic/%{dict_name}*


%changelog
* Sat Jul 23 2011 Yuri Myasoedov <omerta13@mandriva.org> 2.4.2-1mdv2012.0
+ Revision: 691228
- Initial package import

