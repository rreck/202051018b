```json
{
  "id": "f7594472b43765d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290123,
  "host_pid": "9e6742732c60:1",
  "hash": "e625ba400cb989f09f5c4a88c704d6d398da17f57525ba8f6605908342c86bf0",
  "cid": "QmV1e625ba400cb989f09f5c4a88c704d6d398da17f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290123,
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
      "evaluated_at": 1760290123
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
  "sig": "a0bb5f67a9f04a5c6614a15fffa421f153b04f4f23dc1fc756ed3044c456a1f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020245133
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 35500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '4426f66f5774a1b4'}}}