```json
{
  "id": "edbba61bed284667",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289899,
  "host_pid": "9e6742732c60:1",
  "hash": "4c54e3cec962c74eabf2c2af05702c201b19ef6921ff89e1df527cfecb54ce1b",
  "cid": "QmV14c54e3cec962c74eabf2c2af05702c201b19ef69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289899,
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
      "evaluated_at": 1760289899
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
  "sig": "644dc2886680eb6e1a095a824861ed8f1db41e3f6015c4e0844160f95ceae115"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158395869
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 17312528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': '78e23c3ea29c8ae5'}}}