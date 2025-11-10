export default function ActivityCard({ activity }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <h3 className="text-lg font-semibold text-gray-800 mb-2">{activity.title}</h3>
      <p className="text-gray-600 mb-4">{activity.description}</p>
      
      {/* Participants Section */}
      {activity.participants && activity.participants.length > 0 && (
        <div className="mt-6 pt-4 border-t border-gray-200">
          <h3 className="text-sm font-semibold text-gray-700 mb-3">Participants ({activity.participants.length})</h3>
          <ul className="space-y-2">
            {activity.participants.map((participant, index) => (
              <li key={index} className="flex items-center text-sm text-gray-600">
                <span className="inline-block w-2 h-2 bg-blue-500 rounded-full mr-2"></span>
                {participant}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}