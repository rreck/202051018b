```json
{
  "id": "5fba08b1768aa4f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291590,
  "host_pid": "9e6742732c60:1",
  "hash": "9257581dafc3cab8117e477e6b78b0bc0f286b063c5ec74ebf40521c4a1dfca2",
  "cid": "QmV19257581dafc3cab8117e477e6b78b0bc0f286b06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291590,
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
      "evaluated_at": 1760291590
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
  "sig": "6c7833fbaba859d6125bb7564652d811b0e23482e326585789d19a2cd3e6f437"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 80580422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}