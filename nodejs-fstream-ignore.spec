Summary:	A thing for ignoring files based on globs
Name:		nodejs-fstream-ignore
Version:	0.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/fstream-ignore
Source0:	http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-%{version}.tgz
# Source0-md5:	745df91e15f9a64a912c2cd670ca0584
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-fstream
Requires:	nodejs-inherits
Requires:	nodejs-minimatch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A thing for ignoring files based on globs.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/fstream-ignore
cp -pr ignore.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/fstream-ignore

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/fstream-ignore
%{_examplesdir}/%{name}-%{version}
