%define oname CDDB
%define pyversion 2.4
%define pysystemver 2.4

Summary: Python CDDB module
Name: python-%{oname}
Version: 1.4
Release: 16
Source0: %{oname}-%version.tar.bz2
License: GPL
Group: Development/Python
URL: http://cddb-py.sourceforge.net
BuildRequires: python2-devel
Requires: python2

%description
The dynamic duo of CDDB.py and DiscID.py, along with their side-kick C
module cdrommodule.so, provide an easy way for Python programs to
fetch information on audio CDs from CDDB (http://www.cddb.com/) -- a
very large online database of track listings and other information on
audio CDs.  UNIX platforms and Windows are both supported.


%prep
%setup -q -n %oname-%version

%build
python2 setup.py build

%install
python2 setup.py install --root %buildroot

%files
%doc CHANGES COPYING README
%py2_platsitedir/*




%changelog
* Thu Nov 17 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-13mdv2012.0
+ Revision: 731480
- rebuild

* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.4-12mdv2011.0
+ Revision: 598143
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4-11mdv2011.0
+ Revision: 442054
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 1.4-10mdv2009.1
+ Revision: 319198
- rebuild for python 2.6

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.4-9mdv2009.0
+ Revision: 259524
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4-8mdv2009.0
+ Revision: 247392
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.4-6mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 31 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.4-6mdv2007.0
+ Revision: 115731
- Rebuild against new python
- Import python-CDDB

* Fri Jul 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-1mdv2007.0
- Rebuild

* Wed Dec 07 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-4mdk
- Rebuild
- use mkrel

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.4-3mdk
- Rebuild for new python

* Sat Oct 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.4-2mdk
- rebuild

