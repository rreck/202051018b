```json
{
  "id": "440f83ca739167e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286127,
  "host_pid": "9e6742732c60:1",
  "hash": "5fb0d3a1b5e0b00635efd3008e3fb480c94da275c4b34cfac443263d58a3276a",
  "cid": "QmV15fb0d3a1b5e0b00635efd3008e3fb480c94da275",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286127,
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
      "evaluated_at": 1760286127
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
  "sig": "45260f414c00b2fdfa27801078e79500df04c1cc38e6149dbf00767d0b106504"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038607326
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}