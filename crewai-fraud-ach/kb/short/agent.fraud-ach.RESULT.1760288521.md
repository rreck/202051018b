```json
{
  "id": "f3396ebfcb2d7eb3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288521,
  "host_pid": "9e6742732c60:1",
  "hash": "efb506aba45c89e2e45de8e552b7ad3e570aa9877da194736e167573292868fa",
  "cid": "QmV1efb506aba45c89e2e45de8e552b7ad3e570aa987",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288521,
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
      "evaluated_at": 1760288521
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
  "sig": "c054d38a2786e01aaf160451a234f996c19cc2671285732b88fd3a38b9b36290"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464768410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 44932032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '182aec6491bb83ab'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}