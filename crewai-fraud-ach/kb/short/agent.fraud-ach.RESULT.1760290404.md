```json
{
  "id": "dd361278ed8050e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290404,
  "host_pid": "9e6742732c60:1",
  "hash": "b07897bb97a2fdf98676e3f1cbf16cae8ad4eb67e125ecd6fa9bf142ebd489fa",
  "cid": "QmV1b07897bb97a2fdf98676e3f1cbf16cae8ad4eb67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290404,
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
      "evaluated_at": 1760290404
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
  "sig": "ade76ff57041b7dfd2d586c1f8ab62e42388d74b9e0da0c6df2550ee2029a190"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 72222237, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}