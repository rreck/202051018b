```json
{
  "id": "efa1dd1060f96209",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289235,
  "host_pid": "9e6742732c60:1",
  "hash": "2929f318b288a0b455d1d720e58abeaf851c4246bce807eb67fbd64e502e78ac",
  "cid": "QmV12929f318b288a0b455d1d720e58abeaf851c4246",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289235,
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
      "evaluated_at": 1760289235
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
  "sig": "efc6e86ec0545795187284b38bcb99c2ec1c51afb12f5a2bce83a4c7c62e3a7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 56179890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}