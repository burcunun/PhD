import React from 'react';
import { Box, Link, Typography, Button } from '@mui/material';
import Logo from '../../assets/logo_v1.png';
import style from './style';
import SearchIcon from '@mui/icons-material/Search';
import TocIcon from '@mui/icons-material/Toc';
import MenuBookIcon from '@mui/icons-material/MenuBook';
import InfoIcon from '@mui/icons-material/Info';

export default function Navbar(props) {
  const classes = style();

  return (
    <Box className={classes.mainContainer}>
      <Box className={classes.logoContainer}>
        <img className={classes.logo} src={Logo} alt="logo" />
        <Box className={classes.titleContainer}>
          <Typography
            className={classes.title}
            variant="subtitle2"
            color="secondary"
          >
            Innovation
            <br />
            Sustainability
            <br />
            Search
            <br />
            Engine
            <br />
          </Typography>
        </Box>
      </Box>

      <Box className={classes.lineBreak}></Box>

      <Box className={classes.navLinksContainer}>
        <Box className={classes.linkContainer}>
          <SearchIcon />
          <Link
            onClick={props.handleSearch}
            className={classes.link}
          >
            Search
          </Link>
        </Box>
        <Box className={classes.linkContainer}>
          <TocIcon />
          <Link
            onClick={props.handleTableSearch}
            className={classes.link}
          >
            Table View
          </Link>
        </Box>
      </Box>

      <Box className={classes.lineBreak}></Box>
    </Box>
  );
}
