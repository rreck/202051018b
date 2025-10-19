```json
{
  "id": "77856ce1bfd61c71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294360,
  "host_pid": "9e6742732c60:1",
  "hash": "3e5f83eefb4cf23a16fc41b2279120e3dfdedfa9fdbe1ed29c7743dc3e0ac064",
  "cid": "QmV13e5f83eefb4cf23a16fc41b2279120e3dfdedfa9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294360,
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
      "evaluated_at": 1760294360
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
  "sig": "f62b2b81579021f8399f1e678ad1bab072adc64fa00755bf655636f98abeac8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153539871
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 59000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '6120bfc166994b37'}}}