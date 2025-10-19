```json
{
  "id": "1ebc13bf31335c9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293166,
  "host_pid": "9e6742732c60:1",
  "hash": "2d0f319a05136af54c9685f8205f4502232530f27f193be68814091d2fd87f34",
  "cid": "QmV12d0f319a05136af54c9685f8205f4502232530f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293166,
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
      "evaluated_at": 1760293166
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
  "sig": "cbfd5b0aeb99071662c0bf6d32373644a9128eb86338284001406caf9f95fab9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243793866
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 46332612, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '3f378333472d9dcb'}}}maly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6478434}}}