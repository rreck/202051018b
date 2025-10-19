```json
{
  "id": "10a95bfc6643475f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293834,
  "host_pid": "9e6742732c60:1",
  "hash": "d0dded736f7b081d4952f08aa9d138910bc44d6feafb4f297ee53aa94efbddb1",
  "cid": "QmV1d0dded736f7b081d4952f08aa9d138910bc44d6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293834,
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
      "evaluated_at": 1760293834
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
  "sig": "0a0d44a3366d41e21310329c019cedb0bed330612fda0002b719c359f4bcd04b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462505262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 88486684, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': 'e15f6eb56271d036'}}}