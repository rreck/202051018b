```json
{
  "id": "7e36d350bba956e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289338,
  "host_pid": "9e6742732c60:1",
  "hash": "f774ec8bc6f265c15be2a38b13213d65a1e0704e3c6d0ea57a545396ec5e6c17",
  "cid": "QmV1f774ec8bc6f265c15be2a38b13213d65a1e0704e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289338,
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
      "evaluated_at": 1760289338
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
  "sig": "b10f2ee0a87fb516f7909be85252cf859df0b39638687d46b9de798c052fdd8f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593563572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 19362840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}