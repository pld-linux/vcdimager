Summary:	VideoCD (pre-)mastering and ripping tool
Summary(pl):	VideoCD generation tool
Name:		vcdimager
Version:	0.7.13
Release:	1
License:	GPL
Group:		Applications/File
URL:		http://www.gnu.org/software/vcdimager/
Source0:	http://www.vcdimager.org/pub/vcdimager/vcdimager-0.7_UNSTABLE/%{name}-%{version}.tar.gz
Patch0:		%{name}-m4.patch
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libxml2-devel >= 2.3.8
Requires: 	libxml2 >= 2.3.8
BuildRequires:	popt-devel
Requires:	popt
Requires:	fix-info-dir
# required only for m4 macros
##BuildRequires:	gnome-libs-devel
##BuildRequires:	popt-devel
BuildRequires:	texinfo
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files. VCDRip, which comes with VCDImager, does the
reverse operation. That is, ripping mpeg streams from images (and
already burned VideoCDs) and showing some information about the
VideoCD.

%description -l pl
VCDImager pozwala Ci na tworzenie obrazów VideoCD BIN/CUE z plików
mpeg, które nastêpnie mog± byæ wypalone za pomoc± cdrdao lub innego
programu zdolnego do wypalania plików BIN/CUE. VCDRip dostarczany wraz
z VCDImager pozwala na wykonanie odwrotnej operacji tzn. zrzucenia
strumienia mpeg z obrazów (oraz ju¿ wypalonych p³yt VideoCD).

%prep
%setup -q
%patch0 -p1



%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I ./
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man?/*
