Summary:	Interpreter for old Infocom text games
Summary(pl):	Interpreter dla starych tekstówek Infocomu
Name:		frotz
Version:	2.43
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	efe51879e012b92bb8d5f4a82e982677
Source1:	%{name}-wrapper
Patch0:		%{name}-makefilefix.patch
Patch1:		%{name}-configfix.patch
URL:		http://www.ifarchive.com/
BuildRequires:	ncurses-devel
Requires:	ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interpreter for old Infocom text games, so called Interactive Fiction
Adventure.

%description -l pl
Interpreter dla starych tekstówek Infocomu, zwanych takze Interactive
Fiction Adventure.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -d $RPM_BUILD_ROOT%{_datadir}/games/zcode
install frotz $RPM_BUILD_ROOT%{_bindir}
install doc/frotz.6 $RPM_BUILD_ROOT%{_mandir}/man6/
install doc/frotz.conf-big $RPM_BUILD_ROOT%{_sysconfdir}/frotz.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/games/zcode/wrapper.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog HOW_TO_PLAY README README.1st SPEECH TODO
%attr(755,root,root) %{_bindir}/frotz
%{_mandir}/man6/*
%dir %{_datadir}/games/zcode
%attr(755,root,root) %{_datadir}/games/zcode/wrapper.sh
%{_sysconfdir}/frotz.conf
