

<?php
$memcache = new Memcache();
$memcache->connect('prod-vpc-ray-cache3.ahri5l.cfg.apse1.cache.amazonaws.com', 11211) or die ("Could not connect");
$list = array();
for ($i = 1; $i <= 257729; $i++) {
    $key = "sharesettings_acceptance_reminder_".$i
    $val = $memcache->get($eName);
    if ($val) {
        var_dump($val)    
    }
    
}



?>
