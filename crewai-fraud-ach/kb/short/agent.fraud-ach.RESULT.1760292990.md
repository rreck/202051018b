```json
{
  "id": "e15fed1c4e13a959",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292990,
  "host_pid": "9e6742732c60:1",
  "hash": "7bf2e9c78263d785a04b408a6a7235d552fe4d389118844b7d9da88778016c0b",
  "cid": "QmV17bf2e9c78263d785a04b408a6a7235d552fe4d38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292990,
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
      "evaluated_at": 1760292990
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
  "sig": "f00dbf4e280a6c81d634a8939029d6d0cce76136143175df8e8b16cbcb742375"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155376461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 62886219, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': 'ed3a1cd9da35e724'}}}