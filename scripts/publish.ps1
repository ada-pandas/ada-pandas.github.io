$countries_small = 'AD', 'AL', 'AT', 'BA', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DK', 'EE', 'FI', 'GB', 'GI', 'GR', 'HR', 'HU', 'IE', 'IS', 'LT', 'LU', 'LV', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SE', 'SI', 'SK', 'TR', 'XK'
$pollutants = 'CO', 'O3', 'NO2', 'PM2.5', 'PM10', 'SO2'
ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -mkdir ./data"
foreach ($country in $countries_small)
{
	ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -mkdir ./data/${country}"
	foreach($pollutant in $pollutants)
	{
		echo $country
		echo $pollutant
		If (Test-Path ../data/${country}/${pollutant} -PathType Container)
		{
			scp -r ../data/${country}/${pollutant} soldaten@iccluster040.iccluster.epfl.ch:
			ssh soldaten@iccluster040.iccluster.epfl.ch "hadoop fs -copyFromLocal ${pollutant} ./data/{$country}/"
			ssh soldaten@iccluster040.iccluster.epfl.ch "rm -r ${pollutant}"
		}
	}
}