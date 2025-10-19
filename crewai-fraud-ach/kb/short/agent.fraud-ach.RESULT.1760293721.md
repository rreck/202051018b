```json
{
  "id": "5fffdf1d89ce3eeb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293721,
  "host_pid": "9e6742732c60:1",
  "hash": "f3bd4eb5f02522a013475a740723ac9c8f6d7730e682a33bafbb3f80af71eb8a",
  "cid": "QmV1f3bd4eb5f02522a013475a740723ac9c8f6d7730",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293721,
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
      "evaluated_at": 1760293721
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
  "sig": "15d53f7079c2fa3796f229a532efa982500a75dbe3a76bdba12fc44d824bf211"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151773289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 110177088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}