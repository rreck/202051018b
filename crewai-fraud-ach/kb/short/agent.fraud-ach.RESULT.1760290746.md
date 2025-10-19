```json
{
  "id": "1a520f9088ab787c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290746,
  "host_pid": "9e6742732c60:1",
  "hash": "dad2fb8c06e822ce881c8bdb81ebc7994da5696db4eda42c1e29f454cef2f564",
  "cid": "QmV1dad2fb8c06e822ce881c8bdb81ebc7994da5696d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290746,
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
      "evaluated_at": 1760290746
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
  "sig": "607a85d561051125fd3ce07ebae04edd6858dbbb39f1f85175b6d56e101d9898"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036487644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 98443098, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760284979, 'matching_hash': '0d42dcc750e3a553'}}}