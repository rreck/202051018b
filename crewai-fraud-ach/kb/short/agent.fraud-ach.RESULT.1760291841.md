```json
{
  "id": "cfc924f03946c125",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291841,
  "host_pid": "9e6742732c60:1",
  "hash": "16263bc8ea34ef7f3402d1ac00ac90200e75aaec40172fdabe2a78f4783859fa",
  "cid": "QmV116263bc8ea34ef7f3402d1ac00ac90200e75aaec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291841,
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
      "evaluated_at": 1760291841
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
  "sig": "8199431fb79ba9815e23c8bd6e165f5434ef30f17cee6e3b203b7bc0a9139884"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245381675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 30179864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}