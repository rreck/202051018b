```json
{
  "id": "b1b6751453bafb42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294696,
  "host_pid": "9e6742732c60:1",
  "hash": "8c8bd140a5cdb2acdebbfe13b1a20aaf28164f39ae198fd3ce97a60924dbb9e2",
  "cid": "QmV18c8bd140a5cdb2acdebbfe13b1a20aaf28164f39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294696,
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
      "evaluated_at": 1760294696
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
  "sig": "1dce23a67970ac6f94587bc8027918e22ff048c7a08bfd79ceca685e80c290d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244506997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 84081888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '00a59e186c59db13'}}}