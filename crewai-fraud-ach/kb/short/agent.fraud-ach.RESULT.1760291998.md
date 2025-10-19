```json
{
  "id": "471a3ca86fa427b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291998,
  "host_pid": "9e6742732c60:1",
  "hash": "cc60afbbaa086d33890d7b844f6ecc18260017b40e575d7fd44b1a58f3ded81b",
  "cid": "QmV1cc60afbbaa086d33890d7b844f6ecc18260017b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291998,
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
      "evaluated_at": 1760291998
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
  "sig": "b885cdb0ed67ebe95fe02e23fb48a9be9d544fc0293685babb7b8e6dcdeae04f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152831142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 37660160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'a7aa45f184f497a2'}}}