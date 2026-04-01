#include <iostream>
#include <map>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

enum class SubSequenceType
{
	Candidate,
	Invalid,
};

long long count_subsequences(
	long long sum_target,
	long long max_target,
	const vector<long long> &sequence,
	SubSequenceType mode)
{
	auto is_allowed = [&](long long value)
	{
		if (mode == SubSequenceType::Candidate)
		{
			return value <= max_target;
		}
		return value < max_target;
	};

	long long total = 0;
	const int sequence_size = static_cast<int>(sequence.size());

	int index = 0;
	while (index < sequence_size)
	{
		while (index < sequence_size && !is_allowed(sequence[index]))
		{
			++index;
		}

		if (index >= sequence_size)
		{
			break;
		}

		std::map<long long, long long> seen_prefix_sums;
		seen_prefix_sums[0] = 1;

		long long prefix_sum_total = 0;
		while (index < sequence_size && is_allowed(sequence[index]))
		{
			prefix_sum_total += sequence[index];
			const long long required_prefix = prefix_sum_total - sum_target;

			const auto found = seen_prefix_sums.find(required_prefix);
			if (found != seen_prefix_sums.end())
			{
				total += found->second;
			}

			++seen_prefix_sums[prefix_sum_total];
			++index;
		}
	}

	return total;
}

void solve()
{
	std::ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int number_of_testcases;
	cin >> number_of_testcases;

	while (number_of_testcases-- > 0)
	{
		int sequence_length;
		long long sum_target;
		long long max_target;
		cin >> sequence_length >> sum_target >> max_target;

		vector<long long> full_sequence(sequence_length);
		bool has_exact_max_target = false;

		for (int i = 0; i < sequence_length; ++i)
		{
			cin >> full_sequence[i];
			if (full_sequence[i] == max_target)
			{
				has_exact_max_target = true;
			}
		}

		if (!has_exact_max_target)
		{
			cout << 0 << '\n';
			continue;
		}

		const long long candidate_subsequences = count_subsequences(
			sum_target,
			max_target,
			full_sequence,
			SubSequenceType::Candidate);

		const long long invalid_subsequences = count_subsequences(
			sum_target,
			max_target,
			full_sequence,
			SubSequenceType::Invalid);

		cout << (candidate_subsequences - invalid_subsequences) << '\n';
	}
}

int main()
{
	solve();
	return 0;
}
