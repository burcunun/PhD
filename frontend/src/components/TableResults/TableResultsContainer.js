import React from 'react';
import TableResults from './TableResults';
import { useSelector } from 'react-redux';

export default function TableResultsContainer() {
  const results = useSelector((state) => state.results);
console.log(results);
  return <TableResults results={results} />;
}
