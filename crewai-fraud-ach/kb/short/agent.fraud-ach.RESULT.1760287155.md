```json
{
  "id": "f3f597e14b688a67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287155,
  "host_pid": "9e6742732c60:1",
  "hash": "efc46bf5f827115bbd71d6ac565d80c468ebb29c6629d56377630c0ab7fdaf35",
  "cid": "QmV1efc46bf5f827115bbd71d6ac565d80c468ebb29c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287155,
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
      "evaluated_at": 1760287155
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
  "sig": "d4cdf00e707ce7c20e4be2062e95b4f872b67e796e6b43138dbd1da2f0a85f74"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000032200831
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': 'cae8555d53751756'}}} 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760284979, 'matching_hash': '4224f1af7034834c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5663035}}}