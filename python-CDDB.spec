%define oname CDDB
%define version 1.4
%define pyversion 2.4
%define pysystemver 2.4
%define release %mkrel 12

Summary: Python CDDB module
Name: python-%{oname}
Version: %{version}
Release: %{release}
Source0: %{oname}-%version.tar.bz2
License: GPL
Group: Development/Python
URL: http://cddb-py.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libpython-devel >= %pyversion
Requires: python

%description
The dynamic duo of CDDB.py and DiscID.py, along with their side-kick C
module cdrommodule.so, provide an easy way for Python programs to
fetch information on audio CDs from CDDB (http://www.cddb.com/) -- a
very large online database of track listings and other information on
audio CDs.  UNIX platforms and Windows are both supported.


%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root %buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES COPYING README
%py_platsitedir/*


