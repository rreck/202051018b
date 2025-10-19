```json
{
  "id": "0cbab101a9053c5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289825,
  "host_pid": "9e6742732c60:1",
  "hash": "018aa9e5453ac0299fd7488c497c6121f981fcbb54ed5f53a92994e4d05b71ca",
  "cid": "QmV1018aa9e5453ac0299fd7488c497c6121f981fcbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289825,
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
      "evaluated_at": 1760289825
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
  "sig": "e99700f2386dc4ac9332b43b2f759795dadc1b53c7e1811f2c077309c2500f4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 12545884, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}