Summary:	VideoCD (pre-)mastering and ripping tool
Summary(pl):	VideoCD generation tool
Name:		vcdimager
Version:	0.6.2
Release:	2
License:	GPL
Group:		Applications/File
URL:		http://www.gnu.org/software/vcdimager/
Source0:	http://www.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-m4.patch
Patch1:		%{name}-am_ac.patch
Patch2:		%{name}-info.patch
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	fix-info-dir
# required only for m4 macros
BuildRequires:	gnome-libs-devel
BuildRequires:	popt-devel
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
%patch1 -p1
%patch2 -p1

%build
rm missing
%{__libtoolize}
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9fn AUTHORS ChangeLog NEWS README TODO

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man?/*
