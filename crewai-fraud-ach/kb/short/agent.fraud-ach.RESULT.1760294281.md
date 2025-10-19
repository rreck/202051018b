```json
{
  "id": "8e50578a00dbd856",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294281,
  "host_pid": "9e6742732c60:1",
  "hash": "a24e1d8c39adb717dbb0b1ec0a41b85634401ddf8609bb74a25618372b54c312",
  "cid": "QmV1a24e1d8c39adb717dbb0b1ec0a41b85634401ddf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294281,
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
      "evaluated_at": 1760294281
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
  "sig": "2af498182f082d263e59e5aa6502eaf4baf427ba151355f458412f49fdf7f7bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591602283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 34199785, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '995d19d96715feaf'}}}