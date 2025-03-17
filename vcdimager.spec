#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	VideoCD (pre-)mastering and ripping tools
Summary(pl.UTF-8):	Narzędzia do tworzenia i odczytu VideoCD
Name:		vcdimager
Version:	2.0.1
Release:	3
License:	GPL v2+
Group:		Applications/File
Source0:	http://ftp.gnu.org/gnu/vcdimager/%{name}-%{version}.tar.gz
# Source0-md5:	3890d73da62d0607c87962c41cd33a29
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/vcdimager/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6.0
BuildRequires:	help2man
BuildRequires:	libcdio-devel >= 2.0.0
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-devel >= 1:2.6.11
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.7
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
Requires:	libcdio >= 2.0.0
Requires:	libxml2 >= 1:2.6.11
Requires:	popt >= 1.7
Obsoletes:	vcdimager-cdio < 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files. VCDRip, which comes with VCDImager, does the
reverse operation. That is, ripping mpeg streams from images (and
already burned VideoCDs) and showing some information about the
VideoCD.

%description -l pl.UTF-8
VCDImager służy do tworzenia obrazów VideoCD BIN/CUE z plików mpeg,
które następnie mogą być wypalone za pomocą cdrdao lub innego programu
zdolnego do wypalania plików BIN/CUE. VCDRip dostarczany wraz z
VCDImager pozwala na wykonanie odwrotnej operacji tzn. zrzucenia
strumienia mpeg z obrazów (oraz już wypalonych płyt VideoCD).

%package devel
Summary:	Header files for vcd libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek vcd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdio-devel >= 2.0.0
Obsoletes:	vcdimager-cdio-devel < 0.8

%description devel
Header files for vcd libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek vcd.

%package static
Summary:	Static vcd libraries
Summary(pl.UTF-8):	Statyczne biblioteki vcd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	vcdimager-cdio-static < 0.8

%description static
Static vcd libraries.

%description static -l pl.UTF-8
Statyczne biblioteki vcd.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvcdinfo.la

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
%attr(755,root,root) %{_bindir}/cdxa2mpeg
%attr(755,root,root) %{_bindir}/vcd-info
%attr(755,root,root) %{_bindir}/vcdimager
%attr(755,root,root) %{_bindir}/vcdxbuild
%attr(755,root,root) %{_bindir}/vcdxgen
%attr(755,root,root) %{_bindir}/vcdxminfo
%attr(755,root,root) %{_bindir}/vcdxrip
%attr(755,root,root) %{_libdir}/libvcdinfo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvcdinfo.so.0
%{_mandir}/man1/cdxa2mpeg.1*
%{_mandir}/man1/vcd-info.1*
%{_mandir}/man1/vcdimager.1*
%{_mandir}/man1/vcdxbuild.1*
%{_mandir}/man1/vcdxgen.1*
%{_mandir}/man1/vcdxminfo.1*
%{_mandir}/man1/vcdxrip.1*
%{_infodir}/vcd-info.info*
%{_infodir}/vcdimager.info*
%{_infodir}/vcdxrip.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvcdinfo.so
%{_includedir}/libvcd
%{_pkgconfigdir}/libvcdinfo.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvcdinfo.a
%endif
