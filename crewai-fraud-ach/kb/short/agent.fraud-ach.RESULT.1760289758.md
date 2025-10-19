```json
{
  "id": "95b16d5cdfd43c79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289758,
  "host_pid": "9e6742732c60:1",
  "hash": "918d87d4837bb3662d423eff92a6d3e156b0f56d9a7b3d9c9b4fcee0a950a38c",
  "cid": "QmV1918d87d4837bb3662d423eff92a6d3e156b0f56d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289758,
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
      "evaluated_at": 1760289758
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
  "sig": "64c17f8d56dd3c28e6051e7541b8bb9e75cd6bca4c5f3d618bd19d652991abde"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026697062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 66409824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760284979, 'matching_hash': 'f9d80f2e7cffa5ec'}}}