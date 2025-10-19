```json
{
  "id": "364eff17cd1d210d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287731,
  "host_pid": "9e6742732c60:1",
  "hash": "a4c6f123e4d41925489ba5d4da521edadbe4f657d2caebc977087423975a3428",
  "cid": "QmV1a4c6f123e4d41925489ba5d4da521edadbe4f657",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287731,
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
      "evaluated_at": 1760287731
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
  "sig": "5a93d4a6128bf516b0017063a2b9a8bf7e67418b61863da24e54c11ba9b6f195"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}