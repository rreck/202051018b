```json
{
  "id": "b4602c2994b6aacd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293418,
  "host_pid": "9e6742732c60:1",
  "hash": "7f5288c5d90d7836720cf5ccded882c9462db71539bcfe4db9991289de0841b3",
  "cid": "QmV17f5288c5d90d7836720cf5ccded882c9462db715",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293418,
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
      "evaluated_at": 1760293418
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
  "sig": "2bebbd7b20a63d0439e5a28b6db13f23fc5d917cece7e6b0fbb1815af067ef0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 41530526, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}