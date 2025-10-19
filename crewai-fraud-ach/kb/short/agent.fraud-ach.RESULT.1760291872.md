```json
{
  "id": "deb4660eebf8e3b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291872,
  "host_pid": "9e6742732c60:1",
  "hash": "517624db25f8d7e84e40c7dbb5274a1f8abeb8ca499b1cf91ace999865bcc2a4",
  "cid": "QmV1517624db25f8d7e84e40c7dbb5274a1f8abeb8ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291872,
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
      "evaluated_at": 1760291873
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
  "sig": "c14f9350865ae979f8d5f692b69657c10839888b723aa786b06faf3731f3e31d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 47665805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}