Name:		makedumpfile
Version:	1.5.8
Release:	2%{?dist}
Summary:	Helper for making coredump files smaller

Group:		System Environment/Base
License:	GPLv2
URL:		http://makedumpfile.sourceforge.net/
#Source0:    http://heanet.dl.sourceforge.net/sourceforge/makedumpfile/%{name}-%{version}.tar.gz

Source0: https://repo.citrite.net/xs-local-contrib/makedumpfile/makedumpfile-1.5.8.tar.gz
Patch0: SOURCES/makedumpfile/0001-PATCH-1-2-Enable-compressed-dump-formats-for-Xen.patch
Patch1: SOURCES/makedumpfile/0002-PATCH-2-2-Remove-notes-about-ELF-being-the-only-avai.patch


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/makedumpfile/archive?at=1.0.0&format=tar#/makedumpfile.patches.tar) = 7a645363d64d4df52e35132c47af3a0a5953e102


BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Buildrequires:  gcc
BuildRequires:	elfutils-devel, zlib-devel, bzip2-devel, xz-devel
Requires:	elfutils, zlib

%description
makedumpfile package.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
rm -rf %{buildroot}
make LINKTYPE=dynamic

%install
mkdir -p -m755 $RPM_BUILD_ROOT/sbin
mkdir -p -m755 $RPM_BUILD_ROOT/%{_mandir}/man8/m
install -m 755 makedumpfile $RPM_BUILD_ROOT/sbin/makedumpfile
install -m 644 makedumpfile.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/makedumpfile.8.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/sbin/%{name}
%{_mandir}/man8/%{name}.8.gz


%changelog
* Thu Aug 13 2015 Malcolm Crossley <malcolm.crossley@citrix.com> - 1.5.8-1.xs2
- Initial spec file for xenserver
