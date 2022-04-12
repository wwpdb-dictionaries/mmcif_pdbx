s/##V5NEXT##//

# V5_NEXT subsititutions
#
# V50_GROW
/#V50_GROW$/ {
	     /loop/ {   # delelete loop_
	     	    d;
		    }
	     /_item_range.max/ {
	            s/.*/    _item_range.maximum         350.0/
		    }
	     /_item_range.min/ {
	            s/.*/    _item_range.minimum         150.0/
		    }
		    
	     /0.0 *0.0/ { d; }
}
# V50_SHELL_FREE
/#V50_SHELL_FREE$/ {
	     /_item_range.min/ {
	            s/.*/    _item_range.minimum          10.0   0.0/
		    }
}

# V50_SHELL_POS
/#V50_SHELL_POS$/ {
            /\. *0.0/{
	    	 s/   \. *0.0.*$/ 100.0 100.0/
		 a\
				100.0   0.0
		 }
}


/#V50_RMERGE_ALL$/ {
           d;
}

/#V50_SHELL_RMERGE$/ {
           /145.0/ { d;}
	   / 0\.0 *0\.0/ {
	           s/   0\.0 *0\.0.*/10.0    0.0/
	                }
}


/#V50_REFLNS_RMERGE_OBS$/ { d; }

/#V50_REFLNS_SHELL_SYM$/ { d; }