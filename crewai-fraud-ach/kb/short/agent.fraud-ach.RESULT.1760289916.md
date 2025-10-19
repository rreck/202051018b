```json
{
  "id": "cc752e4cc73e7d6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289916,
  "host_pid": "9e6742732c60:1",
  "hash": "43f5136d392ee9317f50335f94a4c8569f9550856917f1d55db316b5dcc13cfe",
  "cid": "QmV143f5136d392ee9317f50335f94a4c8569f955085",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289916,
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
      "evaluated_at": 1760289916
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
  "sig": "f9b18d5e44fe4a7314587b3b6771062d53b9c94c9e08e1b481156196425aaef4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 43281728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}