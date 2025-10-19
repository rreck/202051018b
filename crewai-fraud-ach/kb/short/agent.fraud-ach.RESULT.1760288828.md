```json
{
  "id": "1307c55575089b1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288828,
  "host_pid": "9e6742732c60:1",
  "hash": "64f71c8a1425501df60a63d8d2da5b3a3f0a93b0e0b62c29771e2625910f2e9d",
  "cid": "QmV164f71c8a1425501df60a63d8d2da5b3a3f0a93b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288828,
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
      "evaluated_at": 1760288828
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
  "sig": "e06a317230e208a1db8704665f16c89867db4cb621c3468beaff00e823a15d1c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034778259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 19104120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': 'b6b775805828fc60'}}}