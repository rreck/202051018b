```json
{
  "id": "1251a12eaf62a72f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285030,
  "host_pid": "9e6742732c60:1",
  "hash": "424e45ca9d24fe326c2b953da8a006bbe903f04f4a19bfb87b1c8598758acdaa",
  "cid": "QmV1424e45ca9d24fe326c2b953da8a006bbe903f04f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285030,
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
      "evaluated_at": 1760285030
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
  "sig": "2beaae1d0cc98d5f44233907ce25f57fbe4215bfc0a9a9f8c41fc5ec86247ad9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244838202
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760284979, 'matching_hash': 'f90729670e1d4f48'}}}