```json
{
  "id": "686f11e9161feb47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290670,
  "host_pid": "9e6742732c60:1",
  "hash": "dcb8d6abc55d15bcdc564cff2ed48ab4dc7d62e8a5bfae97db13ee47bc54d029",
  "cid": "QmV1dcb8d6abc55d15bcdc564cff2ed48ab4dc7d62e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290670,
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
      "evaluated_at": 1760290670
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
  "sig": "056e85c61e01c1871c79ac4028b8aface7a53cd118aef6cc7ffefd52cac84136"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241978752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 34882068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '600b54b59692179b'}}}