```json
{
  "id": "b819016f25caff44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291431,
  "host_pid": "9e6742732c60:1",
  "hash": "ff60ace50da3b2273d62f9b1f748e9bddafe2a8a15512a1a25c23c6a3b51afc1",
  "cid": "QmV1ff60ace50da3b2273d62f9b1f748e9bddafe2a8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291431,
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
      "evaluated_at": 1760291431
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
  "sig": "aada80a3455cfc15478d1ec1ff5fdb524cc460a5504c3084f5c5e4d24b5865b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271052795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 38606400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '457d955844db0007'}}}