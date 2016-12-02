Name: bp4o
Version: 1.0.0
Release: 1%{?dist}
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
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_functions.d
install -p -m 755 bin/p4-* %{buildroot}%{_bindir}
install -p -m 444 bp4o.bash %{buildroot}%{_sysconfdir}/profile.d/bp4o.sh
install -p -m 444 bp4o.zsh %{buildroot}%{_datadir}/zsh/site-functions/bp4o
install -p -m 444 bp4o.fish %{buildroot}%{_datadir}/fish/vendor_functions.d/p4.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/p4-*
%{_sysconfdir}/profile.d/bp4o.sh
%{_datadir}/zsh/site-functions/bp4o
%{_datadir}/fish/vendor_functions.d/p4.fish

%changelog
* Fri Dec 02 2016 Zach Whaley <zachbwhaley@gmail.com> 1.0.0-1
- Version 1.0.0 (zachbwhaley@gmail.com)

* Tue Nov 29 2016 Zach Whaley <zachbwhaley@gmail.com> 0.4.1-1
- Fix "bad pattern" errors for Zsh 5.0 (zachbwhaley@gmail.com)

* Tue Nov 22 2016 Zach Whaley <zachbwhaley@gmail.com> 0.4.0-1
- Add BP4O help text to 'p4 help' command (zachbwhaley@gmail.com)
- Add support for Fish shell (zachbwhaley@gmail.com)

* Mon Nov 21 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.3-2
- Install bp4o.zsh to zsh fpath (zachbwhaley@gmail.com)

* Fri Oct 28 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.3-1
- Avoid finding duplicate aliases with similar names (zachbwhaley@gmail.com)
- Set P4VERSION to the actual version of the p4 client (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-5
- Remove tito in favor of manual uploads (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-4
- Fix install of files (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-3
- Revert "Replace mkdir with install" (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-2
- Replace mkdir with install (zachbwhaley@gmail.com)

* Thu Oct 27 2016 Zach Whaley <zachbwhaley@gmail.com> 0.3.2-1
- new package built with tito

