```json
{
  "id": "b07591e0a5d517d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291980,
  "host_pid": "9e6742732c60:1",
  "hash": "1d0cd3eae441735a50965f86040420a7878b3be260925365cdaaf00cff472784",
  "cid": "QmV11d0cd3eae441735a50965f86040420a7878b3be2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291980,
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
      "evaluated_at": 1760291980
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
  "sig": "d6aaf943cb2ddf915a03249324b2c3360cb19bb3cfa70b1199dea99e82d7ff1c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034020503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}