#
# spec file for package lcms (Version 1.19)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           libijs
License:        MIT
Group:          System/Libraries
Summary:        IJS raster image transport protocol library
Version:        0.35_12
Release:        1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz
Source1001: 	libijs.manifest

%description
 IJS raster image transport protocol: shared library
 IJS is, first and foremost, a protocol for transmission of raster page
 images. This snapshot provides a reference implementation of the protocol,
 the design of which is still in flux. When the protocol specification is
 published, it will be authoritative. Applications should feel free to link
 against the library provided in this package, adapt that code for their own
 needs, or roll a completely new implementation.
 .
 IJS is a client-server protocol, used to write ghostscript drivers. The
 drivers are separate programs. The client and server communicate via pipes,
 though shared memory may be used additionally in the future. Currently IJS
 is used by the hpijs and ijsgimpprint drivers.
 .
 Code for both the client- and server-side is included in the library. This
 package provides the shared library.

%package devel
Summary:        Include Files and Libraries Mandatory for Development
Requires:       libijs
Group:          Development/Libraries

%description devel
 IJS raster image transport protocol: development files
 IJS (InkJet Server) is, first and foremost, a protocol for transmission of
 raster page images. This snapshot provides a reference implementation of
 the protocol, the design of which is still in flux. When the protocol
 specification is published, it will be authoritative. Applications should
 feel free to link against the library provided in this package, adapt that
 code for their own needs, or roll a completely new implementation.
 .
 IJS is a client-server protocol, used to write ghostscript drivers. The
 drivers are separate programs. The client and server communicate via pipes,
 though shared memory may be used additionally in the future. Currently IJS
 is used by the hpijs and ijsgimpprint drivers.
 .
 Code for both the client- and server-side is included in the library. This
 package provides a static library, development headers and documentation.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS="$RPM_OPT_FLAGS"    
export CXXFLAGS="$RPM_OPT_FLAGS"    

%reconfigure --enable-shared

make  %{?_smp_flags} CFLAGS="$CFLAGS"

%install
%make_install


mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/debian/copyright %{buildroot}/usr/share/license/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%manifest %{name}.manifest
/usr/share/license/%{name}
%{_libdir}/libijs-0.35.so
%exclude %{_mandir}/man1/ijs-config.1.gz
%exclude %{_bindir}/ijs-config
%exclude %{_bindir}/ijs_client_example
%exclude %{_bindir}/ijs_server_example

%files devel
%manifest %{name}.manifest
%{_includedir}/ijs/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/ijs.pc

%changelog
