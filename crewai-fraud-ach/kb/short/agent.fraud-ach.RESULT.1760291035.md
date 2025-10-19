```json
{
  "id": "e5f567cfd2d36200",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291035,
  "host_pid": "9e6742732c60:1",
  "hash": "b173d25c3ccb40025ccf9c37afa65f9fc76d9987f3a99ff6657aaf7c1b6b4a3c",
  "cid": "QmV1b173d25c3ccb40025ccf9c37afa65f9fc76d9987",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291035,
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
      "evaluated_at": 1760291035
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
  "sig": "bdcdec2b44b2ccbd4a77c070d4539181e538793bc11cfc2711971e125cc5b2ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023966417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 75049260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285764, 'matching_hash': 'bf59b19c5a8c3ed8'}}}