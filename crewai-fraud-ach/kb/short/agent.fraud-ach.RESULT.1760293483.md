```json
{
  "id": "e6a2ae5e29625a1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293483,
  "host_pid": "9e6742732c60:1",
  "hash": "42fbc0ac298077413faf370558ed75c3b62f81970f12f28c79bda60dcd991897",
  "cid": "QmV142fbc0ac298077413faf370558ed75c3b62f8197",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293483,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293483
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "02ed09aaedc2f52ee79d6fdb5dab0b38a2ac2f39cf489eea08de79f22247aafb"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 1711546977, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.04, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7815283}}}