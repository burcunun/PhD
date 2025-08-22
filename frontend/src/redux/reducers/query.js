const queryReducer = (state = '', action) => {
  switch (action.type) {
    case 'QUERY':
      return action.payload;
    default:
      return state;
  }
};

export default queryReducer;
