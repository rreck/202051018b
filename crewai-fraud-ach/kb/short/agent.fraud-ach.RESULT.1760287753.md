```json
{
  "id": "934e6510f933f8af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287753,
  "host_pid": "9e6742732c60:1",
  "hash": "85362e2c372695d95e888ff8661a8277872f900e2d89e2b0f036354f8704fb9f",
  "cid": "QmV185362e2c372695d95e888ff8661a8277872f900e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287753,
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
      "evaluated_at": 1760287753
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
  "sig": "b6e61cf59d5aaeab10b4273df882b02ee4c931adb4374323968da2658cbfd6b8"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 021000024587821
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 30644736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': 'e3fd1743fc412dec'}}}}}}