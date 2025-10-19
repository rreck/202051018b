```json
{
  "id": "d44800730c068ebb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288753,
  "host_pid": "9e6742732c60:1",
  "hash": "9582de6c0fe8781c4af116ec86556c90d3906dc5eb9aca7cbcd39500ce108966",
  "cid": "QmV19582de6c0fe8781c4af116ec86556c90d3906dc5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288753,
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
      "evaluated_at": 1760288753
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
  "sig": "4d3c9a91d622c94f0e020abf5ac8a315c7f17cb2c2965e791e6a4bf2ed73ed1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023498410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 13625767, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': 'a97f330737c5e5f9'}}}