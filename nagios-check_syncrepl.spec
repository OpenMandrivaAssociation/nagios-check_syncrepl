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
