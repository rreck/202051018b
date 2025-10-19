```json
{
  "id": "a15ab58a9d1e0f3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290330,
  "host_pid": "9e6742732c60:1",
  "hash": "221732a1762394bc4145bd3f73dc5cb1ca9d8e7042d0b5a0aae82feb8aaa4c5e",
  "cid": "QmV1221732a1762394bc4145bd3f73dc5cb1ca9d8e70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290330,
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
      "evaluated_at": 1760290330
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
  "sig": "40c2410e71bb82810e64962779857da07429a94d63dad37b9dcde4da204a3f5c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 46782456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}