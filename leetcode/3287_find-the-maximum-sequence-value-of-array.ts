const MAXIMUM_OR_VALUE: number = 1 << 7;

function maxValue(nums: number[], k: number): number {
    const sequenceLength: number = nums.length;
    
    const forwardReachableValues: boolean[][][] = buildForwardReachableValues(nums, k);
    const backwardReachableValues: boolean[][][] = buildBackwardReachableValues(nums, k);
    
    return findMaximumXor(forwardReachableValues, backwardReachableValues, sequenceLength, k);
}

function createDynamicProgrammingTable(
    sequenceLength: number,
    subsequenceSize: number,
): boolean[][][] {
    const elementCountDimension: number = subsequenceSize + 2;
    
    return Array.from({ length: sequenceLength + 1 }, () =>
        Array.from({ length: elementCountDimension }, () => Array(MAXIMUM_OR_VALUE).fill(false)),
);
}

function buildForwardReachableValues(numbers: number[], subsequenceSize: number): boolean[][][] {
    const sequenceLength: number = numbers.length;
    const reachableValues: boolean[][][] = createDynamicProgrammingTable(sequenceLength, subsequenceSize);
    
    // base case: 0 elements selected evaluates to 0
    reachableValues[0][0][0] = true;
    
    for (let currentIndex: number = 0; currentIndex < sequenceLength; currentIndex++) {
        for (let selectedCount: number = 0; selectedCount <= subsequenceSize; selectedCount++) {
            propagateStates(
                reachableValues,
                currentIndex,
                currentIndex + 1,
                selectedCount,
                numbers[currentIndex],
            );
        }
    }
    
    return reachableValues;
}

function buildBackwardReachableValues(numbers: number[], subsequenceSize: number): boolean[][][] {
    const sequenceLength: number = numbers.length;
    const reachableValues: boolean[][][] = createDynamicProgrammingTable(sequenceLength, subsequenceSize);
    
    // base case: 0 elements selected evaluates to 0
    reachableValues[sequenceLength][0][0] = true;
    
    for (let currentIndex: number = sequenceLength; currentIndex > 0; currentIndex--) {
        for (let selectedCount: number = 0; selectedCount <= subsequenceSize; selectedCount++) {
            propagateStates(
                reachableValues,
                currentIndex,
                currentIndex - 1,
                selectedCount,
                numbers[currentIndex - 1],
            );
        }
    }
    
    return reachableValues;
}

function propagateStates(
    reachableValues: boolean[][][],
    fromIndex: number,
    toIndex: number,
    selectedCount: number,
    currentNumber: number,
): void {
    for (let currentOrValue: number = 0; currentOrValue < MAXIMUM_OR_VALUE; currentOrValue++) {
        if (!reachableValues[fromIndex][selectedCount][currentOrValue]) {
            continue;
        }
        
        // paths diverge into either bypassing the number or accumulating its bitwise value
        reachableValues[toIndex][selectedCount][currentOrValue] = true;
        reachableValues[toIndex][selectedCount + 1][currentOrValue | currentNumber] = true;
    }
}

function findMaximumXor(
    forwardReachableValues: boolean[][][],
    backwardReachableValues: boolean[][][],
    sequenceLength: number,
    subsequenceSize: number,
): number {
    let maximumXor: number = 0;
    
    // evaluate all valid partitioning points to guarantee non-overlapping subsequences
    for (
        let splitPoint: number = subsequenceSize;
        splitPoint <= sequenceLength - subsequenceSize;
        splitPoint++
    ) {
        const localMaximum: number = evaluateSplitPoint(
            forwardReachableValues[splitPoint][subsequenceSize],
            backwardReachableValues[splitPoint][subsequenceSize],
        );
        
        maximumXor = Math.max(maximumXor, localMaximum);
    }
    
    return maximumXor;
}

function evaluateSplitPoint(
    firstSequenceReachableValues: boolean[],
    secondSequenceReachableValues: boolean[],
): number {
    let maximumXor: number = 0;
    
    for (let firstOrValue: number = 0; firstOrValue < MAXIMUM_OR_VALUE; firstOrValue++) {
        if (!firstSequenceReachableValues[firstOrValue]) {
            continue;
        }
        
        for (let secondOrValue: number = 0; secondOrValue < MAXIMUM_OR_VALUE; secondOrValue++) {
            if (!secondSequenceReachableValues[secondOrValue]) {
                continue;
            }
            
            maximumXor = Math.max(maximumXor, firstOrValue ^ secondOrValue);
        }
    }
    
    return maximumXor;
}
