```json
{
  "id": "1bf8b3f8839610ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289620,
  "host_pid": "9e6742732c60:1",
  "hash": "8c79b908e584380158d47a08d8c782e20c0aeeeb2d48d3f9dc2de16dbaff8d30",
  "cid": "QmV18c79b908e584380158d47a08d8c782e20c0aeeeb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289620,
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
      "evaluated_at": 1760289620
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
  "sig": "a21f04973db4c056505ce973aa32097c6268193afb6f05cea58ab197437673ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279614717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 50700416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': '2481e4baa9b260b7'}}}