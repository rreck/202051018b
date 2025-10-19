```json
{
  "id": "2047e7a8467ce1a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292950,
  "host_pid": "9e6742732c60:1",
  "hash": "74c2986121a624dcf9c195ae243f423a0718a1dc989e0244841c6ba74f24d62a",
  "cid": "QmV174c2986121a624dcf9c195ae243f423a0718a1dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292950,
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
      "evaluated_at": 1760292950
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
  "sig": "bca84b4f76d149c7d6aeabbfd50938f3bd6d88351c284d48a4c723c8c6268234"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279614717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 82388176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '2481e4baa9b260b7'}}}