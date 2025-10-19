```json
{
  "id": "969c08463647e1d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293525,
  "host_pid": "9e6742732c60:1",
  "hash": "2d24af735f3376a73567147ff9f359a96fc2d3083a9ef72e6d4dfb4c762a4468",
  "cid": "QmV12d24af735f3376a73567147ff9f359a96fc2d308",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293525,
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
      "evaluated_at": 1760293525
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
  "sig": "8f90fe62407112a60216bea90041f8f4b9e5981589f817da9fc4a104f94c7f9b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594679703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 20177960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': 'e094f64527cf9b58'}}}