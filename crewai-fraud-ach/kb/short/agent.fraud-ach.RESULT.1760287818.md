```json
{
  "id": "6840a0ec14626054",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287818,
  "host_pid": "9e6742732c60:1",
  "hash": "6079fddd0c914fe4bebb1320f110ad57468c8bc78348a44b1593f24c8904baa9",
  "cid": "QmV16079fddd0c914fe4bebb1320f110ad57468c8bc7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287818,
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
      "evaluated_at": 1760287818
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "5390636aa3769bd555f21564a184938a8773f5784cbe0500d11f5ff8c5c472e2"
}
```

Fraud detected: amount_anomaly (score: 80)
Transaction: 111000028335360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 542901876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': '8e80efed4b38ef8e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7437012}}}