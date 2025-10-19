```json
{
  "id": "bfa6b06a046f462e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285422,
  "host_pid": "9e6742732c60:1",
  "hash": "7db25abe5b4cd6bbb105fe8346ba451660676665c74f9131c9337ea894fbde5a",
  "cid": "QmV17db25abe5b4cd6bbb105fe8346ba451660676665",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285422,
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
      "evaluated_at": 1760285422
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
  "sig": "700149d23de773ad1389f81cbcf2c382ead0c238bbc643b996a2b755e70b5cc1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18541336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}