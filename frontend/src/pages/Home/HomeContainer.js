import { React, useEffect } from 'react';
import { Box } from '@mui/material';
import Home from './Home';
import { useSelector, useDispatch } from 'react-redux';
import axios from 'axios';
import {
  elasticSearchMethod,
  isLoading,
  denseSearchMethod,
} from '../../redux/actions';
import LoadingContainer from '../Loading/LoadingContainer';
import { motion } from 'framer-motion';

export default function HomeContainer() {
  const loading = useSelector((state) => state.loading);
  const tableSearch = useSelector((state) => state.tableSearch);
  const searchMethod = useSelector((state) => state.searchMethod);
  const dispatch = useDispatch();

  const handleSwitch = (e) => {
    searchMethod === 'dense_vectors'
      ? dispatch(elasticSearchMethod())
      : dispatch(denseSearchMethod());
  };

  const variants = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
    },
    exit: {
      opacity: 0,
    },
  };

  const checkAPI = async () => {
    await axios
      .post('http://' + process.env.REACT_APP_SERVER_IP + ':5000/')
      .then(function (response) {
        // handle success
        dispatch(isLoading());
      })
      .catch(function (error) {
        // handle error
      });
    setTimeout(() => dispatch(isLoading()), 1500);
  };

  useEffect(() => {
    checkAPI();
  }, []);

  return (
    <Box>
      {loading && <LoadingContainer />}
      {!loading && (
        <motion.div variants={variants} initial="hidden" animate="show">
          <Home tableSearch={tableSearch} handleSwitch={handleSwitch} />{' '}
        </motion.div>
      )}
    </Box>
  );
}
