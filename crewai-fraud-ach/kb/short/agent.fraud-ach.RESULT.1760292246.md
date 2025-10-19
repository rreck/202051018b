```json
{
  "id": "579239c2ea5964e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292246,
  "host_pid": "9e6742732c60:1",
  "hash": "6ed2f13a807165f86b268465f258457b170210d3b116cba225157f81e51bb826",
  "cid": "QmV16ed2f13a807165f86b268465f258457b170210d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292246,
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
      "evaluated_at": 1760292246
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
  "sig": "f230c7ae4ee0ccda9a17264aaa8950433426deb5b2b6689eea4aff0eef97fe37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468284841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 36149479, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}