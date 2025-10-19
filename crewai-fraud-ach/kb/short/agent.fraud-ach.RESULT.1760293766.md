```json
{
  "id": "43ac7d989079dc89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293766,
  "host_pid": "9e6742732c60:1",
  "hash": "a3640ee45d35238bb0194bd33fd74c79a5112b32da8fa881a3f99afe8812151f",
  "cid": "QmV1a3640ee45d35238bb0194bd33fd74c79a5112b32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293766,
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
      "evaluated_at": 1760293766
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
  "sig": "ffefd13698e4280f861ddc56a3c9f9244bea777e2936d062a354146947cc0cfc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027727543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 76597425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '30f273873102b27a'}}}