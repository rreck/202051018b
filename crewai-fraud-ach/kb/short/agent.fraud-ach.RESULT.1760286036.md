```json
{
  "id": "27ae027ad1f1b705",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286036,
  "host_pid": "9e6742732c60:1",
  "hash": "6f7c7efe67ef08bf0b3b334bd73121e7bda5f4b6961494132f61c5de3896994f",
  "cid": "QmV16f7c7efe67ef08bf0b3b334bd73121e7bda5f4b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286036,
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
      "evaluated_at": 1760286036
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
  "sig": "fe0904a9ecc11438d51e565bb381da07fb7acc366a6c071241cb62959190e4fe"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037578651
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': '25cb229761d99325'}}}