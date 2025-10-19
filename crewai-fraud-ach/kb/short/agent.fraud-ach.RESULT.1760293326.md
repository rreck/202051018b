```json
{
  "id": "b1de919f3fc7bb33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293326,
  "host_pid": "9e6742732c60:1",
  "hash": "1bd247ee6bf431d420a973ee16c0427afdb26581c5f18df0373c7f1d02d8251f",
  "cid": "QmV11bd247ee6bf431d420a973ee16c0427afdb26581",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293326,
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
      "evaluated_at": 1760293326
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
  "sig": "5e902acd064f7782a9a773cafd236b03821d96cb2735e4de29b35007f2c55d3b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279738088
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 32090688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '31a7269ac1c5c77d'}}}