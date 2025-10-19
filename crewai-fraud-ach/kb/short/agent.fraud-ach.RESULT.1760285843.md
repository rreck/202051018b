```json
{
  "id": "4a324673a82eed1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285843,
  "host_pid": "9e6742732c60:1",
  "hash": "bbc973b09342a74191d17ef938ee72e0f7da116f48fb2b7ebdbfc3311ce2195f",
  "cid": "QmV1bbc973b09342a74191d17ef938ee72e0f7da116f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285843,
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
      "evaluated_at": 1760285843
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
  "sig": "17fd3bf9c513fdf4dd11fcfe3a42a7679afb0f16a09645b686539f8c0983de10"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105158691889
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285764, 'matching_hash': '7f09a9884a1a1f0e'}}}