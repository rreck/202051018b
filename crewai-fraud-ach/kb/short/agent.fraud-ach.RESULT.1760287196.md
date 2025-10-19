```json
{
  "id": "8e4b66edf85d913c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287196,
  "host_pid": "9e6742732c60:1",
  "hash": "86a8d6e5c66116aedf3c7b073c415211f2eb4544c8b275f016c5c118036175b9",
  "cid": "QmV186a8d6e5c66116aedf3c7b073c415211f2eb4544",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287196,
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
      "evaluated_at": 1760287196
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "46248d0fef07dedb702b9ac0061a97fcd2364c98c04a31a0ad649aa04ad89f8d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 16230648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}