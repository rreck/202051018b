```json
{
  "id": "3f452b489c81b5a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289158,
  "host_pid": "9e6742732c60:1",
  "hash": "24e1648e053181cb76812669142a9dae038f1e4d7296f080563f4cf0ca107e49",
  "cid": "QmV124e1648e053181cb76812669142a9dae038f1e4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289158,
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
      "evaluated_at": 1760289158
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
  "sig": "c97d75f69c54c77f057f1d06c4785c27a9047bf247cdadb119ab5e59648b0591"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}een': 1760285763, 'matching_hash': 'ecded74c6845c7bc'}}}