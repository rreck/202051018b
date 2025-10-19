```json
{
  "id": "f2757530832711ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289677,
  "host_pid": "9e6742732c60:1",
  "hash": "aea56ff645e0d01b3e8a3e763895f72c0a9496789f11ef4e75661d76e27c0e78",
  "cid": "QmV1aea56ff645e0d01b3e8a3e763895f72c0a949678",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289677,
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
      "evaluated_at": 1760289677
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
  "sig": "9cc085f29a3f51457cc5aaf6c8978ceeb8e8118dd5a02a9b78ce1f2c312d2f02"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 44251350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}