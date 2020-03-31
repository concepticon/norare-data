cd concept_set_meta
echo '# Brysbaert-2009-Frequency'
cd Brysbaert-2009-Frequency
python map.py map validate
cd ..
echo "# Brysbaert-2014-Concreteness"
cd Brysbaert-2014-Concreteness
python map.py map validate
cd ..
echo "# Cai-2010-SUBTLEXCH"
cd Cai-2010-SUBTLEXCH
python map.py map validate
cd ..
echo "# Kuperman-2012-AoA"
cd Kuperman-2012-AoA
python map.py map validate
cd ..
echo "# Riegel-2015-NAWL"
cd Riegel-2015-NAWL
python map.py map validate
cd ..
echo "# Starostin-2000-Sense"
cd Starostin-2000-Sense
python map.py validate
cd ..
cd ..

