```json
{
  "id": "8ae12585c4771e43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293572,
  "host_pid": "9e6742732c60:1",
  "hash": "acb260cac9cab125798fa29f5d6e12ab27f96cf140bdc9150bd954bef38c70c2",
  "cid": "QmV1acb260cac9cab125798fa29f5d6e12ab27f96cf1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293572,
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
      "evaluated_at": 1760293572
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
  "sig": "37c7455225195821e2bf8ec68f42a0d83ddd366184049d042efb1f23d4eece94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596849873
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 63077599, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'd03c8a9dd75ef277'}}}