```json
{
  "id": "5fcb6f6f1a36519f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286867,
  "host_pid": "9e6742732c60:1",
  "hash": "65f1ac965d249083138c8d2b71bcd81dba5f772e9d1d989b09a9398888a1f387",
  "cid": "QmV165f1ac965d249083138c8d2b71bcd81dba5f772e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286867,
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
      "evaluated_at": 1760286867
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "aedd09e8f57754e8c9ac95782337c644fc49fa68cfbd7413664587312e18c630"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15265440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}