```json
{
  "id": "155d38930e6cc111",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294574,
  "host_pid": "9e6742732c60:1",
  "hash": "41dcf37eedd66e8b0444d8be77badf705113bde07f5e260d38a1ccafed085670",
  "cid": "QmV141dcf37eedd66e8b0444d8be77badf705113bde0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294574,
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
      "evaluated_at": 1760294574
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
  "sig": "be1aa1edbcd57739312accd24426f5fb77f087d122720f2153c6905039a93ce5"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000025312922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 1379946240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': 'ec5c02804d9cd63b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5749776}}}