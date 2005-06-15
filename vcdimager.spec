%bcond_without	static	# don't build static library
Summary:	VideoCD (pre-)mastering and ripping tools
Summary(pl):	Narzêdzia do tworzenia i odczytu VideoCD
Name:		vcdimager
Version:	0.7.22
Release:	1
License:	GPL
Group:		Applications/File
#Source0:	http://www.vcdimager.org/pub/vcdimager/vcdimager-0.7/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.gnu.org/gnu/vcdimager/%{name}-%{version}.tar.gz
# Source0-md5:	d7ceca2631fb732ff1257c2d3a7df45d
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/vcdimager/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.0
BuildRequires:	libcdio-devel >= 0.72
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.7
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
Requires:	libcdio >= 0.72
Requires:	libxml2 >= 2.6.11
Requires:	popt >= 1.7
Obsoletes:	vcdimager-cdio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libvcd.so.0 libvcdinfo.so.0

%description
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files. VCDRip, which comes with VCDImager, does the
reverse operation. That is, ripping mpeg streams from images (and
already burned VideoCDs) and showing some information about the
VideoCD.

%description -l pl
VCDImager s³u¿y do tworzenia obrazów VideoCD BIN/CUE z plików mpeg,
które nastêpnie mog± byæ wypalone za pomoc± cdrdao lub innego programu
zdolnego do wypalania plików BIN/CUE. VCDRip dostarczany wraz z
VCDImager pozwala na wykonanie odwrotnej operacji tzn. zrzucenia
strumienia mpeg z obrazów (oraz ju¿ wypalonych p³yt VideoCD).

%package devel
Summary:	Header files for vcd libraries
Summary(pl):	Pliki nag³ówkowe bibliotek vcd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdio-devel >= 0.72
Obsoletes:	vcdimager-cdio-devel

%description devel
Header files for vcd libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek vcd.

%package static
Summary:	Static vcd libraries
Summary(pl):	Statyczne biblioteki vcd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	vcdimager-cdio-static

%description static
Static vcd libraries.

%description static -l pl
Statyczne biblioteki vcd.

%prep
%setup -q
%patch0 -p1

cp -f libpopt.m4 acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	%{!?with_static:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*.1*
%{_infodir}/*.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libvcd
%{_pkgconfigdir}/*.pc

%if %{with static}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
