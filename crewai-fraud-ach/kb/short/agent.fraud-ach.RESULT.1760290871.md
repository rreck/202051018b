```json
{
  "id": "e37a233717901d3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290871,
  "host_pid": "9e6742732c60:1",
  "hash": "11bf433a2870b6616f5cf636ababdd7e11d87a8772f863392bd1c2aacde5a22b",
  "cid": "QmV111bf433a2870b6616f5cf636ababdd7e11d87a87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290871,
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
      "evaluated_at": 1760290871
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
  "sig": "89878c3e0186682a2eb6c4e44c541beb4f9ad3e1d9335ce4711d9a93e5bceb0c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 32151861, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}