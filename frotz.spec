Summary:	Interpreter for old Infocom text games
Summary(pl):	Interpreter dla starych tekstówek Infocomu
Name:		frotz
Version:	2.43
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/infocom/interpreters/frotz/%{name}-%{version}.tar.gz
# Source0-md5:	efe51879e012b92bb8d5f4a82e982677
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-config.patch
URL:		http://www.ifarchive.org/
BuildRequires:	ncurses-devel
Requires:	ncurses
Provides:	zcode-interpreter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interpreter for old Infocom text games, so called Interactive Fiction
Adventure.

%description -l pl
Interpreter dla starych tekstówek Infocomu, zwanych tak¿e Interactive
Fiction Adventure.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/frotz.conf-big $RPM_BUILD_ROOT%{_sysconfdir}/frotz.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog HOW_TO_PLAY README README.1st SPEECH TODO
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/frotz.conf
%attr(755,root,root) %{_bindir}/frotz
%{_mandir}/man6/*
