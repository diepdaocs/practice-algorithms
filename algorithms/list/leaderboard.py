from typing import TypeVar, Generic, List, Optional, Tuple, Dict
from heapq import heappush, heappop

T = TypeVar('T')

class Leaderboard(Generic[T]):
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize a leaderboard with an optional maximum size.
        If max_size is specified, only the top N players will be kept.
        """
        self._heap: List[Tuple[float, int, T]] = []  # (score, timestamp, player)
        self._player_scores: Dict[T, Tuple[float, int]] = {}  # player -> (score, timestamp)
        self._max_size = max_size
        self._counter = 0  # Used for timestamp to break ties
    
    def add_score(self, player: T, score: float) -> None:
        """
        Add or update a player's score on the leaderboard.
        Higher scores are better (e.g., points in a game).
        Time complexity: O(log n)
        """
        # Update player's score in dictionary
        self._player_scores[player] = (-score, self._counter)  # Negative score for max heap behavior
        
        # Add to heap
        heappush(self._heap, (-score, self._counter, player))
        self._counter += 1
        
        # Maintain max size if specified
        if self._max_size is not None and len(self._heap) > self._max_size:
            # Remove excess items from heap
            while len(self._heap) > self._max_size:
                _, _, p = heappop(self._heap)
                # Only remove from heap if it's not the player's current score
                if p in self._player_scores and self._player_scores[p][0] != -score:
                    continue
                break
    
    def get_top(self, n: int = 10) -> List[Tuple[T, float]]:
        """
        Get the top N players and their scores.
        Returns a list of tuples (player, score) sorted by score in descending order.
        Time complexity: O(n log n)
        """
        n = min(n, len(self._heap))
        # Create a copy of the heap to avoid modifying the original
        temp_heap = self._heap.copy()
        result = []
        
        for _ in range(n):
            if not temp_heap:
                break
            score, _, player = heappop(temp_heap)
            # Only include if it's the player's current score
            if player in self._player_scores and self._player_scores[player][0] == score:
                result.append((player, -score))
        
        return result
    
    def get_player_rank(self, player: T) -> Optional[int]:
        """
        Get the current rank of a player (1-based).
        Returns None if the player is not on the leaderboard.
        Time complexity: O(n log n)
        """
        
        if player not in self._player_scores:
            return None
            
        player_score = self._player_scores[player][0]
        rank = 1
        
        # Create a copy of the heap to avoid modifying the original
        temp_heap = self._heap.copy()
        while temp_heap:
            score, _, p = heappop(temp_heap)
            # Only count if it's the player's current score
            if p in self._player_scores and self._player_scores[p][0] == score:
                if score < player_score:  # Remember scores are negative
                    rank += 1
                if p == player:
                    return rank
        
        return None
    
    def get_player_score(self, player: T) -> Optional[float]:
        """
        Get the current score of a player.
        Returns None if the player is not on the leaderboard.
        Time complexity: O(1)
        """
        if player in self._player_scores:
            return -self._player_scores[player][0]
        return None
    
    def clear(self) -> None:
        """Clear all scores from the leaderboard. Time complexity: O(1)"""
        self._heap.clear()
        self._player_scores.clear()
        self._counter = 0
    
    def __len__(self) -> int:
        """Return the number of players on the leaderboard. Time complexity: O(1)"""
        return len(self._player_scores)
    
    def __str__(self) -> str:
        """
        Return a string representation of the leaderboard.
        Time complexity: O(n log n)
        """
        items = self.get_top(len(self._heap))
        return f"Leaderboard(items={items})"


# Example usage
if __name__ == "__main__":
    # Create a leaderboard
    lb = Leaderboard[str](max_size=5)
    
    # Add some scores
    lb.add_score("Player1", 100)
    lb.add_score("Player2", 150)
    lb.add_score("Player3", 120)
    lb.add_score("Player4", 200)
    lb.add_score("Player5", 180)
    
    print("Initial leaderboard:", lb)
    
    # Get top 3 players
    print("\nTop 3 players:")
    for player, score in lb.get_top(3):
        print(f"{player}: {score}")
    
    # Update a player's score
    lb.add_score("Player1", 250)
    print("\nAfter updating Player1's score:", lb)
    
    # Get Player1's rank
    rank = lb.get_player_rank("Player1")
    print(f"\nPlayer1's current rank: {rank}")
    
    # Get Player1's score
    score = lb.get_player_score("Player1")
    print(f"Player1's current score: {score}") 