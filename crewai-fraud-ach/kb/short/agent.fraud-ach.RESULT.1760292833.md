```json
{
  "id": "f49aa59ce624467c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292833,
  "host_pid": "9e6742732c60:1",
  "hash": "e945b85f014a5a4572f82bc81b18b826768a3179efb03a2f276512d6ac4f2d6e",
  "cid": "QmV1e945b85f014a5a4572f82bc81b18b826768a3179",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292833,
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
      "evaluated_at": 1760292833
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
  "sig": "6a353ed76b751aca0fbc19b538733415a1f3559a4e6485c26e2de43fe27c5a18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247830233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 29219246, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '6844006e916a1387'}}}