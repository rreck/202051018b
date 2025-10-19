```json
{
  "id": "97f568979c620e89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292539,
  "host_pid": "9e6742732c60:1",
  "hash": "53fce2ce7361cb0cd473a7b0b353352ceabc17362ee8bd5c49b78bb27c794d24",
  "cid": "QmV153fce2ce7361cb0cd473a7b0b353352ceabc1736",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292539,
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
      "evaluated_at": 1760292539
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
  "sig": "eb34dd41a82214f94300202c6b648ba23bd9953d29c107cefa4620966f379382"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028645436
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 100000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '6242cc5f185f73d7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}