#!/bin/bash
##############################################
#Este script cambia la configuracion de      #
#las interfaces de los laboratorios para     #
#negociar la velocidad a 10Mbps o 100Mbps y  #
#los parametros de offloading y 	         #
#moderacion de RX y TX			             #
#Practicas RM 2018-2019			             #
#Uso: ./changeParameters.sh	<iface> <speed>  #
##############################################

if [ $# -ne 2 ] ; then

	echo "[$(date)] ERROR - Execution $0 <iface ID> <iface speed>"
	echo "[$(date)] INFO - Config will be applied to <iface ID>, and <iface speed> must be 10 or 100"
	exit 1
fi

if [ $2 != '10' ] && [ $2 != '100' ] ; then
	echo "[$(date)] ERROR - Execution $0 <iface ID> <iface speed>"
	echo "[$(date)] INFO - Speed cannot be set, <iface speed> must be 10 or 100"
	exit 1
fi

echo "[$(date)] INFO - $1 will be negotiated to $2 Mbps"

sudo ethtool -s  $1 speed $2 duplex full
sudo ethtool -K $1 gso off
sudo ethtool -K $1 gro off
sudo ethtool -K $1 lro off
sudo ethtool -A $1 rx off
sudo ethtool -A $1 tx off

