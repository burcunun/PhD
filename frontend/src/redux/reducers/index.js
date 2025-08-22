import { combineReducers } from 'redux';
import tableSearchReducer from './tableSearch';
import loadingReducer from './loading';
import menuCollapseReducer from './menuCollapse';
import mobileMediaReducer from './mobileMedia';
import queryReducer from './query';
import resultsReducer from './results';
import resultsLoadingReducer from './resultsLoading';
import showResultsReducer from './showResults';
import searchMethodReducer from './searchMethod';

const allReducers = combineReducers({
  mobileMedia: mobileMediaReducer,
  menuCollapse: menuCollapseReducer,
  showResults: showResultsReducer,
  query: queryReducer,
  results: resultsReducer,
  loading: loadingReducer,
  tableSearch: tableSearchReducer,
  resultsLoading: resultsLoadingReducer,
  searchMethod: searchMethodReducer,
});

export default allReducers;
