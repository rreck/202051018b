```json
{
  "id": "754cf27597e3e59c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292317,
  "host_pid": "9e6742732c60:1",
  "hash": "35400cd9dd9edce11903fa3100041ee4e0898518c95020cc324eb470766287d5",
  "cid": "QmV135400cd9dd9edce11903fa3100041ee4e0898518",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292317,
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
      "evaluated_at": 1760292317
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
  "sig": "7ee6777f98a9d00da4332e945f65b0554a18c22d58343703d5ff3658283487e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466383232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 38951055, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '37ada470abbef201'}}}