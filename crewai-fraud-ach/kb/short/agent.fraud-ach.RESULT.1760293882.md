```json
{
  "id": "255797bf7e9b9d22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293882,
  "host_pid": "9e6742732c60:1",
  "hash": "ae1c7338cda716a5e7ee12c889f2bafacb6a4024ce325c92cc60c8dee84227a7",
  "cid": "QmV1ae1c7338cda716a5e7ee12c889f2bafacb6a4024",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293882,
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
      "evaluated_at": 1760293882
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
  "sig": "36717a1465073c3cc21c5475bb1d88de7237d9b23fbc2560c7ea553061153415"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038607326
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 36076202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}