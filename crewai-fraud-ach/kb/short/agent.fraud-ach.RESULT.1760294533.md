```json
{
  "id": "d36a7df7c16d867c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294533,
  "host_pid": "9e6742732c60:1",
  "hash": "41260f5ecc092af78cdfc672c9ee458db7d0bb170c6009ba624cdfcace9c67d1",
  "cid": "QmV141260f5ecc092af78cdfc672c9ee458db7d0bb17",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294533,
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
      "evaluated_at": 1760294533
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
  "sig": "d96882ba4803094be8ef7c4e48dc532c7716886059a754099dc1773f17590aec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159149641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 46477440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '1bdba49a970d4caa'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}