```json
{
  "id": "6a7f94dc416d4ce9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287435,
  "host_pid": "9e6742732c60:1",
  "hash": "af0dbacd790f6471aaf9e3d1b810e0623058bd857241dd14c6d2979dc28833f3",
  "cid": "QmV1af0dbacd790f6471aaf9e3d1b810e0623058bd85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287435,
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
      "evaluated_at": 1760287435
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
  "sig": "789ab9a323434a4dfc6777a5c024322c431fd44809b86f3f78448ded485d58d2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100279947961
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': '22db2c62b181c93f'}}}een': 1760285764, 'matching_hash': 'db9686895aceb522'}}}