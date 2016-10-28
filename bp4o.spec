Name: bp4o
Version: 0.3.2
Release: 3%{?dist}
Summary: Better P4 Output
License: MIT
URL: http://zachwhaleys.website/bp4o/

Source0: https://github.com/zachwhaley/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
A bunch of scripts to catch p4 commands, run them, and make their output better.

%prep
%autosetup

%install
mkdir -p ${buildroot}%{_bindir} ${buildroot}%{_sysconfdir}/profile.d
install -p -m 755 bin/p4-* ${buildroot}%{_bindir}
install -p -m 444 bp4o.* ${buildroot}%{_sysconfdir}/profile.d

%files
%{_bindir}/p4-*
%{_sysconfdir}/profile.d/bp4o.*

%changelog
* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-3
- Revert "Replace mkdir with install" (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-2
- Replace mkdir with install (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-1
- new package built with tito

