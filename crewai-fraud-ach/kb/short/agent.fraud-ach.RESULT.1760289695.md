```json
{
  "id": "910da52815885464",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289695,
  "host_pid": "9e6742732c60:1",
  "hash": "ea2338432dc5e796aedae52a8fb00463664b77a41b70213eabfba9e8f6e2dd91",
  "cid": "QmV1ea2338432dc5e796aedae52a8fb00463664b77a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289695,
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
      "evaluated_at": 1760289695
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
  "sig": "a6b680b1d906b36f1fd5da3fbbe06679b5b093dbe83b3da070f4c2a0cbaf4899"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}