#!/bin/bash
#Le but de ce script est de voir les differentes formes de code de sortie dans un script Shell
#Ce script est basé sur celui présent sur le site "https://bash.cyberciti.biz/guide/Exit_command"

BAK=/data2
TAPE=/dev/st0
echo "Sauvegarde du repertoire ${BAK} sur la cassette ${TAPE} .."

# Test sur l'existance du repertoire $BAK
# Si le repertoire n'existe pas, affiche un message d'erreur puis retourne le code erreur 1
[ ! -d $BAK ] && { echo "Le repertoire source $BAK n'existe pas."; exit 1; }

# Test sur l'existance du device $TAPE 
# Puis retourne un message d'erreur avec un code sortie erreur 2 
[ ! -b $TAPE ] && { echo "Le device $TAPE n'a pas ete trouve ou configure."; exit 2; }

# Le backup peut commencer
# Si une erreur survient, elle est envoyee sur /tmp/error.log 
tar cvf $TAPE $BAK 2> /tmp/error.log

#Si l'operation precedante n'a pas retourner de code 0 (pour dire que tout c'est bien deroule)
if [ $? -ne 0 ]
then
   # Affiche un message d'erreur puis retourne le code erreur 3 
   echo "Une erreur est survenue pendant la sauvegarde, voir le fichier /tmp/error.log".
   exit 3 
fi

# Termine le script avec un potentiel message (par exemple "sauvegarde effectuee!")
exit 0