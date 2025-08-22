const resultsLoadingReducer = (state = false, action) => {
  switch (action.type) {
    case 'RESULTS_LOADING':
      return !state;
    default:
      return state;
  }
};

export default resultsLoadingReducer;
