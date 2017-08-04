set terminal pngcairo background "#202020" enhanced fontscale 1.1 size 640, 480
set output 'histogram.png'

set style fill transparent solid 0.5 border
set border lw 2 lc rgb "#dadada"
set xtics textcolor rgb "#dadada"
set ytics textcolor rgb "#dadada"

unset key

set xlabel "" 
set xrange [ 0 : 256 ] noreverse nowriteback
set ylabel "" 
set yrange [ 0 : 260000 ] noreverse nowriteback
unset ytics
set zero 1e-08
set locale "en_US.UTF-8"
GNUTERM = "wxt"

set tmargin 0
set bmargin 0
set lmargin 1
set rmargin 1

set multiplot layout 2,1 margins 0.05,0.95,.1,.99 spacing 0,0

unset xtics
set ylabel "Grayscale" textcolor rgb "#dadada"
p "hist.dat" u 1:2 lc rgb 'dark-grey' w filledcurve

unset label

set xtics 32
set ylabel "RGB" textcolor rgb "#dadada"
p "hist.dat" u 1:3 lc rgb '#8b0001' w filledcurve, \
          "" u 1:4 lc rgb '#00468b' w filledcurve, \
          "" u 1:5 lc rgb '#468b00' w filledcurve

unset multiplot
#    EOF
