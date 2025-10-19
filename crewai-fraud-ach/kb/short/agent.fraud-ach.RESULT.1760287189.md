```json
{
  "id": "9f8ce621ad4e404c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287189,
  "host_pid": "9e6742732c60:1",
  "hash": "c70622c01034c4feef2f75919d59bdb55a3205e80f7ea4466861b7e3f444f1b6",
  "cid": "QmV1c70622c01034c4feef2f75919d59bdb55a3205e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287189,
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
      "evaluated_at": 1760287189
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
  "sig": "cf177cfe9017d461ed9a61371244da3acd77f881cccd8e2905600eb55cfd7b97"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000246033311
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 24473370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285764, 'matching_hash': 'd9b4b01f0add79d3'}}}