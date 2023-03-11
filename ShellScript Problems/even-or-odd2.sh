integer=$1

function test(){
    
    if [ $((integer % 2)) -eq 0 ]
    then
      echo "Even"
    else
      echo "Odd"
    fi
}

test
