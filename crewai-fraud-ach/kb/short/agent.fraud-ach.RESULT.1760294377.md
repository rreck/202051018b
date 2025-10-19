```json
{
  "id": "3a0120b383ad69b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294377,
  "host_pid": "9e6742732c60:1",
  "hash": "03126444d8464c38068616386719e12a3553befa95ad6db7af3c60370b01d84d",
  "cid": "QmV103126444d8464c38068616386719e12a3553befa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294377,
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
      "evaluated_at": 1760294377
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
  "sig": "c166756a8ff3d263a1fe2dd2d4dee5834c4a3fabe002f7b327909b9082dbdb09"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022029572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 63694935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'ab8acd1ae94c4a1e'}}}maly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9144651}}}