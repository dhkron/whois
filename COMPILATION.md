pacman -S --noconfirm base-devel && \
pacman -S --noconfirm gtk-doc && \
pacman -S --noconfirm gperf && \

pacman -S --noconfirm gengetopt && \
pacman -S --noconfirm fig2dev && \
pacman -S --noconfirm help2man && \

git clone -b master https://github.com/rfc1036/whois && \
cd whois && \

wget http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz && \
tar -xf libiconv-1.14.tar.gz && \
cd libiconv-1.14  && \

# Remove stupid warning

sed -i 's/_GL_WARN_ON_USE (gets.*/\/\/REMOVED/g' srclib/stdio.in.h && \

./configure --enable-static --disable-shared && \
make CFLAGS="-static" && \
make install

cd .. && \

git clone git://git.savannah.gnu.org/libidn.git && \

cd libidn && \

touch ABOUT-NLS  && \

aclocal && \
autoconf && \
autoheader && \
autoreconf -if && \
make CFLAGS="-static" && \
make install

cd ..

HAVE_LIBIDN=true HAVE_ICONV=true LD_LBRARY_PATH=".libiconv-1.14/libs" make CFLAGS="-static -liconv" LIBS="-liconv -lidn"


# for 32 bit

pacman -Syyu
pacman -S lib32-glibc
pacman -S gcc-multilib

Recompile libiconv and libidn with -m32

remove from /etc/pacman.conf multilib commented section

HAVE_LIBIDN=true HAVE_ICONV=true LD_LBRARY_PATH=".libiconv-1.14/libs" make CFLAGS="-static -liconv -m32" LDFLAGS="-m32" LIBS="-liconv -lidn"
