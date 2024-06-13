import { React } from 'react';
import DocumentsGrid from './DocumentsGrid';
import { useSelector } from 'react-redux';

export default function DocumentsGridContainer() {
  const results = useSelector((state) => state.results);

  return <DocumentsGrid results={results} />;
}
