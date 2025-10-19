```json
{
  "id": "aeb6d24e97994b23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286038,
  "host_pid": "9e6742732c60:1",
  "hash": "4430493c7dffb5397b9b8bde52f9744bbf44a0ebd7ae20952ffd13b9b0d31a9e",
  "cid": "QmV14430493c7dffb5397b9b8bde52f9744bbf44a0eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286038,
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
      "evaluated_at": 1760286038
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
  "sig": "409aff84c96298f0b04b2b1bee9a7f6ee9e2307f51633553ff2bab6eb939aeb9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021053905
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}