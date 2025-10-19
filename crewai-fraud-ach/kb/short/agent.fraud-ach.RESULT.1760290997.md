```json
{
  "id": "af800469aae3fa2b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290997,
  "host_pid": "9e6742732c60:1",
  "hash": "3bb61bf0cb7739c6ee36ad7071d47924fa0602f86ea5e3c954191fa0d1607f79",
  "cid": "QmV13bb61bf0cb7739c6ee36ad7071d47924fa0602f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290997,
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
      "evaluated_at": 1760290997
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
  "sig": "48ee70564487ea1292545b4e1f75e16889ff2b7d535fc45459f59479607a17b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 47391736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}