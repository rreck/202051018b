```json
{
  "id": "d54c1b4b9dcbb17d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290546,
  "host_pid": "9e6742732c60:1",
  "hash": "270663dce0ceefb486696aa54f5f2bd6fcde03a9b144052648016f33e76c4b72",
  "cid": "QmV1270663dce0ceefb486696aa54f5f2bd6fcde03a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290546,
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
      "evaluated_at": 1760290546
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
  "sig": "567961accdd3b3450137b6f136453adae543e01e6177422607510ddd69a4c6e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279312604
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 18156051, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '998be1a53ec99162'}}}