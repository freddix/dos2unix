Summary:	Text file format converter
Name:		dos2unix
Version:	7.2
Release:	1
License:	BSD
Group:		Applications/Text
Source0:	http://www.xs4all.nl/~waterlan/dos2unix/%{name}-%{version}.tar.gz
# Source0-md5:	40e853c291880d70b229eb41a2bd98b3
URL:		http://www.xs4all.nl/~waterlan/dos2unix.html
BuildRequires:	gettext-devel
Provides:	unix2dos
Obsoletes:	unix2dos
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in DOS/MAC format to UNIX
format.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dos2unix and unix2dos domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS.txt COPYING.txt ChangeLog.txt NEWS.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/dos2unix
%attr(755,root,root) %{_bindir}/mac2unix
%attr(755,root,root) %{_bindir}/unix2dos
%attr(755,root,root) %{_bindir}/unix2mac
%{_mandir}/man1/dos2unix.1*
%{_mandir}/man1/mac2unix.1*
%{_mandir}/man1/unix2dos.1*
%{_mandir}/man1/unix2mac.1*
%lang(nl) %{_mandir}/nl/man1/dos2unix.1*
%lang(nl) %{_mandir}/nl/man1/mac2unix.1*
%lang(nl) %{_mandir}/nl/man1/unix2dos.1*
%lang(nl) %{_mandir}/nl/man1/unix2mac.1*

