```json
{
  "id": "1bf2af1689ac670f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290399,
  "host_pid": "9e6742732c60:1",
  "hash": "5b2d9f903a4f4cc1206811611976e7599e4991ecf1bcb16d33e55af0fed95f6f",
  "cid": "QmV15b2d9f903a4f4cc1206811611976e7599e4991ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290399,
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
      "evaluated_at": 1760290399
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
  "sig": "515ea508d5d6f8f87e2ca04b06df61ed385c9395c0afa40d82a4a123632ece3d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277311413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '8eaabbab3b444a6b'}}}