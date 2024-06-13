import React from 'react';
import { Box, Link, Typography, Icon } from '@mui/material';
import Logo from '../../assets/logo_v1.png';
import style from './style';
import SearchIcon from '@mui/icons-material/Search';
import TocIcon from '@mui/icons-material/Toc';
import MenuBookIcon from '@mui/icons-material/MenuBook';
import InfoIcon from '@mui/icons-material/Info';
import { useSelector, useDispatch } from 'react-redux';
import { openTableSearch, closeTableSearch } from '../../redux/actions';

export default function Menu() {
  const classes = style();
  const dispatch = useDispatch();
  const handleTableSearch = () => {
    dispatch(openTableSearch());
  };

  const handleSearch = () => {
    dispatch(closeTableSearch());
  };
  return (
    <Box className={classes.menuContainer}>
      <Box className={classes.logoContainer}>
        <img className={classes.logo} src={Logo} alt="logo" />
        <Box className={classes.titleContainer}>
          <Typography
            className={classes.title}
            variant="subtitle2"
            color="primary"
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
            onClick={handleSearch}
            className={classes.link}
          >
            Search
          </Link>
        </Box>
        <Box className={classes.linkContainer}>
          <TocIcon />
          <Link
            onClick={handleTableSearch}
            className={classes.link}
          >
            Table View
          </Link>
        </Box>
      </Box>
    </Box>
  );
}
