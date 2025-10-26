import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard endpoint:', apiUrl);
        console.log('Fetched leaderboard:', data);
        setLeaderboard(data.results ? data.results : data);
      });
  }, [apiUrl]);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((entry, idx) => (
          <li key={idx}>{entry.team?.name || entry.team} - {entry.points} pts</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
