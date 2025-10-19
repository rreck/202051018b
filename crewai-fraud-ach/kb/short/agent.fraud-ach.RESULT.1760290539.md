```json
{
  "id": "e1ee0be24041d15f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290539,
  "host_pid": "9e6742732c60:1",
  "hash": "78cf0c5e263b65f733b46e7118dd5d2fa31a3d4d9683fd2a9e3a8af0ddf7a75c",
  "cid": "QmV178cf0c5e263b65f733b46e7118dd5d2fa31a3d4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290539,
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
      "evaluated_at": 1760290539
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
  "sig": "541ecff0b6f36a2bdae080f8d2312d034e54a1f9424da2e8b6e7e0a8e4f271d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032341010
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 16322040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': 'f26a81694d784881'}}}