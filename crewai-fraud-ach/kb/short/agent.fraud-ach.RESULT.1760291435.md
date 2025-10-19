```json
{
  "id": "72371b8357e060ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291435,
  "host_pid": "9e6742732c60:1",
  "hash": "224711287c96640aca698b0682b63757e2ae1e8061cceb046624a7e4e4fc455b",
  "cid": "QmV1224711287c96640aca698b0682b63757e2ae1e80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291435,
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
      "evaluated_at": 1760291435
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
  "sig": "205bdfa3eb49ab0f0367d0bc92d5224a973d4eecbab550ff4c0aac1009bed456"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022956374
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 29127525, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '4e30c52d3b71935d'}}}