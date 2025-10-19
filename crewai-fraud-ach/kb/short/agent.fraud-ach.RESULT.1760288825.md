```json
{
  "id": "ee0fb251d2c821cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288825,
  "host_pid": "9e6742732c60:1",
  "hash": "1598950a44a8e2d26030188b2c9070a1a14c1e17dd39d93135aa54a10cc9c607",
  "cid": "QmV11598950a44a8e2d26030188b2c9070a1a14c1e17",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288825,
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
      "evaluated_at": 1760288825
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
  "sig": "c9ef5a5f0f88544fadc563673bca2e1c2de84f375dd89e2aff34b8161697e8ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026184073
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 32783205, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': '5c433365b4c36f89'}}}