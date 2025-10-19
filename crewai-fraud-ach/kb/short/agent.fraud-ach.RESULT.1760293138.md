```json
{
  "id": "2a071b98e5dc125b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293138,
  "host_pid": "9e6742732c60:1",
  "hash": "28b4603dc06f353fbdd27d13669273b9062119e60af910856b69372c609f92e4",
  "cid": "QmV128b4603dc06f353fbdd27d13669273b9062119e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293138,
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
      "evaluated_at": 1760293138
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
  "sig": "2a1387d6a1bb9ba189761e31d008766db8869388b095307282b98fa1077ac59b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462119178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 89777548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '2f807700ebd65d7c'}}}