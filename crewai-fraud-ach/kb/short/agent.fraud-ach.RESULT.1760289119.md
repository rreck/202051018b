```json
{
  "id": "67abb757a745b666",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289119,
  "host_pid": "9e6742732c60:1",
  "hash": "6427daf43bfe55b60fc92488322f29b5e99290037df21c2c0b5105b9de980d70",
  "cid": "QmV16427daf43bfe55b60fc92488322f29b5e9929003",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289119,
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
      "evaluated_at": 1760289119
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
  "sig": "e540075301ed30011107418b1a7555e0cc82463080133eff12c3eff6188f8e81"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155818462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 37370340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': '4e45a5675434ecee'}}}