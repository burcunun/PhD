const resultsReducer = (state = { results: [] }, action) => {
  switch (action.type) {
    case 'SET_RESULTS':
      return { ...state, results: action.payload };
    default:
      return state;
  }
};

export default resultsReducer;
