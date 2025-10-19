```json
{
  "id": "866a4c43df23b041",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292926,
  "host_pid": "9e6742732c60:1",
  "hash": "2f11e6f4ea4fb1c6182d96364bab624d19aa8a93cdd90db0f0b56c7208040325",
  "cid": "QmV12f11e6f4ea4fb1c6182d96364bab624d19aa8a93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292926,
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
      "evaluated_at": 1760292926
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
  "sig": "5d3cffc6a08c9a1cb2b78d5fd1ab75b3a4c200ed9e8a1ee90f10731bde1a3fc7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027294403
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 41549664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '8d40dd17cbab8bca'}}}