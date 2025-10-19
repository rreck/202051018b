```json
{
  "id": "4f7fcea158cb9bc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289404,
  "host_pid": "9e6742732c60:1",
  "hash": "9e949b64e02e6cfcf771ab194c747a5106aaa9b6e36e4286d8db7f3fd8fac305",
  "cid": "QmV19e949b64e02e6cfcf771ab194c747a5106aaa9b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289404,
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
      "evaluated_at": 1760289404
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
  "sig": "af20f4c348247075461fe50e8f0623f54b0f75e7cb08db02916912982f2308ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598290210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': '255d3759171e1aec'}}} 1760285763, 'matching_hash': 'e635467487b35661'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}