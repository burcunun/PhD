import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import ResutlsBox from './ResultsBox';
import { tableSearch } from '../../redux/actions';

export default function ResutlsBoxContaier() {
  const resultsLoading = useSelector((state) => state.resultsLoading);
  const showResults = useSelector((state) => state.showResults);

  return (
    <ResutlsBox resultsLoading={resultsLoading} showResults={showResults} />
  );
}
