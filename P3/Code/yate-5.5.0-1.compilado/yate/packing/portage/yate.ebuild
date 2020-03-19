# Ebuild script for Gentoo
# Package net-voip/yate

EAPI=1

inherit eutils

DESCRIPTION="YATE - Yet Another Telephony Engine"
SRC_URI="http://yate.null.ro/tarballs/yate5/yate-5.5.0-1.tar.gz"
HOMEPAGE="http://yate.null.ro/"
LICENSE="GPL-2"

KEYWORDS="~x86 ~amd64"
IUSE="doc gsm speex amrnb h323 ilbc mysql postgres ssl zlib qt4 spandsp sctp wanpipe zaptel"

DEPEND="
	media-sound/sox
	doc? ( || ( app-doc/doxygen >=dev-util/kdoc-2.0_alpha54 ) )
	gsm? ( media-sound/gsm )
	speex? ( media-libs/speex )
	amrnb? ( media-libs/amrnb )
	h323? ( >=net-libs/openh323-1.15.3 dev-libs/pwlib )
	mysql? ( dev-db/mysql )
	postgres? ( dev-db/postgresql-base )
	ssl? ( dev-libs/openssl )
	zlib? ( sys-libs/zlib )
	qt4? ( x11-libs/qt-core:4 x11-libs/qt-gui:4 )
	spandsp? ( media-libs/spandsp )
	sctp? ( net/sctp-tools )
	wanpipe? ( net-misc/wanpipe )
	zaptel? ( net-misc/zaptel )
"
RDEPEND="${DEPEND}"


src_compile()
{
	local configopts
	if use doc; then
		if has_version app-doc/doxygen; then
			configopts+=" --with-doxygen"
		fi
		if has_version dev-util/kdoc; then
			configopts+=" --with-kdoc"
		fi
	else
		configopts+=" --without-doxygen --without-kdoc"
	fi

	econf \
		$(use_enable ilbc) \
		$(use_enable sctp sctp) \
		$(use_with gsm libgsm) \
		$(use_with speex libspeex) \
		$(use_with amrnb amrnb /usr) \
		$(use_with h323 pwlib /usr) \
		$(use_with h323 openh323 /usr) \
		$(use_with mysql mysql /usr) \
		$(use_with postgres libpq /usr) \
		$(use_with ssl openssl) \
		$(use_with zlib zlib /usr) \
		$(use_with qt4 libqt4) \
		$(use_with spandsp) \
		${configopts} || die "Configuring failed"

	emake -j1 all || die "Building failed"
}

src_install()
{
	local target
	if use doc; then
		target="install"
	else
		target="install-noapi"
	fi
	emake DESTDIR=${D} ${target} || die "emake ${target} failed"
	newinitd ${S}/packing/portage/yate.init yate
	newconfd ${S}/packing/portage/yate.conf yate
}
