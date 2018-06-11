#!/usr/bin/env python
<?php

    function divisable($x){
        return ((($x % 3) == 0) or (($x % 5) == 0)); 
    }

    $total = 0;
    foreach (range(1, 1000) as $i) {
        if(divisable($i)){
            $total += $i;
        }
    }

    echo $total;