%define		_plugin	virtusertable
Summary:	To logg in with your email address as in virtusertable
Summary(pl):	Logowanie z u¿yciem pe³nego adresu mailowego, jak w virtusertable
Name:		squirrelmail-plugin-%{_plugin}
Version:	0.3
Release:	3
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}.tar.gz
# Source0-md5:	8b33deac026f6e4c099aa918da71f8aa
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	/home/services/httpd/html/squirrel/plugins/%{_plugin}

%description
For those who use sendmail's virtusertable, users will be able to log
in using their full mail address instead of their user name.

%description -l pl
Dla tych którzy u¿ywaj± sendmailowego virtusertable - u¿ytkownicy bêd±
mogli siê logowaæ przy u¿yciu pe³nego adresu mailowego zamiast samej
nazwy u¿ytkownika.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install *.php $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_plugindir}
%{_plugindir}/*.php
