package require solvate
package require autoionize
package require autopsf

proc quickPrep {id out {padding {{15 15 15} {15 15 15}}}} {
    autopsf -mol $id -prefix TEMP -protein
    mol delete all
    set id_psf [mol new TEMP.psf]
    mol addfile TEMP.pdb
    set minmax [measure minmax [atomselect $id_psf all]]
    set min [vecsub [lindex $minmax 0] [lindex $padding 0]]
    set max [vecadd [lindex $minmax 1] [lindex $padding 1]]
    set box [list $min $max]
    solvate TEMP.psf TEMP.pdb -o TEMP -minmax $box 
#    autoionize -psf solvate.psf -pdb solvate.pdb -sc .15 -o $out
    autoionize -psf TEMP.psf -pdb TEMP.pdb -neutralize -o $out
    mol delete all
    file delete TEMP.psf
    file delete TEMP.pdb
}
