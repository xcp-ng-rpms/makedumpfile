%global package_speccommit b5912f6f0ad888f8744d8797cb9d6125d2b71793
%global usver 1.5.8
%global xsver 4
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit Released-1-5-8

Name:        makedumpfile
Version:     1.5.8
Release:     %{?xsrel}%{?dist}
Summary:     Helper for making coredump files smaller

Group:       System Environment/Base
License:     GPLv2
URL:         http://makedumpfile.sourceforge.net/
Source0: makedumpfile-1.5.8.tar.gz
Patch0: 0001-PATCH-1-2-Enable-compressed-dump-formats-for-Xen.patch
Patch1: 0002-PATCH-2-2-Remove-notes-about-ELF-being-the-only-avai.patch

Buildrequires:    gcc
BuildRequires:    elfutils-devel, zlib-devel, bzip2-devel, xz-devel
%{?_cov_buildrequires}
Requires:    elfutils, zlib

%description
makedumpfile package.

%prep
%autosetup -p1
%{?_cov_prepare}

%build
%{?_cov_wrap} make LINKTYPE=dynamic

%install
mkdir -p -m755 $RPM_BUILD_ROOT/sbin
mkdir -p -m755 $RPM_BUILD_ROOT/%{_mandir}/man8/m
install -m 755 makedumpfile $RPM_BUILD_ROOT/sbin/makedumpfile
install -m 644 makedumpfile.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/makedumpfile.8.gz
%{?_cov_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/sbin/%{name}
%{_mandir}/man8/%{name}.8.gz

%{?_cov_results_package}

%changelog
* Tue Nov 02 2021 Igor Druzhinin <igor.druzhinin@citrix.com> - 1.5.8-4
- CP-38201: Enable static analysis with Coverity
- Convert from a tarball to XSU mirror

* Thu Aug 13 2015 Malcolm Crossley <malcolm.crossley@citrix.com> - 1.5.8-1.xs2
- Initial spec file for xenserver
