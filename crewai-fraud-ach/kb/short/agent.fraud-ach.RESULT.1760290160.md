```json
{
  "id": "770777a4c6fa929e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290160,
  "host_pid": "9e6742732c60:1",
  "hash": "e616db8656cde1f9f8a699897c56a02de193b986c93d6d2a2023c7373db7dbe3",
  "cid": "QmV1e616db8656cde1f9f8a699897c56a02de193b986",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290160,
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
      "evaluated_at": 1760290160
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
  "sig": "6cbc11cf5726563459162373a8985662c018bc15cefd6ba768bfb6a57274e48a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274546383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 37834940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '76da04c5629ac502'}}}