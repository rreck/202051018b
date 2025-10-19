```json
{
  "id": "1f307a637e4270bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286645,
  "host_pid": "9e6742732c60:1",
  "hash": "e0051b4b6be1925ca1d930f3496c83c4fb3faf7fa8dbbdcbb7b90f98d390f970",
  "cid": "QmV1e0051b4b6be1925ca1d930f3496c83c4fb3faf7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286645,
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
      "evaluated_at": 1760286645
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "36bd5dbb357f64a9577c03332485c66f4e525b1505f373963dc7955d7a052c2d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15416736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}