Summary:	A thing for ignoring files based on globs
Name:		nodejs-fstream-ignore
Version:	1.0.0
Release:	1
License:	ISC
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-%{version}.tgz
# Source0-md5:	3d59f1c3c501aaa5d9ec283fd6a2fd0d
URL:		https://github.com/isaacs/fstream-ignore
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-fstream
Requires:	nodejs-inherits < 3
Requires:	nodejs-inherits >= 2
Requires:	nodejs-minimatch < 2
Requires:	nodejs-minimatch >= 1.0.0
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
