```json
{
  "id": "632645e40740d6a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285639,
  "host_pid": "9e6742732c60:1",
  "hash": "8506d1fb7ac64ef9a3ea124982888c43c0b20b0d439c5faf868859316a655dbe",
  "cid": "QmV18506d1fb7ac64ef9a3ea124982888c43c0b20b0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285639,
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
      "evaluated_at": 1760285639
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
  "sig": "5405fea1c4654152fe54db0927cf95ec9f86d3a4b010406dbacf1d3e9efc26a9"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 17163770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}