```json
{
  "id": "00034de9b1a98f1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287437,
  "host_pid": "9e6742732c60:1",
  "hash": "c143f36f619a26e8a746c8bf030a51e7adf6a40edea92d6a34e8ffb0d075ba06",
  "cid": "QmV1c143f36f619a26e8a746c8bf030a51e7adf6a40e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287437,
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
      "evaluated_at": 1760287437
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
  "sig": "58f479ff33f69a336ca6f85035eead749449e7299b898e5988fed89fbbcc0ef2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594714846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 67462256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760284979, 'matching_hash': 'bc3982de93079c96'}}}