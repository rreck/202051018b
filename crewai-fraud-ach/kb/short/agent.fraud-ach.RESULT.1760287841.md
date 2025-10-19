```json
{
  "id": "57ae7b000447af22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287841,
  "host_pid": "9e6742732c60:1",
  "hash": "31d7e431c02b5d6c28c2a7080213a9c4bc5fac78711b465f35dc4fe727cd52a3",
  "cid": "QmV131d7e431c02b5d6c28c2a7080213a9c4bc5fac78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287841,
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
      "evaluated_at": 1760287841
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
  "sig": "0969777fd64319009e1af5cb6304376230309bafaa437662f139ed2e83a40a7e"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 026009592473066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 24206214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': '48f07b8f6bc31034'}}}