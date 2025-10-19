```json
{
  "id": "6a24653e1391c22c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287962,
  "host_pid": "9e6742732c60:1",
  "hash": "2f0a04f8590fa0736a5b9f7be5302e7bef3c9c0fe961fab78a517741fd7e8496",
  "cid": "QmV12f0a04f8590fa0736a5b9f7be5302e7bef3c9c0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287962,
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
      "evaluated_at": 1760287962
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "2ce7aed0095ad2e87e3839495073be37cefe9f0b7bb7370e9e05d2571c6a506f"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000022964635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 78000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': '99d3229e22856917'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}