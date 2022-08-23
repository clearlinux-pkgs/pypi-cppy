#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cppy
Version  : 1.2.1
Release  : 12
URL      : https://files.pythonhosted.org/packages/c5/7e/6cc5acd93752ee52d2f0423046072a2ce3ae16dfcd44373b9fe2a0222204/cppy-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/7e/6cc5acd93752ee52d2f0423046072a2ce3ae16dfcd44373b9fe2a0222204/cppy-1.2.1.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cppy-license = %{version}-%{release}
Requires: pypi-cppy-python = %{version}-%{release}
Requires: pypi-cppy-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)

%description
Cppy
====
.. image:: https://github.com/nucleic/cppy/actions/workflows/ci.yml/badge.svg
:target: https://github.com/nucleic/cppy/actions/workflows/ci.yml

%package dev
Summary: dev components for the pypi-cppy package.
Group: Development
Provides: pypi-cppy-devel = %{version}-%{release}
Requires: pypi-cppy = %{version}-%{release}

%description dev
dev components for the pypi-cppy package.


%package license
Summary: license components for the pypi-cppy package.
Group: Default

%description license
license components for the pypi-cppy package.


%package python
Summary: python components for the pypi-cppy package.
Group: Default
Requires: pypi-cppy-python3 = %{version}-%{release}

%description python
python components for the pypi-cppy package.


%package python3
Summary: python3 components for the pypi-cppy package.
Group: Default
Requires: python3-core
Provides: pypi(cppy)

%description python3
python3 components for the pypi-cppy package.


%prep
%setup -q -n cppy-1.2.1
cd %{_builddir}/cppy-1.2.1
pushd ..
cp -a cppy-1.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656367770
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cppy
cp %{_builddir}/cppy-1.2.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cppy/aaeb6aef24b11a94de50d8e9b2d6d1728c25a0e4
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.10/site-packages/cppy/include/cppy/cppy.h
/usr/lib/python3.10/site-packages/cppy/include/cppy/defines.h
/usr/lib/python3.10/site-packages/cppy/include/cppy/errors.h
/usr/lib/python3.10/site-packages/cppy/include/cppy/ptr.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cppy/aaeb6aef24b11a94de50d8e9b2d6d1728c25a0e4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
