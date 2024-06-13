import { React, useEffect } from 'react';
import { Box } from '@mui/material';
import Navbar from './Navbar';
import NavbarSmall from './NavbarSmall';
import { useSelector, useDispatch } from 'react-redux';
import { openTableSearch, closeTableSearch } from '../../redux/actions';

export default function NavbarContainer() {
  const isMobile = useSelector((state) => state.mobileMedia);
  const collapse = useSelector((state) => state.menuCollapse);
  const tableSearch = useSelector((state) => state.tableSearch);
  const dispatch = useDispatch();
  const handleTableSearch = () => {
    dispatch(openTableSearch());
  };

  const handleSearch = () => {
    dispatch(closeTableSearch());
  };

  return (
    <Box>
      {!isMobile && (
        <Navbar
          handleTableSearch={handleTableSearch}
          handleSearch={handleSearch}
        />
      )}
      {isMobile && <NavbarSmall collapse={collapse} />}
    </Box>
  );
}
