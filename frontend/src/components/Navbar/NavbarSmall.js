import React from 'react';
import { Box, Link, Typography, Icon } from '@mui/material';
import Logo from '../../assets/logo_v1.png';
import Menu from './Menu';
import MenuIcon from '@mui/icons-material/Menu';
import style from './style';
import { IconButton } from '@mui/material';
import { useSelector, useDispatch } from 'react-redux';
import { menuCollapse } from '../../redux/actions';

export default function NavbarSmall({ collapse }) {
  const classes = style();
  const dispatch = useDispatch();

  return (
    <Box className={classes.navSmallContainer}>
      <Box className={classes.menuIcon}>
        <IconButton onClick={() => dispatch(menuCollapse())}>
          <MenuIcon />
        </IconButton>
      </Box>
      <Box className={classes.menuMainContainer}>{collapse && <Menu />}</Box>
    </Box>
  );
}
