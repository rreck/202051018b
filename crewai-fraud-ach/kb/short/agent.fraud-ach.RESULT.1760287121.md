```json
{
  "id": "d6abb8399c71a86a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287121,
  "host_pid": "9e6742732c60:1",
  "hash": "e309c552638d8665b4ac5cb1f0e0488b857801eea84ebfbfce8a33eae33f6f18",
  "cid": "QmV1e309c552638d8665b4ac5cb1f0e0488b857801ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287121,
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
      "evaluated_at": 1760287121
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
  "sig": "faae470abbaa1bfbae8d53eac0c9d410f1914af8c76c3da06c24124c4c19c24a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025560621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13310360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '1e88fa5a655ec1c9'}}}