const tableSearchReducer = (state = false, action) => {
  switch (action.type) {
    case 'OPEN_TABLE_SEARCH':
      return true;
    case 'CLOSE_TABLE_SERACH':
      return false;
    default:
      return state;
  }
};

export default tableSearchReducer;
