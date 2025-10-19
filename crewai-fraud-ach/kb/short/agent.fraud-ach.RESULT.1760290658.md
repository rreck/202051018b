```json
{
  "id": "81f5b4f626f43a51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290658,
  "host_pid": "9e6742732c60:1",
  "hash": "edd93a8c3bfd6f0e8359415164eb6e6f5758b754bc215e67ca38b14580ec26b2",
  "cid": "QmV1edd93a8c3bfd6f0e8359415164eb6e6f5758b754",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290658,
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
      "evaluated_at": 1760290658
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
  "sig": "8cdc594284c38a2efaef0e8560162d540c60de9c2654bdcf956a7cccd9bc0fcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152451584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 61983636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '0001f0028f567562'}}}maly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6888614}}}