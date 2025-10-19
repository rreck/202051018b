```json
{
  "id": "4b02351d5cc34b39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290908,
  "host_pid": "9e6742732c60:1",
  "hash": "187b3a0a586fd6f5c47de1668381a6a3614e7a0313693fb962b0ef2ca0f10cd0",
  "cid": "QmV1187b3a0a586fd6f5c47de1668381a6a3614e7a03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290908,
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
      "evaluated_at": 1760290908
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
  "sig": "18ba85eb71fcb02e4d55cbdf87a50d9def32f9d41e161cb33901c2c3129a0b10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 38852460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '7b717df8c1c9c887'}}}