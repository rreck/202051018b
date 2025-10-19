```json
{
  "id": "ba9e33345fbef333",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294334,
  "host_pid": "9e6742732c60:1",
  "hash": "c3189265ba97260f95f57a472b65bd184011d12755d9fe22b954a59a7d7e71bb",
  "cid": "QmV1c3189265ba97260f95f57a472b65bd184011d127",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294334,
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
      "evaluated_at": 1760294334
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
  "sig": "eed08eeac0ef9c3e12cf015f6d56d93f9d7a59dac4636fd8669d3bc3a0fb8e70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153776491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 20884348, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '94746339473c09ed'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8595712}}}