```json
{
  "id": "289b214e2a95f074",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291489,
  "host_pid": "9e6742732c60:1",
  "hash": "7fb49cedc82ffff5d96e731842ae25c1beb0379e141e8cbd029b22c849188e68",
  "cid": "QmV17fb49cedc82ffff5d96e731842ae25c1beb0379e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291489,
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
      "evaluated_at": 1760291489
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
  "sig": "b5ff95520a848a54481426a7c5800830656863dca2774286998f454519334660"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464030736
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 19628224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': 'cf146634c1028d90'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5513113}}}