import React from 'react';
import { Box, Stack, Switch } from '@mui/material';
import ResultsBoxContainer from '../../components/ResultsBox/ResultsBoxContainer';
import NavbarContainer from '../../components/Navbar/NavbarContainer';
import SearchbarContainer from '../../components/SearchBar/SearchBarContainer';
import { motion } from 'framer-motion';

import style from './style';
import { Typography } from '@mui/material';
import TableResultsContainer from '../../components/TableResults/TableResultsContainer';

export default function Home(props) {
  const classes = style();

  return (
    <Box className={classes.mainContainer}>
      <Box className={classes.navbarContainer}>
        <NavbarContainer />
      </Box>
      <Box className={classes.searchResultContainer}>
        <Box className={classes.searchbarContainer}>
          <SearchbarContainer />
        </Box>
        <Box className={classes.resultBoxContainer}>
          {props.tableSearch && <TableResultsContainer />}
          {!props.tableSearch && <ResultsBoxContainer />}
        </Box>
      </Box>
    </Box>
  );
}
