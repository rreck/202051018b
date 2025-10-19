```json
{
  "id": "4637fd6d0f014cd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285821,
  "host_pid": "9e6742732c60:1",
  "hash": "2fd8e277959d171a92da4afdcd6a39f1cbfc79774dafc0f20ce1dd80b2b611c1",
  "cid": "QmV12fd8e277959d171a92da4afdcd6a39f1cbfc7977",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285821,
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
      "evaluated_at": 1760285821
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
  "sig": "921fe36a5ac55acea84986a24ffa7acaf03b36431156dbef3c1986ff2f2b381a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249268740
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': '2b1c4c9f55d7dd69'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}