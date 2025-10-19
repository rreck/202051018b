```json
{
  "id": "ee01d0462963012d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292055,
  "host_pid": "9e6742732c60:1",
  "hash": "46509a02252ade98e3654e9cc26eb518bf65feb748f6bfc8a074832145364bcd",
  "cid": "QmV146509a02252ade98e3654e9cc26eb518bf65feb7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292055,
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
      "evaluated_at": 1760292055
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
  "sig": "2726724c373847f8a78244c0fbd437044b8ac2c0043e835cc3f553ca822ddd6d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021173532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 58262841, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'a0cc7134a86fdd26'}}}