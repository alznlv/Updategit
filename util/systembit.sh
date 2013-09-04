function is64()
{
 result=$(uname -a |grep i386)
 if [ "$result" == "" ]; then 
    return 0
 else
    echo $result
    return 1
 fi
}

if is64 ;
then
   echo '64bit system'
else
   echo '32bit system'
fi
