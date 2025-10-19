```json
{
  "id": "01267d17be8e05f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294845,
  "host_pid": "9e6742732c60:1",
  "hash": "b41fee004cac3b3c7239921462d7be2132f216663bbdb1613c99be7f6cdfb0cd",
  "cid": "QmV1b41fee004cac3b3c7239921462d7be2132f21666",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294845,
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
      "evaluated_at": 1760294845
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
  "sig": "9a808195f8a3ed96e83289b0d040c0020b6b8707354e3de12e8f8396f2058de2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159928324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 107724785, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': 'f9e49b53b0020755'}}}