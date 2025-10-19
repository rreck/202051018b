```json
{
  "id": "f29306fef684036a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294302,
  "host_pid": "9e6742732c60:1",
  "hash": "e55aa26a0f826bad8c4a5ec95a9877ce870c9ac4f5378cc2208c6ce6287fb1af",
  "cid": "QmV1e55aa26a0f826bad8c4a5ec95a9877ce870c9ac4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294302,
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
      "evaluated_at": 1760294302
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
  "sig": "95f44b59b0463e79785f0cad216202d471653a08a9c3134d03b61f7ce5ffa047"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029441717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 50012230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}