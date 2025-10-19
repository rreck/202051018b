```json
{
  "id": "16eb5dbe810fe15b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293611,
  "host_pid": "9e6742732c60:1",
  "hash": "a4a8607278e20980b726adca40bb5ed4e98b8fc48e367d3cb6226245c97c9d21",
  "cid": "QmV1a4a8607278e20980b726adca40bb5ed4e98b8fc4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293611,
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
      "evaluated_at": 1760293611
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
  "sig": "338fbed04d2f6044d51ff0d5e283b2e55045d209f91c898accfd79e0c85c7665"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000026930485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 111000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285764, 'matching_hash': '3159baf1077152c6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}