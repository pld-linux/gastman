# TODO:
# - desktop file (vfolder? how to make it?)
Summary:	Gtk ASTerisk MANager
Name:		gastman
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.asterisk.org/pub/telephony/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e62a7b4c4161d25c8b7b54fe875d5f5c
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.asterisk.org/
BuildRequires:	gtk+-devel >= 1.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gastmandir	/usr/share/gastman

%description
Gtk ASTerisk MANager.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SBINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_gastmandir}
%dir %{_gastmandir}/icons
%{_gastmandir}/icons/*.xpm
