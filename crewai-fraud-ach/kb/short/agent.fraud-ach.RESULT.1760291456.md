```json
{
  "id": "5fee1a85a5e55936",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291456,
  "host_pid": "9e6742732c60:1",
  "hash": "57e175102da68b4afcff501c30281ce90809fe9f99517dba942ba4ec4015a7b5",
  "cid": "QmV157e175102da68b4afcff501c30281ce90809fe9f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291456,
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
      "evaluated_at": 1760291456
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
  "sig": "3ebb5185bd07e06d00c86702eb15f3dd6d5feae6729f1c5c54d9c0c3d1c78a61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270344488
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 46681775, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285764, 'matching_hash': 'ec3de169da630728'}}}