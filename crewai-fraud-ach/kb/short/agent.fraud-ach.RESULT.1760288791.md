```json
{
  "id": "40affc33d7a0547d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288791,
  "host_pid": "9e6742732c60:1",
  "hash": "cb7a12c22e733bc4e9ffbfeff799aa557f9a933695cefc61d08ffe15d7dc3737",
  "cid": "QmV1cb7a12c22e733bc4e9ffbfeff799aa557f9a9336",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288791,
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
      "evaluated_at": 1760288791
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
  "sig": "0f25653df0108e6a30246639dcea1ea85df61521d7477189ce2ef183fc4feada"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271976362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 42008928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285764, 'matching_hash': 'fe2a7bcd9137a402'}}}