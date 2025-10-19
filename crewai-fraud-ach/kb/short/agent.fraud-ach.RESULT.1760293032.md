```json
{
  "id": "a92b7c53f3c6060f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293032,
  "host_pid": "9e6742732c60:1",
  "hash": "b635e5a5fb379af8367c36e464bf962cd519e2959b3060db4b86eb3266d9d030",
  "cid": "QmV1b635e5a5fb379af8367c36e464bf962cd519e295",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293032,
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
      "evaluated_at": 1760293032
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
  "sig": "3351a839d5cb7763f288fef9c24f74d49970ce0f2c050072a66d2cdb78906f4c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595535562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 28391370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}