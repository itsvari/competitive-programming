function minMaxDifference(num: number): number {
  const numString: string = num.toString();
  const minVal: number = Number(numString.replaceAll(numString[0], "0"));

  for (const digit of numString) {
    if (digit !== "9") {
      const maxVal: number = Number(numString.replaceAll(digit, "9"));
      return maxVal - minVal;
    }
  }

  return num - minVal;
}
