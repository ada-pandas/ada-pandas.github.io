$countries_big = 'DE', 'ES', 'FR', 'IT'
$pollutants1 = 'CO', 'PM2.5'
$pollutants2 = 'NO2', 'O3', 'PM10', 'CO'
foreach ($country in $countries_big)
{
	ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -mkdir ./data/${country}"
	foreach($pollutant in $pollutants1)
	{
		echo $country
		echo $pollutant
		scp -r ../data/${country}/${pollutant} soldaten@iccluster040.iccluster.epfl.ch:
		ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -copyFromLocal ${pollutant} ./data/{$country}/"
		ssh soldaten@iccluster040.iccluster.epfl.ch "rm -r ${pollutant}"
	}
	foreach($pollutant in $pollutants2)
	{
		echo $country
		echo $pollutant
		ssh soldaten@iccluster040.iccluster.epfl.ch "mkdir ${pollutant}"
		scp ../data/${country}/${pollutant}/1* soldaten@iccluster040.iccluster.epfl.ch:${pollutant}
		ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -copyFromLocal ${pollutant} ./data/{$country}/"
		ssh soldaten@iccluster040.iccluster.epfl.ch "rm ${pollutant}/*"
		scp ../data/${country}/${pollutant}/2* soldaten@iccluster040.iccluster.epfl.ch:${pollutant}
		ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -copyFromLocal ${pollutant}/* ./data/{$country}/${pollutant}"
		ssh soldaten@iccluster040.iccluster.epfl.ch "rm ${pollutant}/*"
		scp ../data/${country}/${pollutant}/3* soldaten@iccluster040.iccluster.epfl.ch:${pollutant}
		ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -copyFromLocal ${pollutant}/* ./data/{$country}/${pollutant}"
		ssh soldaten@iccluster040.iccluster.epfl.ch "rm ${pollutant}/*"
		scp ../data/${country}/${pollutant}/4* ../data/${country}/${pollutant}/5* ../data/${country}/${pollutant}/6* ../data/${country}/${pollutant}/7* ../data/${country}/${pollutant}/8* ../data/${country}/${pollutant}/9* soldaten@iccluster040.iccluster.epfl.ch:${pollutant}
		ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -copyFromLocal ${pollutant}/* ./data/{$country}/${pollutant}"
		ssh soldaten@iccluster040.iccluster.epfl.ch "rm -r ${pollutant}"
	}
}