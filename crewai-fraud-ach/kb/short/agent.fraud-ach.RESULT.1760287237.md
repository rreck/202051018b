```json
{
  "id": "e7275057b2a4d31b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287237,
  "host_pid": "9e6742732c60:1",
  "hash": "de9b15bbb442711a4a01af6afe0c472450bc3a0e64c78e03eb02f709938203bc",
  "cid": "QmV1de9b15bbb442711a4a01af6afe0c472450bc3a0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287237,
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
      "evaluated_at": 1760287237
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2484316059074074614d7be1772371123802eae07ea198160f67df3a94add481"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 044000037758614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285763, 'matching_hash': '8cf13377232eef82'}}}764, 'matching_hash': '7bd2e976d6ef9e3c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9245331}}}