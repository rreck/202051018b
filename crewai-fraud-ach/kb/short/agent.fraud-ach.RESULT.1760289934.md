```json
{
  "id": "361ab6439b8fae15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289934,
  "host_pid": "9e6742732c60:1",
  "hash": "7ba530fc82d9d7e5890a0ce836f6de154b591bc15d4571b9d65c4ee9f39d9c07",
  "cid": "QmV17ba530fc82d9d7e5890a0ce836f6de154b591bc1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289934,
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
      "evaluated_at": 1760289934
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
  "sig": "35f0d50caabb92728b06f835fdc339ec9596f3d04cc272bc9527587ce56a6cb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592248809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 23767308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': 'ed3ae9155c1e3edb'}}}maly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.93, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9380590}}}