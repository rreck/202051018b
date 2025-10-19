```json
{
  "id": "908620e8d88be016",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285977,
  "host_pid": "9e6742732c60:1",
  "hash": "5a3d9d72ca190f287f01340bee0385d1f064de6811a962e52633297eb34bd115",
  "cid": "QmV15a3d9d72ca190f287f01340bee0385d1f064de68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285977,
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
      "evaluated_at": 1760285977
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
  "sig": "1893ad73e4cbf8977ca85d7ac10bbdc3c3fcd8114a00945e563ac609eee6c723"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241083307
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '06ddfe971a6a4d24'}}}