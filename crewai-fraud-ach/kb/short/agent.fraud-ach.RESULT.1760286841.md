```json
{
  "id": "d32a926ac435f6f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286841,
  "host_pid": "9e6742732c60:1",
  "hash": "8bb4d05355792d80856562265b6295e1de0a262d1738daf6a65844ecaf74ec94",
  "cid": "QmV18bb4d05355792d80856562265b6295e1de0a262d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286841,
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
      "evaluated_at": 1760286841
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
  "sig": "27c3159b532ac9a59510f8c6dac53e0e79a4e84c3669d8240077c5bc2283eb3b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039536800
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': 'd097f3de33be356c'}}}