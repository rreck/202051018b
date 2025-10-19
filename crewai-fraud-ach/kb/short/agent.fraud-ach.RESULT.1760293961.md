```json
{
  "id": "9fc1f41b8eb593e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293961,
  "host_pid": "9e6742732c60:1",
  "hash": "79e791bfa23ef012da4c1513f42ce5d511aa011c8e76d8ded98fdc73faf4e7a3",
  "cid": "QmV179e791bfa23ef012da4c1513f42ce5d511aa011c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293961,
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
      "evaluated_at": 1760293961
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
  "sig": "eefa2e00c62fac5fe6abe349da8ab6f1942c9967dbaf012d3f63a9811e3b10ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 30577683, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}