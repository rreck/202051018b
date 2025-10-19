```json
{
  "id": "b3e568d7e4a4aa79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287414,
  "host_pid": "9e6742732c60:1",
  "hash": "6a22ba030a4a010936aea2a09740b5cc3f210dfc1901ef1aa39cf110fd1224fd",
  "cid": "QmV16a22ba030a4a010936aea2a09740b5cc3f210dfc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287414,
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
      "evaluated_at": 1760287414
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8c6bab3a4f819059852b9a343a1c8134d2484baa889e84cf58d922d73da19102"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 26168801, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}