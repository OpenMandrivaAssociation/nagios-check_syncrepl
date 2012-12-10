%define name	nagios-check_syncrepl
%define version	20080409
%define release	%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check the open ldap syncrepl
Group:		Networking/Other
License:	BSD
URL:		http://www.nagiosexchange.org/cgi-bin/page.cgi?g=Detailed%2F2477.html
Source0:	check_syncrepl.py
Patch0:     check_syncrepl.py-allow-openldap2.4-CSN-format.patch
Patch1:     check_syncrepl.py-fix-exit-status.patch
Patch2:     check_syncrepl.py-allow-ignore-higher-CSN.patch
Requires:   python-ldap
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Check the open ldap replication via SYNCREPL and python. 

%prep
%setup -c -T
cp %{SOURCE0} .
%patch0 -p 0
%patch1 -p 0
%patch2 -p 0

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 check_syncrepl.py %{buildroot}%{_datadir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_syncrepl.cfg <<'EOF'
define command{
	command_name	check_syncrepl
	command_line	%{_datadir}/nagios/plugins/check_syncrepl.py -q -n $ARG1$ $ARG2$ -b $ARG3$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_syncrepl.py
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_syncrepl.cfg


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 20080409-8mdv2011.0
+ Revision: 620466
- the mass rebuild of 2010.0 packages

* Thu May 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-7mdv2010.0
+ Revision: 380370
- patch: allow consumer CSN to be higher than provider

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-6mdv2009.1
+ Revision: 331023
- patch1: exit wit expected status when test fails

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-5mdv2009.1
+ Revision: 314640
- now a noarch plugin

* Thu Sep 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-4mdv2009.0
+ Revision: 288130
- fix openldap2.4 CSN format issue

* Thu Sep 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-3mdv2009.0
+ Revision: 287982
- configuration tuning

* Wed Sep 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-2mdv2009.0
+ Revision: 287965
- fix dependencies

* Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-1mdv2009.0
+ Revision: 283008
- import nagios-check_syncrepl


* Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080409-1mdv2009.0
- first release
