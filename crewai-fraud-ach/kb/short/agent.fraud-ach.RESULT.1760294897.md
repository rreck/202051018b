```json
{
  "id": "2a4890dfe3d832a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294897,
  "host_pid": "9e6742732c60:1",
  "hash": "82f0601bcbfdd63080165271573cf26b8488da085893c61322c560a6a701153e",
  "cid": "QmV182f0601bcbfdd63080165271573cf26b8488da08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294897,
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
      "evaluated_at": 1760294897
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
  "sig": "94d607e20377a18c8fde25af183aba0104b57807dd83c5e21a13aa0ac48aa9b6"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 1510201380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.08, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6139030}}}