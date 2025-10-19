```json
{
  "id": "d695618bfbe04751",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291703,
  "host_pid": "9e6742732c60:1",
  "hash": "3aa4ebd7754444b01b3f2c75547aee66e9669740ab6aa56d662124be02729b53",
  "cid": "QmV13aa4ebd7754444b01b3f2c75547aee66e9669740",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291703,
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
      "evaluated_at": 1760291703
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
  "sig": "f97c5b9ab91be558d7ff0da02babfe703ccbeeca815914ea76e3ce75b6119afe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032365153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 71747495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': 'db9686895aceb522'}}}