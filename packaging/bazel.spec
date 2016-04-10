Name:           PKG_NAME
Version:        PKG_VERSION
Release:        PKG_RELEASE%{?dist}
Summary:        Correct, reproducible, and fast builds for everyone.
License:        Apache License 2.0
URL:            http://bazel.io/
Source0:        PKG_NAME-PKG_VERSION.tar.gz

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  zlib-devel
Requires:       java-1.8.0-openjdk-devel

%define debug_package %{nil}
%define __os_install_post %{nil}

%description
Correct, reproducible, and fast builds for everyone.

%prep
%setup -q

%build

./compile.sh

%check

%install

mkdir -p %{buildroot}/%{_bindir}
cp output/bazel %{buildroot}/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/bazel

%changelog
