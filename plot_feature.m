args = argv();
file = args{1};
xlab = file;

data = dlmread(file);

if length(args) == 0
  display("usage: ./plot_feature.m filename featurename [feature_cutoff]")
  display("you can use feature_cutoff to make your feature binary")
end

if length(args) > 1
  cutoff = sscanf(args{2}, "%d")
  data(:,1) = data(:,1) > cutoff;
  data(:,1) = data(:,1)  + randn(length(data), 1)/10;
end

data(:,2) = data(:,2) + randn(length(data), 1)/10;

plot(data(:,1), data(:,2), 'ro')
xlabel(xlab)
ylabel("is vandalism")
title(sprintf("feature %s, correlation with vandalism = %f", \
		       xlab, corrcoef(data(:,1), data(:,2))))

print([xlab, '.png'], '-dpng')

