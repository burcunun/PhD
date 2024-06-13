const showResultsReducer = (state = false, action) => {
  switch (action.type) {
    case 'SHOW_RESULTS':
      return true;
    case 'DONT_SHOW_RESULTS':
      return false;
    default:
      return state;
  }
};

export default showResultsReducer;
