```json
{
  "id": "88f6b56597316772",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292113,
  "host_pid": "9e6742732c60:1",
  "hash": "91d0df94692d0e0b91aef3f9fe67efb3aefae2529ff7c0e8865454f586fb99e5",
  "cid": "QmV191d0df94692d0e0b91aef3f9fe67efb3aefae252",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292113,
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
      "evaluated_at": 1760292113
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
  "sig": "043563b37daebb6742c22b60ffdea582ac96c1f0548a8b9b02cff336646b08b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 87169910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}