import { React } from 'react';
import SearchBar from './SearchBar';
import { useSelector, useDispatch } from 'react-redux';
import {
  setQuery,
  setResults,
  showResults,
  dontShowResults,
  resultsIsLoading,
} from '../../redux/actions';
import axios from 'axios';

export default function SearchBarContainer() {
  const query = useSelector((state) => state.query);
  const searchMethod = useSelector((state) => state.searchMethod);
  const dispatch = useDispatch();

  const queryAPI = async () => {
    dispatch(resultsIsLoading());
    dispatch(dontShowResults());
    await axios
      .post(
        'http://' +
          process.env.REACT_APP_SERVER_IP +
          ':5000/query/' +
          searchMethod,
        { term: query }
      )
      .then(function (response) {
        // handle success
        dispatch(setResults(response.data));
        dispatch(showResults());
        dispatch(resultsIsLoading());
      })
      .catch(function (error) {
        // handle error
        dispatch(dontShowResults());
      });
  };

  const handleOnChange = (e) => {
    dispatch(setQuery(e.target.value));
  };

  const handleOnClick = () => {
    queryAPI();
  };  
const handleOnEnter = (e) => {
    if(e.charCode===13){
    	queryAPI();
    }
  };

  return (
    <SearchBar handleOnEnter={handleOnEnter} handleOnChange={handleOnChange} handleOnClick={handleOnClick} />
  );
}
