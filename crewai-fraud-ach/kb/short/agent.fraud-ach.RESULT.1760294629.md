```json
{
  "id": "d3be3abef283b87c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294629,
  "host_pid": "9e6742732c60:1",
  "hash": "f669ec127f98a1faaca56a93b7243432963a83fd22e2bfd25aa1b52b20e15a69",
  "cid": "QmV1f669ec127f98a1faaca56a93b7243432963a83fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294629,
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
      "evaluated_at": 1760294629
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
  "sig": "08de1e838cf567419c8dcabab747aa812edd0b54be785224980a51977872abfa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 92842840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': '7a1c6367235ff38a'}}}