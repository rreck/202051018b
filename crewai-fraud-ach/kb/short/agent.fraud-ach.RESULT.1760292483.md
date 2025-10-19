```json
{
  "id": "6749573c7d7e98b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292483,
  "host_pid": "9e6742732c60:1",
  "hash": "ffa8e8a936539023f58e0b709703de9ed35496f1b0e17d43e25da2f5f791308e",
  "cid": "QmV1ffa8e8a936539023f58e0b709703de9ed35496f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292483,
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
      "evaluated_at": 1760292483
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
  "sig": "f181d4c9150bc223cb0ac05b02fbc5928c80c6775c14f6c5d3a24a82c3040be7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 63013104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}