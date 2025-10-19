```json
{
  "id": "1d50cb7790935820",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291205,
  "host_pid": "9e6742732c60:1",
  "hash": "c9441c7755f280841381487352e04480fd3b71e32279fef260bef367dc5a181d",
  "cid": "QmV1c9441c7755f280841381487352e04480fd3b71e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291205,
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
      "evaluated_at": 1760291205
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
  "sig": "388e6f71b21df3c8fbf51345668ae0f11a839693018bd892072b817bfc7a0a00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597800882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 34713783, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': 'e972b74e8fc22124'}}}