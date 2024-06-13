import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Chip from '@mui/material/Chip';
import PictureAsPdfIcon from '@mui/icons-material/PictureAsPdf';

export default function TableResults({ results }) {
  //console.log(results);
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Rank</TableCell>
            <TableCell>Title</TableCell>
            <TableCell>Score</TableCell>
            <TableCell>Total Cost</TableCell>
            <TableCell>EU Contribution</TableCell>
            <TableCell>Duration</TableCell>
            <TableCell>End Date</TableCell>
            <TableCell>Database</TableCell>
            <TableCell>Download PDF</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {results.results.map((doc) => (
            <TableRow key={doc['_source'].title}>
              <TableCell>{doc['_source'].rank}</TableCell>
              <TableCell sx={{ maxWidth: '12rem' }}>
                <a href={doc['_source'].source} target="_blank">{doc['_source'].title}</a>
              </TableCell>
              <TableCell>{doc['_source'].score.toFixed(3)}</TableCell>
              <TableCell>
                {doc['_source'].totalCost == null || doc['_source'].totalCost == "" ? "-" : "€ " + doc['_source'].totalCost.toLocaleString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
              </TableCell>
              <TableCell>
                {doc['_source'].ecMaxContribution == null || doc['_source'].ecMaxContribution == "" ? "-" : "€ " + doc['_source'].ecMaxContribution.toLocaleString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}  
              </TableCell>
              <TableCell>
                {doc['_source'].duration == null ||doc['_source'].duration == "" ? "-" : doc['_source'].duration.toString() + " months"} 
              </TableCell>
              <TableCell>
                {doc['_source'].endDate == null ? "-":doc['_source'].endDate}
              </TableCell>
              <TableCell>
                {doc['_source'].database}
              </TableCell>
              <TableCell>                
		<a href={doc['_source'].pdfLink} target="_blank">
		   <Chip color="primary" sx={{ cursor: 'pointer' }} icon={<PictureAsPdfIcon color="primary" />} label="PDF" />
		</a>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
