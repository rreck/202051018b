```json
{
  "id": "df1b8d0fae43c311",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287583,
  "host_pid": "9e6742732c60:1",
  "hash": "d723695ce02d0661bece59f6e39f104c59211f8cfab42b7e117a1bee48ba28eb",
  "cid": "QmV1d723695ce02d0661bece59f6e39f104c59211f8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287583,
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
      "evaluated_at": 1760287583
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
  "sig": "d1072f76bf323f7522e41e2759dfc99230d5ee7f79ac30c58ca07b9e358fe718"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 22081020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}