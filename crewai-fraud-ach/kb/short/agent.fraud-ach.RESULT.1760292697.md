```json
{
  "id": "dee992802ae48793",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292697,
  "host_pid": "9e6742732c60:1",
  "hash": "c4fe078a98b4f893f4a5787fa33816c3718793d83fd7ee23da560f0bd8f8176c",
  "cid": "QmV1c4fe078a98b4f893f4a5787fa33816c3718793d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292697,
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
      "evaluated_at": 1760292697
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
  "sig": "c578cdb61637060fbb3546e96296858570ef21819e6d151f8e448230a4762940"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277214063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 58170665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'ff6f9f90137c8ef9'}}}