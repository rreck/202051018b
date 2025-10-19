```json
{
  "id": "170274a688380f6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288140,
  "host_pid": "9e6742732c60:1",
  "hash": "e1ef0cb1d73a3231769dd6f7a6ada9b604668c65d3972da5a1b34f0c0b602748",
  "cid": "QmV1e1ef0cb1d73a3231769dd6f7a6ada9b604668c65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288140,
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
      "evaluated_at": 1760288140
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
  "sig": "5062fc8b2c3e03a870be79e6c868b4231999acffb7b747ce913f44946580665f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279650502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 20954556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': 'f07ec2819f69af8b'}}}