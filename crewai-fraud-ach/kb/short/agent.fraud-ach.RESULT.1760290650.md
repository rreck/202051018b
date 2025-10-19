```json
{
  "id": "b597888f8a1d4b5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290650,
  "host_pid": "9e6742732c60:1",
  "hash": "065b7a0c7a31c763b8e5bc28b22ab1c6a16ba43e65217e0ad42650919088d679",
  "cid": "QmV1065b7a0c7a31c763b8e5bc28b22ab1c6a16ba43e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290650,
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
      "evaluated_at": 1760290650
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
  "sig": "486e6269c0e745a4efe51d3504420a7910ec36f3395bd7c9bd9968a058738d8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275498951
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 29668548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'a1e1622f9da312c5'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}