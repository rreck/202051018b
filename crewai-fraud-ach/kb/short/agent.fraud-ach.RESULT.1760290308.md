```json
{
  "id": "46ede39173b12193",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290308,
  "host_pid": "9e6742732c60:1",
  "hash": "d06bdbedd6775e1f568c4ddb8ab56298f1bf7985baba0a43df2878d3addd492d",
  "cid": "QmV1d06bdbedd6775e1f568c4ddb8ab56298f1bf7985",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290308,
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
      "evaluated_at": 1760290308
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
  "sig": "5ef6571b34ef2d31961f60e48584504260ed2f8773641e0f656a4994a3e8ba26"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 43024401, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}