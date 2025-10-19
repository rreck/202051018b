```json
{
  "id": "392b5427f5fda0e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286241,
  "host_pid": "9e6742732c60:1",
  "hash": "f5aa685b786e19033dda78fe0e4995c43563504298da170b1e92b0a476d6fba2",
  "cid": "QmV1f5aa685b786e19033dda78fe0e4995c435635042",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286241,
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
      "evaluated_at": 1760286241
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "6427d6fe67d91d6d0df7d67d6399b6504369dec41b96981efe32305dc2f6216a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000026531578
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': 'f6751e9d8f5fd136'}}}re': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285764, 'matching_hash': '13ee20e814facee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.37, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8942822}}}