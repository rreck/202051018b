```json
{
  "id": "dd9c538f2c610646",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285898,
  "host_pid": "9e6742732c60:1",
  "hash": "c602512b9ba2085776e7bac296345ee3cc68241c8953db51a7d4c21592532bef",
  "cid": "QmV1c602512b9ba2085776e7bac296345ee3cc68241c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285898,
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
      "evaluated_at": 1760285898
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
  "sig": "cae2d4121b3d11ec96994581fcb324fe8e1441f8216cdae66fd5ba825f8bebbf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038480332
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285765, 'matching_hash': '8289eea4583ef54f'}}}